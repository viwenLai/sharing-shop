"""
  handler
  ~~~~~~~

  相关 handlers

"""
import json
import random
import logging

from raven.contrib.tornado import SentryMixin
from tornado.web import RequestHandler
from mwtk_utils import tornado_handy_utils as thu
from mwtk_utils import obj_json_dumps, to_str

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
        obj = ShopBulkData.select().order_by(ShopBulkData.id.desc()).get()
        self.write(obj.converted_data)


class ShopDataUpdateHandler(BaseReqHandler):
    file_field_name = 'shops.data'

    def post(self):
        # 处理数据
        logging.info(self.request.files)
        if self.file_field_name != self.request.files['file'][0]['filename']:
            thu.fin_400_bad_request(self, 'file field not exist.')
            return
        file_body = self.request.files['file'][0]['body']
        file_body = to_str(file_body)
        data = self.convert_data(file_body)

        # 入库处理
        ShopBulkData.create(data=file_body, converted_data=json.dumps(data))
        rv = {
            'result': 'ok'
        }
        self.write(rv)

    def convert_data(self, data):
        """ 将文件数据转为结构化数据。"""
        rv = {}
        for line in data.split('\n'):
            parts = [part.strip() for part in line.split('|')]
            code, klass, name, url = parts
            if klass not in rv:
                rv[klass] = []
            _t = {
                'code': code,
                'name': name,
                'url': url
            }
            rv[klass].append(_t)
        return rv
