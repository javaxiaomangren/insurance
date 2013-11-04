#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import markdown
import os.path
import re
import torndb
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="insurance database host")
define("mysql_database", default="insurance", help="insurance database name")
define("mysql_user", default="root", help="insurance database user")
define("mysql_password", default="", help="insurance database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/insurance", InsuranceHandler),
            (r"/", HomeHandler),
            # (r"/archive", ArchiveHandler),
            # (r"/feed", FeedHandler),
            # (r"/entry/([^/]+)", EntryHandler),
            # (r"/compose", ComposeHandler),
            # (r"/auth/login", AuthLoginHandler),
            # (r"/auth/logout", AuthLogoutHandler),
        ]
        settings = dict(
            site_title=u"Insurance search",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Entry": EntryModule},
            # xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("blogdemo_user")
        if not user_id: return None
        return self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))

    def initialize(self):
        print "helllo"

class HomeHandler(BaseHandler):
    def get(self):
        self.render("base.html")

class InsuranceHandler(BaseHandler):
    def get(self):
        result = self.db.query("""SELECT i.id,i.pro_name,i.age_min,i.age_max, i.insu_days, i.tags,
                              i.description,c.id as clause_limit_id, c.insu_id, c.clause_name, c.limits 
                           FROM insurance i, clause_limit c 
                           WHERE i.id = c.insu_id 
                    """)
        result_dict = {"result:":result}
        # for e in result:
        #     exist = result_dict.get(e.get("id"))
        #     if exist:
        #         result_dict.get("clause_limits"+str(exist)).append({e.get("clause_limit_id"):[e.get("clause_name"),  e.get("limits")]})
        #     else:
        #         result_dict[e.get("id")] = e.get("id")
        #         result_dict['pro_name'] = e.get("pro_name")
        #         result_dict['age_min'] = e.get("age_min")
        #         result_dict['age_max'] = e.get("age_max")
        #         result_dict['insu_days'] = e.get("insu_days")
        #         result_dict['tags'] = e.get("tags")
        #         result_dict['description'] = e.get("description")
        #         result_dict["clause_limits"+str(e.get("id"))] = [{e.get("clause_limit_id"):[e.get("clause_name"),  e.get("limits")]}]
        #         # result_dict["clause_limits"] = result_dict.get("clause_limits").append({e.get("clause_limit_id"):[e.get("clause_name",  e.get("limits"))]})
        self.write(result_dict)


    def post(self):
        insu_id = self.get_argument("pro_id", None)
        pro_name = self.get_argument("pro_name", None)
        age_min = self.get_argument("age_min", None)
        age_max = self.get_argument("age_max")
        print  pro_name, age_min, age_max
        insu_days = self.get_argument("insu_days")
        description = self.get_argument("description")
        tags = self.get_argument("tags")
        INSERT_ID = self.db.execute("INSERT INTO insurance (pro_name, age_min, age_max, category,"
                        "insu_days,claus_limit_id,tags,price,description)" 
                        "VALUES (%s, %s, %s, NULL, %s, NULL, %s, 0, %s)", 
                        pro_name, age_min, age_max, insu_days, tags, description)
        # INSERT_ID = self.db.query("SELECT LAST_INSERT_ID() as insert_id")
        if not  INSERT_ID:
            raise  tornado.web.HTTPError(500, "Failed")

        clause_limit = self.get_argument("clause_limit", None)
        def cancat_tuple(last_id, cl):
            _clause, _limit = cl.split(":")
            return (last_id, _clause, _limit)

        if (clause_limit):
            _cl = set(clause_limit.split(","))
            clauses = [cancat_tuple(int(INSERT_ID), c) for c in _cl]
            print clauses
            self.db.executemany("INSERT INTO clause_limit(insu_id, clause_name,"
                                " limits) VALUES(%s, %s, %s)", clauses)
        else:
            tornado.web.HTTPError(500, "Bad Parameter of form")
        self.redirect("/insurance?action=list")

class EntryHandler(BaseHandler):
    def get(self, slug):
        entry = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
        if not entry: raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)


class ArchiveHandler(BaseHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM entries ORDER BY published "
                                "DESC")
        self.render("archive.html", entries=entries)


class FeedHandler(BaseHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM entries ORDER BY published "
                                "DESC LIMIT 10")
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", entries=entries)


class ComposeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_argument("id", None)
        entry = None
        if id:
            entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
        self.render("compose.html", entry=entry)

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        text = self.get_argument("markdown")
        html = markdown.markdown(text)
        if id:
            entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(id))
            if not entry: raise tornado.web.HTTPError(404)
            slug = entry.slug
            self.db.execute(
                "UPDATE entries SET title = %s, markdown = %s, html = %s "
                "WHERE id = %s", title, text, html, int(id))
        else:
            slug = unicodedata.normalize("NFKD", title).encode(
                "ascii", "ignore")
            slug = re.sub(r"[^\w]+", " ", slug)
            slug = "-".join(slug.lower().strip().split())
            if not slug: slug = "entry"
            while True:
                e = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
                if not e: break
                slug += "-2"
            self.db.execute(
                "INSERT INTO entries (author_id,title,slug,markdown,html,"
                "published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",
                self.current_user.id, title, slug, text, html)
        self.redirect("/entry/" + slug)


class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        author = self.db.get("SELECT * FROM authors WHERE email = %s",
                             user["email"])
        if not author:
            # Auto-create first author
            any_author = self.db.get("SELECT * FROM authors LIMIT 1")
            if not any_author:
                author_id = self.db.execute(
                    "INSERT INTO authors (email,name) VALUES (%s,%s)",
                    user["email"], user["name"])
            else:
                self.redirect("/")
                return
        else:
            author_id = author["id"]
        self.set_secure_cookie("blogdemo_user", str(author_id))
        self.redirect(self.get_argument("next", "/"))


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("blogdemo_user")
        self.redirect(self.get_argument("next", "/"))


class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()