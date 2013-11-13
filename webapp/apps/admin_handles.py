import tornado.web
from tornado.log import gen_log

from apps.utils import route


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        pass

    def initialize(self):
        print "please define your initialize..............."


@route(r"/admin/login", name="login")
class LoginHandler(BaseHandler):

    def get(self):
        #redirect to login url
        gen_log.info("hello %s" % "Yan")
        self.write("Login html")

    def post(self):
        pass


@route(r"/admin/logout", name="logout")
class LogoutHandler(BaseHandler):

    def get(self):
        pass


@route(r"/admin", name="admin")
class AdminHandler(BaseHandler):

    def get(self):
        self.render("admin.html")


@route(r"/admin/insu/(.*)", name="insurance")
class InsuranceHandler(BaseHandler):

    query_sql = """SELECT i.id,i.pro_name,i.age_min,i.age_max, i.insu_days, i.tags,i.description,
                          c.id as clause_limit_id, c.insu_id, c.clause_name, c.limits
                      FROM insurance i, clause_limit c
                     WHERE i.id = c.insu_id
                """

    def get(self, action):
        result = self.db.query(self.query_sql)
        result_dict = {"result:": result}
        self.write(result_dict)

    def post(self):
        # insu_id = self.get_argument("pro_id", None)
        pro_name = self.get_argument("pro_name", None)
        age_min = self.get_argument("age_min", None)
        age_max = self.get_argument("age_max")
        insu_days = self.get_argument("insu_days")
        description = self.get_argument("description")
        tags = self.get_argument("tags")
        INSERT_ID = self.db.execute("INSERT INTO insurance (pro_name, age_min, age_max, category,"
                                    "insu_days,claus_limit_id,tags,price,description)"
                                    "VALUES (%s, %s, %s, NULL, %s, NULL, %s, 0, %s)",
                                    pro_name, age_min, age_max, insu_days, tags, description)
        # INSERT_ID = self.db.query("SELECT LAST_INSERT_ID() as insert_id")
        if not INSERT_ID:
            raise tornado.web.HTTPError(500, "Failed")

        clause_limit = self.get_argument("clause_limit", None)

        def cancat_tuple(last_id, cl):
            _clause, _limit = cl.split(":")
            return last_id, _clause, _limit

        if clause_limit:
            _cl = set(clause_limit.split(","))
            clauses = [cancat_tuple(int(INSERT_ID), c) for c in _cl]
            print clauses
            self.db.executemany("INSERT INTO clause_limit(insu_id, clause_name,"
                                " limits) VALUES(%s, %s, %s)", clauses)
        else:
            tornado.web.HTTPError(500, "Bad Parameter of form")
        self.redirect("/insurance?action=list")
