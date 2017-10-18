import random
import logging
from unittest import TestCase

import requests
from faker import Faker


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s# %(message)s",
                    datefmt="%Y/%m/%d-%H:%M:%S")


tc = TestCase()
fake = Faker('zh_CN')
ALLCLASS = [
    '复刻与原创银器',
    '购物网站',
    '复刻手工靴',
    '户外用品',
    '长牛仔裤',
    '牛仔裤代购',
    '鞋子代购',
    '奶粉代购',
    '手机代购',
    '电脑代购',
    '国外购物网站',
    '知名论坛',
]
GEN_ITEMS = 222
TEMPFILE = 'temp.data'


def gen_items(num=10):
    rv = []
    base_num = 1000
    for i in range(num):
        code = str(base_num + i)
        klass = random.choice(ALLCLASS)
        title = fake.company_prefix()
        url = fake.url()
        item = '|'.join([code, klass, title, url])
        rv.append(item)
    return '\n'.join(rv)


def write_tmp_file():
    content = gen_items(GEN_ITEMS)
    with open(TEMPFILE, 'w') as f:
        f.write(content)


def ws_api(path):
    uri = 'http://127.0.0.1:3378{}'.format(path)
    return uri


def api_push_file():
    path = "/api/v1/sharing-shops/backend/data/update"
    uri = ws_api(path)
    files = {'file': ('shops.data', open(TEMPFILE, 'rb'))}
    r = requests.post(uri, files=files)
    tc.assertEqual(r.status_code, 200)


def api_fetch_data():
    path = "/api/v1/sharing-shops"
    uri = ws_api(path)
    r = requests.get(uri)
    tc.assertEqual(r.status_code, 200)
    rv = r.json()
    print(rv)


if __name__ == '__main__':
    # print(gen_items(num=200))
    write_tmp_file()
    api_push_file()
    api_fetch_data()
