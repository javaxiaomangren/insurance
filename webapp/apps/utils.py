import tornado.web


class route(object):
    """
    decorates RequestHandlers and builds up a list of routables handlers

    Tech Notes (or 'What the *@# is really happening here?')
    --------------------------------------------------------

    Everytime @route('...') is called, we instantiate a new route object which
    saves off the passed in URI.  Then, since it's a decorator, the function is
    passed to the route.__call__ method as an argument.  We save a reference to
    that handler with our uri in our class level routes list then return that
    class to be instantiated as normal.

    Later, we can call the classmethod route.get_routes to return that list of
    tuples which can be handed directly to the tornado.web.Application
    instantiation.

    Example
    -------

    @route('/some/path')
    class SomeRequestHandler(RequestHandler):
        pass

    @route('/some/path', name='other')
    class SomeOtherRequestHandler(RequestHandler):
        pass

    my_routes = route.get_routes()

    In your Application:
    Application = Application(my_routes, **settings)
    """
    _routes = []

    def __init__(self, uri, name=None):
        self._uri = uri
        self.name = name

    def __call__(self, _handler):
        """gets called when we class decorate"""
        name = self.name and self.name or _handler.__name__
        self._routes.append(tornado.web.url(self._uri, _handler, name=name))
        return _handler

    @classmethod
    def get_routes(cls):
        return cls._routes


def route_redirect(from_, to, name=None):
    route._routes.append(tornado.web.url(from_, tornado.web.RedirectHandler, dict(url=to), name=name))


class Transaction(object):
    """
        处理事务集合
        db: mysql db connection
        Usage:
        with Transaction(db) as trans_db:
            trans_db.execute(sql)
            trans_db.commit()
    """
    def __enter__(self, db):
        """set up tings and return things"""
        self.tran_db = db 
        self.tran_db.autocommit(False)
        return self.tran_db

    def __exit__(self):
        """tear down thins"""
        self.tran_db.autocommit(True)