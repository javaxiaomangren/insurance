#coding: utf-8
import pysolr
import tornado.web
from tornado.util import ObjectDict

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
        self.render("index.html")

    def post(self):
        #should decode
        args = self.request.arguments
        param = []
        for arg in args:
            if arg == "ageCover":
                continue
            ls = args[arg]
            print arg, ls
            if arg in ["companyId", "clauseName", "tagId"]:
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
            "sort": "id desc"
        })
        # results = sorted(results, key=lambda y: y.get('id'))
        # entries = [ObjectDict(row) for row in results]
        # print entries
        # # self.render("table.html", entries=entries)
        self.write({"results":[r for r in results]})