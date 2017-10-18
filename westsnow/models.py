"""
  models
  ~~~~~~

  项目数据库表结构处理。

"""
from datetime import datetime

from peewee import (MySQLDatabase, Model, CharField, IntegerField,
                    DateTimeField, BooleanField, ForeignKeyField, TextField)
from playhouse.shortcuts import RetryOperationalError
from tornado.options import options

from .config import define_options


class MyRetryDB(RetryOperationalError, MySQLDatabase):
    pass


define_options()
db = MyRetryDB(options.mysql_db, **{'port': options.mysql_port,
                                    'password': options.mysql_password,
                                    'user': options.mysql_user,
                                    'host': options.mysql_host})


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = db


class ShopBulkData(BaseModel):
    data = TextField()
    converted_data = TextField()
    created = DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'shop_bulk_data'



FieldsMap = {
    'ShopBulkData': ShopBulkData._meta.sorted_field_names,
}


if __name__ == '__main__':
    db.connect()
    db.create_tables([ShopBulkData])
