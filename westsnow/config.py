"""
  config
  ~~~~~~

  配置相关处理。
"""
from tornado.options import define, parse_command_line


def define_options():
    define('port', default=3378, help='run on the given port', type=int)
    define('debug', default='false', help='debug or not', type=str)
    define("mysql_host", default="127.0.0.1", help="Mysql host specify")
    define("mysql_port", default=3306, help="Mysql port specify", type=int)
    define("mysql_db", default="eshop", help="Mysql DB name")
    define("mysql_user", default="root", help="Mysql user specify")
    define("mysql_password", default="", help="Mysql user password")
    define("dsn", help="Sentry DSN specify",
           default="https://9a5b8779590f483a9b517c56d38d3d2b:88bc68aea40d4263862c27dfa7b03989@sentry.io/231690")
    parse_command_line()
