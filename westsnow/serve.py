"""
  server
  ~~~~~~

  web main module

"""
import logging

from raven.contrib.tornado import AsyncSentryClient
from tornado.options import options
from tornado import web, ioloop

# must be first import models module for setup the config module.
from .models import db
from .handler import ShopRecordHandler, ShopDataUpdateHandler


def make_app():
    debug = True if options.debug != 'false' else False
    urlmap = [
        (r"/api/v1/sharing-shops/?", ShopRecordHandler),
        (r"/api/v1/sharing-shops/backend/data/update/?", ShopDataUpdateHandler),
    ]

    app = web.Application(urlmap, debug=debug)
    app.db = db
    app.db.connect()
    app.sentry_client = AsyncSentryClient(options.dsn)
    return app


def runserver():
    app = make_app()

    logging.debug("test test")

    logging.info("")
    logging.info("----------------------------------------------")
    logging.info("- Server Listening to - %s...", options.port)
    logging.info("- Server Debug - %s...", options.debug)
    logging.info("- Sentry DSN - %s...", options.dsn)
    logging.info("----------------------------------------------")
    logging.info("- MySQL Host: %s", options.mysql_host)
    logging.info("- MySQL Port: %s", options.mysql_port)
    logging.info("- MysQL DataBase: %s", options.mysql_db)
    logging.info("- MysQL User: %s", options.mysql_user)
    logging.info("- MysQL Password: ****")
    logging.info("----------------------------------------------")
    logging.info("- Author: Kolast Co.,Limited")
    logging.info("- Email: support@kolast.com")
    logging.info("----------------------------------------------")
    logging.info("")

    app.listen(options.port)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    runserver()
