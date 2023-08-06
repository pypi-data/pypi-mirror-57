"""
The ExSql view performs SQL queries directly against the
database. It can be used to perform high performance reads
or writes that are otherwise not allowed by Sage's validation
(caveat emptor).
"""
from contextlib import contextmanager

from . import ExView

@contextmanager
def exsql_result(query):
    """Open an ``ExSql`` view, executes a query, and yield the results.

    :param query: SQL query to execute.
    :type query: str
    :yields: ExSql
    :rtype: None
    :raises: ExSqlError, ExViewError

    .. code-block:: python

        query = ("SELECT ITEM FROM OEORDD WHERE "
                 "ORDUNIQ = {} AND LINENUM = {}".format(
                        234634, 2))
        try:
            with exsql_result(query) as res:
                item = res.get("ITEM")
        except ExSqlError as e:
            # Handle an SQL fail
        except ExViewError as e:
            # Handle a view layer fail
    """

    exs = ExSql()
    try:
        exs.query(query)
        yield exs
    except:
        exs.close()
        raise

@contextmanager
def exsql():
    """Open an ``ExSql`` view and yield it.

    :yields: ExSql
    :rtype: None
    :raises: ExSqlError, ExViewError

    .. code-block:: python

        try:
            with exsql() as exs:
                exs.query("SELECT ITEM FROM OEORDD WHERE "
                          "ORDUNIQ = {} AND LINENUM = {}".format(
                                234634, 2))
                item = exs.get("ITEM")
        except ExSqlError as e:
            # Handle an SQL fail
        except ExViewError as e:
            # Handle a view layer fail
    """
    exs = ExSql()
    try:
        exs.query(query)
        yield exs
    except:
        exs.close()
        raise

class ExSql(ExView):

    CSQL_VIEWID = "CS0120"

    def __init__(self):
        super().__init__(self.CSQL_VIEWID)

    def query(self, query):
        """Perform an SQL query and return the view.

        :param query: an SQL query to execute.
        :type query: str
        :returns: view with the first result fetched.
        :rtype: ExView
        :raises: ExSqlError, ExViewError

        If you only need to execute a query, consider using a
        context manager like :py:meth:`extools.exview.exsql.exsql` or
        :py:meth:`extools.exview.exsql.exsql_result`.

        .. code-block:: python

            try:
                exs = ExSql()
                result = exs.query("SELECT ITEM FROM OEORDD WHERE "
                                   "ORDUNIQ = {} AND LINENUM = {}".format(
                                        234634, 2))
                item = result.get("ITEM")
            except ExSqlError as e:
                # Handle an SQL fail
            except ExViewError as e:
                # Handle a view layer fail
        """

        self.recordClear()
        self.browse(query)
        self.fetch()

