# coding:utf-8
# @Time    : 2019-12-09
# @Author  : Kevin Kong (kfx2007@163.com)

import requests
import time
from hashlib import md5
import json

TOKEN_URL = "https://open.ky-express.com/security/token"
SANDBOX_TOKEN_URL = "https://open.ky-express.com/security/sandbox/accessToken"
REFESH_URL = "https://open.ky-express.com/security/token/refresh"
API_URL = "https://open.ky-express.com/router/rest"
SANDBOX_URL = "https://open.ky-express.com/sandbox/router/rest"


class Comm(object):

    def __get__(self, instance, type):
        self.appkey = instance.appkey
        self.appsecret = instance.appsecret
        self.sandbox = instance.sandbox
        return self

    def _get_token(self):
        """获取TOKEN"""
        headers = {"Content-Type": "application/json", "X-from": "openapi_app"}
        url = SANDBOX_TOKEN_URL if self.sandbox else TOKEN_URL
        res = requests.post(url, json={
            "appkey": self.appkey,
            "appsecret": self.appsecret
        }, headers=headers).json()
        if res["success"]:
            return res["data"]["token"], res["data"]["refresh_token"]

    def _refresh_token(self, refresh_token):
        """刷新token"""
        headers = {"Content-Type": "application/json", "X-from": "openapi_app"}
        res = requests.post(REFESH_URL, json={
            "refresh_token": refresh_token
        }, headers=headers).json()
        if res["success"]:
            return res["data"]["refresh_token"]

    def _get_request_header(self, timestamp):
        token, _ = self._get_token()
        return {
            "X-from": "openapi_app",
            "Content-Type": "application/json",
            "token": token,
            "appkey": self.appkey,
            "timestamp": timestamp,
            "format": "json"
        }

    def _sign(self, params, timestamp):
        return md5("{}{}{}".format(self.appsecret, timestamp, params).encode('utf-8')).hexdigest().upper()

    def post(self, method, data=None):
        # 这里吐槽一下跨越官方 不仅没有Python版的SDK，即使是Java和Net，居然也只是放了个DLL进去，源码都不带给的。。
        timestamp = str(int(round(time.time()*1000)))
        headers = self._get_request_header(timestamp)
        # 去除空值
        data = {key: val for key, val in data.items() if val}
        sign = self._sign(json.dumps(data), timestamp)
        headers['method'] = method
        headers['sign'] = sign
        url = SANDBOX_URL if self.sandbox else API_URL
        return requests.post(url, json=data, headers=headers)
