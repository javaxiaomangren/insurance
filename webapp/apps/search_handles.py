#coding: utf-8
import pysolr
import tornado.web
from tornado.util import ObjectDict
from tornado.web import access_log

from utils import route


class BaseHandler(tornado.web.RequestHandler):
    @property
    def solr(self):
        #do i need to create a new connection at every request??
        return pysolr.Solr(self.application.solr_path)

    def get_current_user(self):
        pass

    def initialize(self):
        print "please define your initialize..............."


@route(r"/", name="index")
class IndexHandler(BaseHandler):
    def get(self):
        result = self.solr.search("*:*", **{
            "sort": "id asc",
            "start": 0,
            "rows": 20
        })
        self.render("index.html", entries=[ObjectDict(r) for r in result])

    # @tornado.web.asynchronous
    def post(self):
        #should decode
        args = self.request.arguments
        print args
        param = []
        for arg in args:
            if arg == "ageCover":
                continue
            ls = args[arg]
            if arg in ["companyId", "clauseName", "tagId"]:
                print args[arg]
                ors = " OR ".join([arg + ":" + v for v in args[arg] if v])
                if ors:
                    param.append(ors)
            elif ls and ls[0]:
                value = ls[0].split(",")
                if len(value) == 2:
                    param.append("%s: [ %s TO %s]" % (arg, value[0], value[1]))
                else:
                    param.append(arg + ":" + value[0])
        if param:
            query_string = " AND ".join(param)
        else:
            query_string = "*:*"
        results = self.solr.search(query_string, **{
            "sort": "id asc"
        })
        access_log.info("solr_query > %s", query_string)
        self.render("list.html", entries=[ObjectDict(r) for r in results])


class InsuranceEntry(tornado.web.UIModule):
    """docstring for InsuranceEntry"""
    def render(self, entry, show_comments=False):
        return self.render_string("modules/insurance-entry.html", entry=entry, show_comments=show_comments)