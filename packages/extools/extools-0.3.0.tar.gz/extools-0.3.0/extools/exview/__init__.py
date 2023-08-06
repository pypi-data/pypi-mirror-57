"""
ExView is a fully functional wrapper around the Extender View object
that raises exceptions instead of providing non-zero returns on error
for the methods defined in :py:data:`extools.exview.ExView.WRAP`.

It supports all the methods of the ``Extender.View`` class, along with many
extra helpers.

On startup an ``ExView`` introspects the underlying Sage view to automatically
determine:

- The view's composition tree
- The field names
- The allowed indexes and their key fields

Based on this information, the class automatically configures itself to:

- Self-compose on request (see :py:meth:`extools.exview.ExView.compose`)
- Validate orders and keys before errors are raised by Sage
- Automatically add the correct helpers
    - For detail views, the ``.lines()``, ``.lines_from(start, end)``,
      ``.lines_where(key=value, key=value, ...)`` generators and ``newline()``
      helper.
    - For optional field views, or any view composed with an optional
      field view, enable the ``create_optfield``, ``update_optfield``,
      ``get_optfield``, ``update_or_create_optfield``, ``seek_to_optfield``,
      and ``delete_optfield`` helpers.

"""
from contextlib import contextmanager

from extools import success
from extools.exmessages import ExMessages

from .errors import (ExViewError, ExViewComposeError,
                     ExViewOpenError, ExViewInvalidOrder,
                     ExViewFieldDoesNotExist, ExViewIndexError, )

try:
    from accpac import View
except ImportError as e:
    # This happens when the tools are imported outside of the Extender env.
    # We can pass to let the tool do its work (likely sphinx making docs).
    pass

EXVIEW_BLACKLIST = [ "OE0999", ]
"""Views that can never be composed with any other."""

exm = ExMessages("extools.exview", ExMessages.DEBUG)

@contextmanager
def exview(rotoid, index=-1, seek_to={}):
    """Context manager to cleanly open and use an ExView.

    :param rotoid: the RotoID of the Sage view.
    :type rotoid: str
    :param index: the index to open the view with.
    :type index: int
    :param seek_to: field value mapping to seek to after opening. When set
        to an empty dictionary, seek to the first line in the view. If set
        to ``None``, disable seek after opening.
    :type seek_to: dict|None
    :raises: ExViewError
    :rtype: None

    When called the context manager will yield an open view
    object. On exit of the block the view will be closed cleanly.

    .. code-block:: python

        with exview("EX0001") as view:
            try:
                view.recordClear()
                view.browse("")
                view.fetch()
                value = view.get("KEY")
            except ExToolError as err:
                showMessageBox("Failed to get KEY, {}.".format(err))
    """
    exv = ExView(rotoid, index, seek_to)
    try:
        yield exv
    finally:
        exv.close()

class ExView():
    """An exception raising wrapper around the Extender View class.

    ExViews can be used to replace repetitive error checking and to
    take advantage of the try/except/else/finally construct in Python.

    :param rotoid: the RotoID of the Sage view.
    :type rotoid: str.
    :param index: the index to open the view with.
    :type index: int.
    :param seek_to: field value mapping to seek to after opening. When set
        to an empty dictionary, seek to the first line in the view. If set
        to ``None``, disable seek after opening.
    :type seek_to: dict|None
    :raises: ExViewError
    :rtype: ExView

    Replace this:

    .. code-block:: python

        view = openView("EX0001")
        if not view:
            showMessageBox("Failed to open view.")
            return 1
        rc = view.recordClear()
        if rc != 0:
            showMessageBox("Failed to record clear.")
            return 1
        br = view.browse("")
        if br != 0:
            showMessageBox("Failed to browse.")
            return 1
        fe = view.fetch()
        if fe != 0:
            showMessageBox("Failed to fetch.")
            return 1

        value = view.get("KEY")

        if view:
            view.close()

    With this:

    .. code-block:: python

        try:
            view = ExView("EX0001")
            value = view.get("KEY")
        except ExToolError as err:
            showMessageBox("Failed to get KEY, {}.".format(err))
            return 1
        finally:
            view.close()

    You can even include the traceback using the ExMessages:

    .. code-block:: python

        try:
            view = ExView("EX0001")
            value = view.get("KEY")
        except ExToolError as err:
            # Use ExMessages to display an error level message box and
            # log to a file (if configured). The last exception traceback
            # will be included in both the box and log if ``exc_info=True``.
            exm.error("Failed to get KEY, {}.".format(err), exc_info=True)
            return 1
        finally:
            view.close()

    ExViews can also self-compose, composing the view and all its related
    views automatically.  Fully composed views require more database
    operations every time the header is changed and do not perform as well as
    standalone views or SQL access.  However, in cases where performance isn't
    paramount you cannot beat the convenience.

    .. code-block:: python

        from extools.extools import success
        from extools.exview import ExView
        from extools.exmessages import ExMessages

        exm = ExMessages("compose-test", ExMessages.DEBUG)

        try:
            exv = ExView("OE0520")
            exv.compose()
        except Exception as e:
            exm.error("Failed to setup view: {}".format(e), exc_info=True)

        # Seek to order ORD000000000064
        try:
            # Use index 1, key (ORDNUMBER, )
            exv.order(1)
            exv.seek_to(ORDNUMBER="ORD000000000064")
        except Exception as e:
            exm.error("Failed to seek: {}".format(e), exc_info=True)

        # Perform an action on each of the detail lines in the order
        try:
            for line in exv.oe0500.lines():
                exm.info("Read new line {}".format(line.get("ITEM")))
                # perform many important actions...
        except Exception as e:
            exm.error("Failed to perform action: {}".format(e), exc_info=True)
    """

    WRAP = [ 'fetchLock', 'read', 'readLock',
             'insert', 'delete', 'init',
             'post', 'process', 'verify', 'recordClear',
             'exists', 'dirty', 'unlock', 'cancel',
             'recordGenerate', 'put', 'browse', ]
    """These View functions raise an ``ExViewError`` on non-zero return."""

    DETAIL_VIEW_HINTS = {'LINENUM', 'DETAILNUM', }
    """Views containing any one of these fields may be detail views."""

    OPTFIELD_VIEW_HINTS = {'OPTFIELD', }
    """Views containing any one of these fields may be optional field views."""

    __exview_cache = {}
    """The view cache is shared by all instances of a class. Views can only be
    opened once per index, to avoid opening views twice on compose, 
    cache them here.
    
    format: { index: { viewid: view } }
    """

    def __init__(self, rotoid, index=-1, seek_to={}, _root=True):
        """Introspect and setup the object based on the results."""
        self.rotoid = rotoid
        self.index = index
        
        # Is this a root view or opened on compose?
        self._root = _root

        # The underlying Extender ``View`` object.
        self._view = None

        # list of view rotoids this view composes with
        self._views = []

        # pointers to the views this view composes with in the view_cache
        self._cviews = []
        
        self.composed = False

        # The current view order index.
        self._order = 0

        # The human readable field names in the view.
        self.field_names = []

        # The indexes supported by this view, a list of field name tuples.
        self.indexes = []

        # Open the underlying View
        self._open()

        # Wrap the view to raise on error instead of returning non-zero
        self._setup_wrapper()

        ## Introspection stuff

        # Get the field names
        self._get_field_names()

        # the indexes
        self._get_indexes()
        
        # the composed views
        self._get_composed_views()

        self.detail_view = None
        # If this looks like a detail view, then add extra detail functions.
        self._check_and_setup_detail_view()

        # If this looks like an optional field view, then add extra functions.
        self.optfield_view = None
        self._check_and_setup_optfield_view()

        # Open the first record.
        if isinstance(seek_to, dict):
            self.seek_to(**seek_to)

    def cached_view(self, viewid):
        """Get a view from the view cache.
        
        :param viewid: the view ID, i.e. OE0500
        :type viewid: str
        :raises: ExViewError
        """
        view = self._view_cache.get(viewid)
        created = False
        if not view:
            view = ExView(viewid, self.index, _root=False)
            self._view_cache[viewid] = view
            created = True
        
        return view, created

    def remove_cached_view(self, viewid):
        """Remove and close a view from the cache.
        
        :param viewid: the view ID, i.e. OE0500
        :type viewid: str
        :raises: ExViewError
        """
        # We remove ourself from the cache in close only.
        if viewid == self.rotoid:
            raise ExViewError(self.rotoid, action="remove_cache")
            
        view = self._view_cache.get(viewid)
        if view:
            view.close()
        
        try:
            del self._view_cache[viewid]
        except KeyError:
            pass
    
    @property
    def _view_cache(self):
        """Get the views cached for this index."""
        
        cache_for_index = self.__exview_cache.get(self.index, {})
        if not cache_for_index:
            self.__exview_cache[self.index] = cache_for_index
        
        return self.__exview_cache[self.index]

    def _check_and_setup_detail_view(self):
        """Check if this or a composed view is a detail view.

        :returns: True if self is or is composed with a detail view.
        :rtype: bool
        """
        if self.DETAIL_VIEW_HINTS.intersection(self.field_names):
            self.detail_view = self
        else:
            for view in self._cviews:
                if view and self.DETAIL_VIEW_HINTS.intersection(
                                                            view.field_names):
                    self.detail_view = view
                    break

        if self.detail_view:
            self._detail_func_factory(self.detail_view)
            return True

        return False

    def _check_and_setup_optfield_view(self):
        """Check if this or a composed view is an optional field view.

        :returns: True if self is or is composed with an optional field view.
        :rtype: bool
        """
        if self.OPTFIELD_VIEW_HINTS.intersection(self.field_names):
            self.optfield_view = self
        else:
            for view in self._cviews:
                if view and self.OPTFIELD_VIEW_HINTS.intersection(
                                                            view.field_names):
                    self.optfield_view = view
                    break

        if self.optfield_view:
            self._optf_func_factory(self.optfield_view)
            return True

        return False

    def _open(self):
        """Open the underlying view object. Called automatically on init.

        :raises: ExViewOpenError
        :rtype: None
        """
        if self._view:
            _c = self._view.close()
        self._view = View(self.rotoid, self.index)
        if not self._view:
            raise ExViewOpenError(self.rotoid, action_return=self._view)
        o = self._view.order(self._order)
        if not success(o):
            raise ExViewOrderError(self.rotoid,
                                   order=self.order,
                                   action_return=o)

        self._view_cache[self.rotoid] = self
        return True

    def _get_field_names(self):
        """Get the field names from their positions in the view."""
        for i in range(0, self._view.fields()):
            field = self._view.fieldByPosition(i)
            if field:
                self.field_names.append(field.name)

    def _get_indexes(self):
        """Get the indexes and their constituent fields."""
        for i in range(0, self._view.keyCount()):
            k = self._view.key(i)
            names = [self._view.fieldByIndex(j).name for j in k.fields]
            self.indexes.insert(i, names)
    
    def _get_composed_views(self):
        """Get the composed view list."""
        self._views = self._composed_views()
    
    def _get_index_for_fields(self, fields):
        sfields = set(fields)
        for i in range(0, len(self.indexes)):
            if sfields == set(self.indexes[i]):
                return i

    def _setup_wrapper(self):
        """Setup a wrapper function for all calls that should raise.

        Called on init, dynamically assign wrapper methods on the ``ExView``
        instance that raise when the underlying View returns a non-zero
        value.

        Cannot be used to wrap methods: that don't return 0 on success
        (looking at you, ``.get()``); for which a non-zero return may be
        expected (think ``while(view.fetch() == 0))``); that interact with
        the ExView instance state (we need to track the ``order``).
        """
        for funcname in self.WRAP:
            func = self._wrap_func_factory(funcname)
            setattr(self, funcname, func)

    def _wrap_func_factory(self, funcname):
        """Get a function that raises ExViewError on non-zero View return.

        :param funcname: name of the View function to wrap.
        :type funcname: str
        :returns: wrapper around ``self._view.<funcname>``
        :rtype: function
        """
        def func(*args, **kwargs):
            fu = getattr(self._view, funcname)
            r = fu(*args, **kwargs)
            if not success(r):
                raise ExViewError(self.rotoid,
                                  action=funcname,
                                  action_return=r)
            return r
        return func

    def _composed_views(self):
        """Get a list of all views that can be composed with this one.

        This method automatically filters out views that do not support
        composition defined in ``EXVIEW_BLACKLIST``.

        :returns: view ids or None in the compose order.
        :rtype: list
        """
        return [rotoid if not rotoid in EXVIEW_BLACKLIST else None
                for rotoid in self._view.composeInfo().views]

    def _optf_func_factory(self, optfield_view):
        """Adds methods to the instance for working with optional fields.

        :param optfield_view: The Optional field ExView instance.
        :type optfield_view: ExView
        :rtype: None
        """
        self.optfield_view = optfield_view

        def create_optfield(field, value):
            self.optfield_view.recordClear()
            self.optfield_view.recordGenerate()
            self.optfield_view.put("OPTFIELD", field)
            self.optfield_view.put("VALUE", value)
            self.optfield_view.insert()
        self.create_optfield = create_optfield

        def update_optfield(field, value):
            self.seek_to_optfield(field)
            self.optfield_view.put("VALUE", value)
            self.optfield_view.update()
        self.update_optfield = update_optfield

        def delete_optfield(field):
            self.seek_to_optfield(field)
            self.optfield_view.delete()
        self.delete_optfield = delete_optfield

        def get_optfield(field):
            self.seek_to_optfield(field)
            return self.optfield_view.get("VALUE")
        self.get_optfield = get_optfield

        def seek_to_optfield(field):
            self.optfield_view.recordClear()
            self.optfield_view.put("OPTFIELD", field)
            self.optfield_view.read()
        self.seek_to_optfield = seek_to_optfield

        def update_or_create_optfield(field, value):
            try:
                self.get_optfield(field)
            except ExViewError:
                self.create_optfield(field, value)
            else:
                self.update_optfield(field, value)
        self.update_or_create_optfield = update_or_create_optfield

        def has_optfield(field):
            try:
                self.get_optfield(field)
                return True
            except ExViewError:
                return False
        self.has_optfield = has_optfield

        def all_optfields():
            self.optfield_view.browse("",1)
            while self.optfield_view.fetch():
                yield self.optfield_view
        self.all_optfields = all_optfields

        @property
        def optfields():
            return { optf.get("OPTFIELD"): optf.get('VALUE')
                     for optf in self.all_optfields()}
        self.optfields = optfields


    def _detail_func_factory(self, view):
        """Adds methods to the instance for working with detail views."""
        def lines():
            """Generator that yields each line in a detail view."""
            view.recordClear()
            view.browse("", 1)
            while(view.fetch()):
                yield view
        self.lines = lines

        def lines_from(start, end=None):
            """Generator that yields each line from index start to end.

            :param start: (int) line index to start from.
            :param end: (int) line index to end on (inclusive).
            :yields: (ExView) detail view on line.
            """

            index = 0
            for line in self.lines():
                if start <= index:
                    if end and end >= index:
                        yield line
                index += 1
        self.lines_from = lines_from

        def lines_where(**criteria):
            """Generator that yields each line from index start to end.

            :param criteria: ``key=value`` criteria to browse to.
            :type criteria: dict
            :yields: ExView
            :raises: ExViewError
            """
            view.recordClear()
            view.browse(" AND ".join(['{} = "{}"'.format(k, v)
                                      for (k, v) in criteria.items()]))
            while(view.fetch()):
                yield view
        self.lines_where = lines_where

    def all(self, ascending=True):
        """Generator that yields once for each record in the view.
        
        :raises: ExViewError
        :yields: ExView
        """
        self.recordClear()
        self.browse("", ascending)
        while(self.fetch()):
            yield self
    
    def where(self, **criteria):
        """Generator that yields each line matching the provided criteria.

        :param criteria: ``field=value`` criteria to browse to.
        :type critera: dict
        :yields: ExView
        :raises: ExViewError
        """
        self.recordClear()
        self.browse(" AND ".join(['{} = "{}"'.format(k, v)
                                  for (k, v) in criteria.items()]))
        while(self.fetch()):
            yield self
    

    def create(self, **fields):
        """Generate and insert a new entry with field/value pairs.

        :param fields: field value pairs that will be set on the new entry.
        :type fields: field=value
        :rtype: None
        :raises: ExViewError
        """
        self.recordClear()
        self.recordGenerate()
        for (field, value) in fields.items():
            self.put(field, value)
        self.insert()

    def update(self, **fields):
        """Update an entry with field/value pairs.

        :param kwargs: field value pairs that will be set on the new entry.
        :type kwargs: field=value
        :rtype: None
        :raises: ExViewError
        """
        for (field, value) in fields.items():
            self.put(field, value)
        up = self._view.update()
        if not success(up):
            raise ExViewError(self.rotoid, action="update", action_return=up)

    def fetch(self):
        """A special wrapper because a non-zero fetch return isn't an error.

        :returns: True if a new line was fetched, else False.
        :rtype: bool
        """
        f = self._view.fetch()
        if success(f):
            return True
        return False

    def get(self, field):
        """A special wrapper because get doesn't return 0 on success.

        :param field: field name to get.
        :type field: str
        :returns: value in the view.
        :rtype: builtin.*
        :raises: ExViewFieldDoesNotExist
        """
        if not field in self.field_names:
            raise ExViewFieldDoesNotExist(self.rotoid,
                                          field=field,
                                          action="get")

        return self._view.get(field)

    def order(self, ord):
        """Wrap the order to track state in the class as it can't be queried.

        :param index: the index ID to order by.
        :type index: int
        :rtype: None
        :raises: ExViewError
        """
        o = self._view.order(ord)

        if not success(o):
            raise ExViewOrderError(self.rotoid, ord, action_return=o)

        self._order = ord
        return o

    def compose(self):
        """Recursively compose this and all related views.

        Enables this ``ExView`` to self-compose based on the compose
        information stored in the View.

        :raises: ExViewComposeError

        The algorithm for self-composing an ExView is roughly::

                for each view in the compose info list:
                    if the view isn't cached:
                        open and cache the view in self._view_cache
                        compose the view (recurse on the child view)

                compose self with views in compose info list.
                for each composed view:
                    assign a new property to self pointing to the composed view

        This results in an object with properties named after the view RotoID.

        In action, you may:

        .. code-block:: python

            try:
                exv = ExView("OE0520")
                exv.compose()
                for line in exv.oe0500.lines():
                    for optfield in line.oe0501.lines():
                        # Process the optional field.
            except ExViewComposeError as e:
                # Handle a compose failure.
            except ExViewOpenError as e:
                # Handle a view open error
            except ExViewError as e:
                # handle an error processing the lines.

        Note that :py:class:`extools.exview.ExViewComposeError` and
        :py:class:`extools.exview.ExViewOpenError` are both children of
        :py:class:`extools.exview.ExViewError`, so if you don't care which
        failure occurred, you can just except the more general ``ExViewError``.

        For more information and background, see :ref:`Self-composing views`.
        """
        try:
            # Find the blacklist filtered composed view list
            self._views = self._composed_views()

            # Store the views to compose with this one in order.
            self._cviews = []

            # For each of the composed views...
            for i in range(0, len(self._views)):

                # The entry may be None or blacklisted. Either way, there is
                # no view to compose at this index.
                if self._views[i] and not self._views[i] in EXVIEW_BLACKLIST:

                    # Try to get the view from the class view cache.
                    view, created = self.cached_view(self._views[i])

                    # If it isn't cached, open and compose it.
                    if created:
                        view.compose()

                    # Add the composed view to the compose list.
                    self._cviews.insert(i, view)
                else:
                    # The entry was None, propagate to preserve argument order.
                    self._cviews.insert(i, None)

            # All the views I compose with are composed, compose me!
            if success(self._view.compose(*self._cviews)):

                # Assign a new property pointing to the view.
                for view in self._cviews:
                    if view:
                        setattr(self, view.rotoid.lower(), view)

                # Re-check the for optional field  and detail views.
                self._check_and_setup_optfield_view()
                self._check_and_setup_detail_view()
                self.composed = True
                
        except RuntimeError as err:
            raise ExViewComposeError(self.rotoid, compose_list=self._views,
                                     triggering_exc=err)

    def _close_all_cached_views(self):
        """Close all composed views in the _view_cache.
        
        :raises: ExViewError
        """
        views = [v for v in self._view_cache.values()]
        for view in views:
            if view:
                if not view._root:
                    self.remove_cached_view(view.rotoid)
            else:
                 self.remove_cached_view(view.rotoid)


    def close(self):
        """Close me cleanly, closing all composed views first.
        
        :rtype: None
        :raises: ExViewError
        """

        if self._root and len(self._view_cache.values()) > 1:
            self._close_all_cached_views()
        c = self._view.close()
        if not success(c):
            raise ExViewError(self.rotoid, action='close', action_return=c)
        if self.rotoid in self._view_cache.keys():
            del self._view_cache[self.rotoid]

    def seek_to(self, **kwargs):
        """Intelligently seek to a specific entry.

        This seek to implementation accepts an arbitrary set of field value
        pairs and then seeks to the entry using one of three methods:

        - If the current View order index is made up of exactly the fields
          requested, perform a straight put and read.
        - If the current View has an index made up of exactly the fields
          requested, temporarily change the index and perform and put a read.
        - If the current View does not have and index made up of exactly the
          fields requested, attempt to browse and fetch the record.

        :param kwargs: (key)=(value) pairs, where the keys must be the same as
                        the current index keys.
        :type kwargs: dict
        :rtype: None
        :raises: ExViewError

        .. code-block:: python

            viewid = "OE0500"
            try:
                exv = ExView(viewid) # Open Order Details, default view order 0

                # Seek to the 7th line of the order with unique key 1024
                # The default view order is 0: (ORDUNIQ, LINENUM, )
                exv.seek_to(ORDUNIQ=1024, LINENUM=7)

                # Get details from the record and process or update.
                item = exv.get("ITEM")
                ...
            except ExViewError as e:

                # The error, "failed to [open|seek]", is contained in the
                # error message.
                showMessage("Error doing something with view {}: {}".format(
                    viewid, e))

        """
        # If the current index matches the fields, read the record.
        if set(self.indexes[self._order]) == set(kwargs.keys()):
            # Try to read the record
            self.recordClear()
            for (key, value) in kwargs.items():
                self.put(key, value)
            self.read()

        elif self._get_index_for_fields(kwargs.keys()):
            # If there exists an index with these fields, use it.
            # Set the order back after reading
            index = self._get_index_for_fields(kwargs.keys())
            if index is not None:
                # Try to read the record
                original_order = self._order
                try:
                    self.order(index)
                    self.recordClear()
                    for (key, value) in kwargs.items():
                        self.put(key, value)
                    self.read()
                finally:
                    self.order(original_order)
        else:
            # No index exists with these fields, try browsing.
            criteria = " AND ".join(['{} = "{}"'.format(f, v)
                                     for (f, v) in kwargs.items()])
            self.recordClear()
            self.browse(criteria)
            self.fetch()

    @property
    def is_optfield_view(self):
        """Is this an optional field view?

        :returns: True if this view is an optional field view.
        :rtype: bool
        """
        if self.optfield_view and self.optfield_view == self:
            return True
        return False

    @property
    def has_optfield_view(self):
        """Is this view composed with an optional field view?

        :returns: True if this view is composed with an optional field view.
        :rtype: bool
        """
        if self.optfield_view and not self.optfield_view == self:
            return True
        return False

    def __getattr__(self, attr):
        """Check all unknown attributes against the underlying view.

        This is where some of the magic is. When a call is made to a property
        or method that is not explicitly (either static or dynamic)
        defined in ExView this handler is triggered by the interpreter.

        Before returning an ``AttributeError``, which is the default
        behaviour, check to see if the view has the attribute.  If so,
        delegate the call.

        An example is the ``.handle()`` method, a key one on views.  It isn't
        defined explicitly or dynamically on the ``ExView`` class but if you
        try calling ``exview.handle`` it will return the host view handle.
        The call was delegated to the ``_view`` here.
        """
        if hasattr(self, "_view") and hasattr(self._view, attr):
            return getattr(self._view, attr)
        raise AttributeError("Attr {} doesn't exist on {} or View.".format(
            attr, self.rotoid))

    def __str__(self):
        return "ExView({})".format(self.rotoid)
