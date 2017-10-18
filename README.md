# Westsnow

## 后端 API

### GET /api/v1/sharing-shops - 获取店铺数据
### POST /api/v1/sharing-shops/backend/data/update/ - 推送数据到服务端

## 前端页面

一共是两个，分别提交数据和展示数据，如下，

### 基于 GET /api/v1/sharing-shops API 将数据在页面中展示出来

- 样式：基于提供图片的样子进行页面构建；
- 返回的数据是 json 对象，格式如下，

```py
{
  '衣服代购': [
    {
      'number': 1000,
      'name': '上物东',
      'url': 'http://xxx.xxx.xx'
    },
    {
      'number': 1001,
      'name': '上物西',
      'url': 'http://xxx.xxx.xx'
    }
  ],
  '牛仔裤代购': [
    {
      'number': 1002,
      'name': '上物东',
      'url': 'http://xxx.xxx.xx'
    }
  ],
}
```

### 基于 POST /api/v1/sharing-shops/backend/data/update/ API 让管理员将原始数据提交到后端；

页面样式 - 一个单独的用于上传文件的页面，这个可以自由发挥，找一下已有的模板咯；

POST 请求使用 form 的 file upload 进行参数上传，并需要指定上传的文件名为 ‘shops.data’；

返回参数，
```sh
当处理成功，返回结果为 200 且包括下面数据，

{
  'result': 'ok'
}

当处理成功，则返回结果为非 200
```

## 测试地址

- 地址， http://13.124.164.239:3378
- 对于 GET /sharing-shops API，将会返回测试的构造数据，即每次返回都是一样，具体数据以实际测试为准；
- 对于 POST /sharing-shops/backend/data/update/ API 仅仅是测试，过程不会影响到上面的 GET API；
