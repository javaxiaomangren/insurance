#coding: utf-8
import datetime
import tornado.web
from tornado.log import gen_log

from apps.utils import route, nice_bool
import sql_statement as sqls


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        pass

    def initialize(self):
        print "please define your initialize..............."


@route(r"/auth/login", name="login")
class LoginHandler(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self):
        #redirect to login url
        gen_log.info("hello %s" % "Yan")
        self.write("enter username and password")

    def post(self):
        name = self.get_argument("username")
        passwd = self.get_argument("password")
        if name == "a" and passwd == "b":
            # self.redirect(self.reverse_url("admin"))
            self.write("success")
        else:
            self.write("bad username or password")


@route(r"/auth/logout", name="logout")
class LogoutHandler(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self):
        self.write("Login page")


@route(r"/admin", name="admin")
class AdminHandler(BaseHandler):
    def get(self):
        self.render("admin/home.html")


@route(r"/admin/insurance", name="insurance")
class InsuranceHandler(BaseHandler):
    def get(self):
        result = self.db.query(sqls.QR_INSURANCE)
        result_dict = {"result:": result}
        self.write(result_dict)

    #should be aysnc
    def post(self):
        args = self.get_argument
        lastid = self.db.execute(sqls.INST_INSURANCE, *get_insurance_args(args))
        self.write(str(lastid))


@route(r"/admin/test/(.*)$", name="edit_insurance")
class EditInsuranceHandle(BaseHandler):
    def get(self, id):
        print id


def get_insurance_args(args):
    pro_name = args("pro_name")
    min_age = args("min_age", 1)
    max_age = args("max_age", min_age)
    notice = args("notice", u'')
    description = args("description", u'')
    tags = args("tags", u'')
    suitable = args("suitable", u'')
    company_id = args("company_id")
    category_id = args("category_id")
    example = args("example", u'')
    price = args("price", 0)
    sales_volume = args("sales_volume", 0)
    buy_count = args("buy_count", 1)
    update_time = args("update_time", datetime.datetime.now())

    if not (nice_bool(pro_name) and nice_bool(company_id) and nice_bool(category_id)):
        raise tornado.web.HTTPError(500)
    return pro_name, min_age, max_age, notice, description, \
        tags, suitable, company_id, category_id, example, \
        price, sales_volume, buy_count, update_time


@route(r"/admin/clause", name="clause")
class ClauseHandle(BaseHandler):
    """docstring for ClauseHandle"""
    def get(self):
        pass

    def post(self):
        args = self.get_argument
        name = args("clause_name")
        desc = args("description", u'')
        cate_id = args("category_id")
        if not (nice_bool(name) and nice_bool(cate_id)):
            raise tornado.web.HTTPError(500)
        lastid = self.db.execute(sqls.INST_CLAUSE, name, desc, cate_id)
        self.write(str(lastid))


@route(r"/admin/insu_clause", name="insu_clause")
class InsuClauseHandle(BaseHandler):

    def get(self):
        pass

    def post(self):
        args = self.get_argument
        insu_id = args("insu_id")
        clause_id = args("clause_id")
        limits = args("limits", 0)
        insu_days = args("insu_days", 0)
        price = args("price", 0)
        update_time = args("update_time", datetime.datetime.now())
        if not (nice_bool(insu_id) and nice_bool(clause_id)):
            raise tornado.web.HTTPError(500)
        lastid = self.db.execute(sqls.INST_INSU_CLAUSE, insu_id, clause_id, limits, \
                                 insu_days, price, update_time)
        self.write(str(lastid))

@route(r"/admin/company", name="company")
class CompanyHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self):
        company = self.db.query(sqls.QR_COMPANY)
        #TODO RENDER COMPANY
        self.render_string("/admin/company.html", company)

    def post(self):
        name = self.get_argument("company_name")
        logo = self.get_argument("logo", u'')
        if not nice_bool(name):
            raise tornado.web.HTTPError(500, "company name can not be null")
        lastid = self.db.execute(sqls.INST_COMPANY, *(name, logo))
        self.write(str(lastid))


@route(r"/admin/category", name="category")
class CategoryHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self):
        category = self.db.query(sqls.QR_CATEGORY)
        #TODO RENDER CATEGORY
        self.render_string("/admin/category.html", category)

    def post(self):
        name = self.get_argument("category_name")
        desc = self.get_argument("description", u'')
        parent = self.get_argument("parent_id", 0)
        if not nice_bool(name):
            raise tornado.web.HTTPError(500, "category name can not be null")
        lastid = self.db.execute(sqls.INST_CATEGORY, name, desc, parent)
        self.write(str(lastid))


@route(r"/admin/tags/(.*)", name="tags")
class TagsHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self, tag_id):
        print tag_id
        tags = self.db.query(sqls.QR_TAGS)
        #TODO RENDER TAGS

    def post(self, tag_id):
        tag_name = self.get_argument("tag_name")
        if not nice_bool(tag_name):
            raise tornado.web.HTTPError(500)
        lastid = self.db.execute(sqls.INST_TAGS, tag_name)
        self.write(str(lastid))


@route(r"/admin/img", name="image")
class ImageHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self):
        #TODO GET IMAGE
        pass

    def post(self):
        img_name = self.get_argument("img_name")
        img_url = self.get_argument("img_url")
        refered_id = self.get_argument("refered_id")
        type = self.get_argument("type", 0)
        if not (nice_bool(img_name) and nice_bool(img_url) and nice_bool(refered_id)):
            raise tornado.web.HTTPError(500)
        lastid = self.db.execute(sqls.INST_IMAGE, img_name, img_url, refered_id, type)
        self.write(str(lastid))


