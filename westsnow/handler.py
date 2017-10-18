"""
  handler
  ~~~~~~~

  相关 handlers

"""
import random
import logging

from raven.contrib.tornado import SentryMixin
from tornado.web import RequestHandler
from mwtk_utils import tornado_handy_utils as thu
from mwtk_utils import obj_json_dumps

from .models import FieldsMap, ShopBulkData


__all__ = ['ShopRecordHandler', 'ShopDataUpdateHandler']


class BaseReqHandler(SentryMixin, RequestHandler):

    def options(self, *args, **kwargs):
        """ 为了处理跨域请求问题，统一加入 patch 处理逻辑"""
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT,DELETE")
        self.set_header("Access-Control-Allow-Headers", "authorization, x-user-auth, Content-Type")


class ShopRecordHandler(BaseReqHandler):

    def get(self):
        pass


@auth.apiauth
class ShopDataUpdateHandler(BaseReqHandler):
    def post(self, domain, record, type):
        pass
