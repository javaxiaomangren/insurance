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
            if arg == "age_max" or arg == "age_min":
                continue
            ls = args[arg]
            if ls and len(ls) > 0:
                if arg == "clause_limit" and ls[0]:
                    for e in set(ls[0].split(",")):
                        param.append("clause:%s" % e.replace(":", " AND limits:"))
                elif ls[0]:
                    param.append("%s:%s" % (arg, ls[0]))
        if param:
            query_string = " AND ".join(param)
        else:
            query_string = "*:*"
        results = self.solr.search(query_string)
        results = sorted(results, key=lambda y: y.get('id'))
        print dir(ObjectDict)
        # print ObjectDict(zip(results[0].keys, results[0]))
        entries = [ObjectDict(row) for row in sorted(results, key=lambda y: y.get('id'))]
        print entries
        # self.render("table.html", entries=entries)
        # self.write({"results":[r for r in result]})