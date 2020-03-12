# -*- coding: utf-8 -*-
import logging
import json

# if you open the initializer feature, please implement the initializer function, as below:
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')

# 阿里云API网关与函数计算调用模板
# 重定向功能
# aliapigateway.chaochaogege.com/redirect

def handler(event, context):
#   logger = logging.getLogger()
#   logger.info(event)
#   logger.info(context)
    e = json.loads(event.decode("utf-8"))
    query = e["queryParameters"]
    redirect = ""
    code = 404
    headers = {
    }
    if "redirect" in query:
        redirect = query["redirect"]
        code = 302
        headers["location"] = redirect

    return {
        "isBase64Encoded":False,
        "statusCode":code,
        "headers":headers,
        "body":""
    }

# event结构
# {
#     "path":"api request path",
#     "httpMethod":"request method name",
#     "headers":{all headers,including system headers},
#     "queryParameters":{query parameters},
#     "pathParameters":{path parameters},
#     "body":"string of request payload",
#     "isBase64Encoded":"true|false, indicate if the body is Base64-encode"
# }

# context存放ali相关的信息
# https://help.aliyun.com/document_detail/74756.html?spm=a2c4g.11174283.6.565.5b565212jrvRvY#general-handler-interface