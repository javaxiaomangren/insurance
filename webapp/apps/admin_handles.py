#coding: utf-8
import datetime
import time
import uuid
import os
import httplib
import traceback

from collections import namedtuple
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

    def get_error_html(self, status_code, **kwargs):

        try:
            template = "admin/404.html"
            message = httplib.responses[status_code]
            exception = "%s\n\n%s" % (kwargs["exception"], traceback.format_exc())
            return self.render_string(template,
                                      code=status_code,
                                      message=message,
                                      exception=exception)
        except Exception:
            return self.write("Server error")

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
        self.redirect("/admin/insurance/")

Insurance = namedtuple("Insurance",
                       "id pro_name company_id category_id notice min_age max_age"
                       "description example price sales_volume buy_count suitable tags")


@route(r"/admin/insurance/(.*)$", name="insurance")
class InsuranceHandler(BaseHandler):
    """
        产品信息维护
    """
    def get(self, action):
        if not action:
            category = self.db.query(sqls.QR_SIMPLE_CATEGORY)
            company = self.db.query(sqls.QR_SIMPLE_COMPANY)
            tags = self.db.query(sqls.QR_TAGS)
            self.render("admin/home.html", categories=category, companies=company, tags=tags)
        if "list" == action:
            entries = self.db.query("SELECT * FROM insurance")
            self.render("admin/list_insurance.html", entries=entries)
        raise tornado.web.HTTPError(400)

    def post(self, action):
        args = self.get_argument
        _id = args("id", None)
        expire = args("expire", "2200-01-01 00:00:00")

        if _id:
            #do update
            pass
        self.db.execute(sqls.INST_INSURANCE,
                        args("proName"), args("companyId"), args("categoryId"), args("notice", u''),
                        args("minAge", 1), args("maxAge", 0), args("description", u''), args("example", u''),
                        args("price", 0), args("salesVolume", 0), args("buyCount", 1), args("suitable", u''),
                        ",".join(args("tags", u'')), expire)
        self.redirect("list")


@route(r"/admin/clause/(.*)$", name="clause")
class ClauseHandle(BaseHandler):
    """docstring for ClauseHandle"""
    def get(self, action):
        if not action:
            category = self.db.query(sqls.QR_SIMPLE_CATEGORY)
            self.render("admin/add_clause.html", entries=category)
        if "list" == action:
            clauses = self.db.query(sqls.QR_CLAUSE)
            self.render("admin/list_clause.html", entries=clauses)
        elif "forSelect" == action:
            self.render("admin/select_clause.html")

    def post(self, action):
        args = self.get_argument
        _id = args("clauseId", None)
        name = args("clauseName")
        desc = args("description", u'')
        cate_id = args("categoryId")
        if len(name) < 2 or len(desc) < 2:
            raise tornado.web.HTTPError(500)
        if _id:
            #do update
            pass
        self.db.execute(sqls.INST_CLAUSE, name, desc, cate_id)
        self.redirect("list")


@route("/admin/(\d+)/clause/(edit|del)", name="edit_clause")
class EditClause(BaseHandler):

    def get(self, clauseId, action):
        clause = self.db.query(sqls.QR_CLAUSE)
        if "del" == action and clause:
            self.db.execute("DELETE FROM clause WHERE id = %s ", clauseId)
            self.redirect("/admin/clause/list")
        raise tornado.web.HTTPError(404)


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


@route(r"/admin/company/(.*)$", name="company")
class CompanyHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self, action):
        if not action:
            self.render("admin/add_company.html")
        elif "list" == action:
            entries = self.db.query(sqls.QR_COMPANY)
            self.render("admin/list_company.html", entries=entries)
        elif "forSelect" == action:
            entries = self.db.query(sqls.QR_COMPANY)
            self.render("admin/select-company.html", entries=entries)
        else:
            raise tornado.web.HTTPError(400)

    def post(self, action):
        """TODO:but it's not recommend, because all upload date is load on RAM,
         the best way is use nginx loadup module, but thses complex
        """
        if not "save" == action:
            raise tornado.web.HTTPError(400)
        name = self.get_argument("companyName", u'')
        if len(name) < 2:
            raise tornado.web.HTTPError(500, "company name can not be null")
        logoName = ""
        if self.request.files:
            path = "static/uploads/"
            logoName = saveFile(self.request.files, "logo", path)
        companyId = self.get_argument("companyId", None)
        if companyId:
            #TODO delete old image
            self.write("TODO update")
            # lastId = self.db.execute("UPDATE", *(name, logoName, companyId))
        else:
            self.db.execute(sqls.INST_COMPANY, *(name, logoName))
        self.redirect("/admin/company/list")


@route(r"/admin/(\d+)/company/(edit|del)$", name="edit_company")
class EditCompany(BaseHandler):
    """docstring for ClassName"""
    def get(self, company_id, action):
        company = self.db.query(sqls.QR_COMPANY)
        if not company:
            raise tornado.web.HTTPError(404)
        if "del" == action:
            self.db.execute("DELETE FROM company where id = %s", company_id)
            self.redirect("/admin/company/list")
        if "edit" == action:
            self.render("admin/edit_company.html", entry=company)
        raise tornado.web.HTTPError(400)


@route(r"/admin/category/(.*)$", name="category")
class CategoryHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self, action):
        if not action:
            category = self.db.query(sqls.QR_SIMPLE_CATEGORY)
            self.render("admin/add_category.html", entries=category)
        elif "list" == action:
            category = self.db.query(sqls.QR_CATEGORY)
            self.render("admin/list_category.html", entries=category)
        elif "forSelect" == action:
            category = self.db.query(sqls.QR_CATEGORY)
            self.render("admin/select_category.html", category)
        raise tornado.web.HTTPError(400)

    def post(self, action):
        id = self.get_argument("categoryId", None)
        name = self.get_argument("categoryName")
        desc = self.get_argument("description", u'')
        parent = self.get_argument("parentId", 0)
        if len(name) < 2:
            raise tornado.web.HTTPError(500, "category name can not be null")
        if id:
            pass
        else:
            self.db.execute(sqls.INST_CATEGORY, name, desc, parent)
            self.redirect("/admin/category/list")


@route(r"/admin/(\d+)/category/(edit|del)", name="edit_category")
class CategoryHandle(BaseHandler):
    def get(self, categoryId, action):
        category = self.db.query("SELECT * FROM category WHERE id = %s", categoryId)
        if not category:
            raise tornado.web.HTTPError(404)
        if action and action == "edit":
            pass
        if "del" == action:
            self.db.execute("DELETE FROM category WHERE id = %s", categoryId)
            self.redirect("/admin/category/list")


@route(r"/admin/tags/(.*)$", name="tags")
class TagsHandle(BaseHandler):
    """docstring for ClauseHandle"""

    def get(self, action):
        if not action:
            self.render("admin/add_tags.html")
        elif "list" == action:
            tags = self.db.query(sqls.QR_TAGS)
            self.render("admin/list_tags.html", entries=tags)
        elif "forSelect" == action:
            tags = self.db.query(sqls.QR_CATEGORY)
            self.render("admin/select_tags.html", entries=tags)
        raise tornado.web.HTTPError(400)

    def post(self, action):
        id = self.get_argument("tagsId", None)
        tag_name = self.get_argument("tagsName")
        if len(tag_name) < 2:
            raise tornado.web.HTTPError(500)
        if id:
            #do update
            pass
        self.db.execute(sqls.REPLACE_TAGS, tag_name)
        self.redirect("list")


@route(r"/admin/(\d+)/tags/(edit|del)", name="edit_tags")
class TagsHandle(BaseHandler):
    def get(self, tagId, action):
        tags = self.db.query("SELECT * FROM tags WHERE id = %s", tagId)
        if not tags:
            raise tornado.web.HTTPError(404)
        if action and action == "edit":
            pass
        if "del" == action:
            self.db.execute("DELETE FROM tags WHERE id = %s", tagId)
            self.redirect("/admin/tags/list")


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


@route("/admin/upload", name="upload")
class UploadHandle(BaseHandler):

    def get(self):
        self.render("admin/upload.html")

    def post(self):
        fileName = saveFile(self.request.files, "uploadName", "static/uploads/")
        self.write(fileName)

@route("/admin/upload/del", name="del_file")
class DelHandle(BaseHandler):

    def get(self):
        file_name = self.get_argument("fileName", None)
        if not file_name:
            raise tornado.web.HTTPError(400)
        del_file(file_name, "static/uploads/")
        self.write(file_name)


def saveFile(files, key, path):
    fl = files[key][0]
    req_name = fl["filename"]
    body = fl["body"]
    timestamp = int(time.time() + 300)
    fileName = "%d_%s.%s" % (timestamp, str(uuid.uuid1()), req_name.split(".").pop())
    gen_log.info(fileName)
    with open(path + fileName, "w") as f:
        f.write(body)
    return fileName


def del_file(file_name, path):
    vpath = os.path.abspath(path + file_name)
    if os.path.isfile(vpath):
        os.remove(vpath)