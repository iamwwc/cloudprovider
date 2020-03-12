# -*- coding: utf-8 -*-
import logging
import json
import requests
import re


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
    regexp = re.compile("1drv\\.ms/(.)/.+!(.+)")

    query = e["queryParameters"]
    downloadurl = ""
    code = 404
    headers = {
    }
    if "downloadurl" in query:
        downloadurl = query["downloadurl"]
        result = regexp.findall(downloadurl)
        if len(result) != 0:
            code = 302
            headers["location"] = get_direct_url(result[0][0], result[0][1])

    return {
        "isBase64Encoded": False,
        "statusCode": code,
        "headers": headers,
        "body": ""
    }


def get_direct_url(ch, share_token):
    url_step1 = 'https://1drv.ms/{ch}/s!{share_token}'.format(
        ch=ch,  # the ch could be w u t or more
        share_token=share_token
    )
    resp_step1 = requests.get(url_step1, timeout=10, allow_redirects=False)
    url_step2 = resp_step1.headers['Location']
    url_step3 = url_step2.replace('/redir?', '/download?')
    resp_step3 = requests.get(url_step3, timeout=10, allow_redirects=False)
    url_final = resp_step3.headers['Location']

    return url_final

if __name__ == '__main__':
    event = b'{"queryParameters":{"downloadurl":"https://1drv.ms/v/s!Aj2hkAf7BSizzH6FeOnKEFxmM4Zu?e=DXW90a"}}'
    handler(event,None)

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
