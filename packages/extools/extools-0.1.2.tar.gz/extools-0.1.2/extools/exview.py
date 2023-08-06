"""
extools.exview - An exception raising view wrapper.

ExView is a fully functional wrapper around the Extender View object
that raisies exceptions instead of providing non-zero returns on error.
"""
from contextlib import contextmanager
from extools.extools import success, ExToolsError

try:
    from accpac import openView
except ImportError as e:
    # This happens when the tools are imported outside of the Extender env.
    # We can pass to let the tool do its work (likely sphinx making docs).
    pass


class ExViewError(ExToolsError): pass
class ExViewOpenError(ExViewError): pass

@contextmanager
def exview(rotoid, index=-1):
    """Context manager to cleanly open and use an ExView.

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
    exv = ExView(rotoid, index)
    try:
        yield exv
    finally:
        exv.close()

class ExView():
    """An exception raising wrapper around the Extender View class.

    ExViews can be used to replace repetitive error checking and to
    take advantage of the try/except/else/finally construct in Python.

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
            view.recordClear()
            view.browse("")
            view.fetch()
            value = view.get("KEY")
        except ExToolError as err:
            showMessageBox("Failed to get KEY, {}.".format(err))
            return 1
        finally:
            view.close()

    You can even include the traceback using the ExMessageWriter:

    .. code-block:: python

        try:
            view = ExView("EX0001")
            view.recordClear()
            view.browse("")
            view.fetch()
            value = view.get("KEY")
        except ExToolError as err:
            # Use ExMessageWriter to display an error level message box and
            # log to a file (if configured). The last exception traceback
            # will be included in both the box and log if ``exc_info=True``.
            exm.error("Failed to get KEY, {}.".format(err), exc_info=True)
            return 1
        finally:
            view.close()

    """

    _NOWRAP = ['getHandle', 'setHandle', 'setRvhAndView',
               'fields', 'getAccess', 'setAccess',
               'fieldByPosition', 'fieldByIndex',
               'fieldByName', 'getOriginal', 'replaceFields',
               'keyCount', 'key', 'composeInfo', 'getPresents',
               'attribs', ]
    _NOARGS = ['fetch', 'fetchLock', 'read', 'readLock',
               'insert', 'update', 'delete', 'close', 'init',
               'post', 'process', 'verify', 'recordClear',
               'exists', 'dirty', 'cancel', 'unlock', ]

    _UNIARG = ['get', 'order', 'recordGenerate', ]
    _MULTIARGS = ['put', 'browse', ]

    def __init__(self, rotoid, index=-1):
        """Wrap the view with rotoid using index."""
        self.rotoid = rotoid
        self._view = None
        self.index = index
        self._set_nowrap()
        self._set_noargs()
        self._set_multiargs()
        self._open()

    def _open(self):
        """Open the underlying view object."""
        if self._view:
            _c = self._view.close()
        self._view = openView(self.rotoid, self.index)
        if not self._view:
            raise ExViewOpenError("open failed {}".format(self._view))
        return True

    def _set_nowrap(self):
        for f in self._NOWRAP:
            def nowrap(self, *args, **kwargs):
                fu = getattr(self._view, f)
                return fu(*args, **kwargs)
            setattr(self, f, nowrap)

    def _set_noargs(self):
        for f in self._NOARGS:
            def noargs(self, *args, **kwargs):
                fu = getattr(self._view, f)
                r = fu()
                if not success(r):
                    raise ExViewError("{} failed: {}".format(f, r))
                return r
            setattr(self, f, noargs)

    def _set_multiargs(self):
        for f in self._UNIARG.extend(self._MULTIARGS):
            def multiargs(self, *args, **kwargs):
                fu = getattr(self._view, f)
                r = fu(*args, **kwargs)
                if not success(r):
                    raise ExViewError("{}({}) failed: {}".format(f, args, r))
                return r
            setattr(self, f, multiargs)

    def compose(self, index=89):
        try:
            self._views = self.composeInfo().views
            self._cviews = []
            for i in range(0, len(self._views))
                if self._views[i]:
                    self._cviews[i] = openView(self._views[i], index)

            co = self._view.compose(*_cviews)
            if not success(co):
                raise ExViewError("hostcompose returned {}".format(co))

            for i in range(0, len(_views))
                setattr(self, _views[i].lower(), _cviews[i])
        except Exception as e:
            raise ExViewError("compose() failed: {}".format(e))

        return self
