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
        entry = {
        "id": 1,
        "proName": "“车路有我”交通意外垫付保障计划",
        "maxAge": 6570,
        "minAge": 29200,
        "description": "保障全面，既保障车主司机的人身意外和医疗保障，还包括陪同乘客的保障。适合自驾车人或司机人群。",
        "notice": "1、本保险产品每一被保险人限投保贰份，多投无效。\n2、本产品生效日期为投保次日起第六日零时开始。\n3、本产品一般意外事故保障和特定意外事故特约赔付保障不能累加重复赔付。\n4、本产品为保险激活卡，您在本网站购买此产品则视为同意授权慧择网代为激活。本保险不办理变更、撤保、退保和加保。\n5、按保监会规定，未满十八周岁的未成年人以身故为给付责任的保险金不得超过10万（航空意外除外）。\n6、主被保险人发生保险事故可通过拨打全国24小时医疗救援电话：400 6506 119，可在全国914家网络医院启用意外住院押金垫付功能（意外门诊无垫付功能），享用专业授权医生现场电话急救指导、协助报案、联系被保险人家属、安排急救车辆、提供就近医院信息、网络医院入院安排等增值服务。\n7、本投保人已阅读相关条款，并特别就条款中有关责任免除和投保人、被保险人义务的内容进行阅读。本投保人特此同意接受条款全部内容，确认对其中各项内容尤其是投保条件、保险责任条款、免责条款、合同解除条款均完全理解并同意遵守。\n",
        "suitable": "有车一族、商务人士、司机。",
        "example": "example.pdf",
        "price": 100,
        "salesVolume": 10,
        "buyCount": 1,
        "validFlag": 1,
        "clauseName": [
          "意外事故",
          "意外事故医疗",
          "意外三度烧烫",
          "航空意外事故身故",
          "公共交通工具意外身故",
          "自驾车交通意外事故",
          "自驾车交通意外医疗",
          "自驾车时车上乘客意外"
        ],
        "limits": [
          5000,
          300000,
          120000,
          10000,
          50000,
          60000
        ],
        "insuDays": [
          365
        ],
        "companyId": 4,
        "companyName": "平安人寿",
        "companyLogo": "20120215095300.gif",
        "categoryId": 4,
        "categoryName": "交通意外",
        "imgUrl": [
          ""
        ],
        "tagId": [
          1,
          2,
          3,
          4,
          5,
          7
        ],
        "tagName": [
          "高额第三者责任",
          "随身财物损失",
          "超高医疗",
          "全面医疗",
          "高尔夫一杆进洞",
          "电子保单"
        ],
        "_version_": 1452122976098975700
        }
        self.render("index.html", entries=[ObjectDict(entry)])

    def post(self):
        #should decode
        args = self.request.arguments
        param = []
        for arg in args:
            if arg == "ageCover":
                continue
            ls = args[arg]
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
            "sort": "id asc"
        })
        # results = sorted(results, key=lambda y: y.get('id'))
        # entries = [ObjectDict(row) for row in results]
        # print entries
        # # self.render("table.html", entries=entries)
        # self.write({"results":[r for r in results]})
        self.render("index.html", entries=[ObjectDict(r) for r in results])

@route("/entry")
class InsuranceHandle(BaseHandler):

    def get(self):
        aaa = {
        "id": 1,
        "proName": "“车路有我”交通意外垫付保障计划",
        "maxAge": 6570,
        "minAge": 29200,
        "description": "保障全面，既保障车主司机的人身意外和医疗保障，还包括陪同乘客的保障。适合自驾车人或司机人群。",
        "notice": "1、本保险产品每一被保险人限投保贰份，多投无效。\n2、本产品生效日期为投保次日起第六日零时开始。\n3、本产品一般意外事故保障和特定意外事故特约赔付保障不能累加重复赔付。\n4、本产品为保险激活卡，您在本网站购买此产品则视为同意授权慧择网代为激活。本保险不办理变更、撤保、退保和加保。\n5、按保监会规定，未满十八周岁的未成年人以身故为给付责任的保险金不得超过10万（航空意外除外）。\n6、主被保险人发生保险事故可通过拨打全国24小时医疗救援电话：400 6506 119，可在全国914家网络医院启用意外住院押金垫付功能（意外门诊无垫付功能），享用专业授权医生现场电话急救指导、协助报案、联系被保险人家属、安排急救车辆、提供就近医院信息、网络医院入院安排等增值服务。\n7、本投保人已阅读相关条款，并特别就条款中有关责任免除和投保人、被保险人义务的内容进行阅读。本投保人特此同意接受条款全部内容，确认对其中各项内容尤其是投保条件、保险责任条款、免责条款、合同解除条款均完全理解并同意遵守。\n",
        "suitable": "有车一族、商务人士、司机。",
        "example": "example.pdf",
        "price": 100,
        "salesVolume": 10,
        "buyCount": 1,
        "validFlag": 1,
        "clauseName": [
          "意外事故",
          "意外事故医疗",
          "意外三度烧烫",
          "航空意外事故身故",
          "公共交通工具意外身故",
          "自驾车交通意外事故",
          "自驾车交通意外医疗",
          "自驾车时车上乘客意外"
        ],
        "limits": [
          5000,
          300000,
          120000,
          10000,
          50000,
          60000
        ],
        "insuDays": [
          365
        ],
        "companyId": 4,
        "companyName": "平安人寿",
        "companyLogo": "20120215095300.gif",
        "categoryId": 4,
        "categoryName": "交通意外",
        "imgUrl": [
          ""
        ],
        "tagId": [
          1,
          2,
          3,
          4,
          5,
          7
        ],
        "tagName": [
          "高额第三者责任",
          "随身财物损失",
          "超高医疗",
          "全面医疗",
          "高尔夫一杆进洞",
          "电子保单"
        ],
        "_version_": 1452122976098975700
        }
        dic = ObjectDict(aaa)
        self.render("insurance_entry.html", entry=dic)


class InsuranceEntry(tornado.web.UIModule):
    """docstring for InsuranceEntry"""
    def render(self, entry, show_comments=False):
        self.render_string("modules/insurance-entry.html", entry=entry, show_comments=show_comments)