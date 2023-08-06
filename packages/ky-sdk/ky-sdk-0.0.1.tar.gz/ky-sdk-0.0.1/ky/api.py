# coding:utf-8
# @Time    : 2019-12-09
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .order import Order
from .base import Base


class KY(object):

    def __init__(self, appkey, appsecret, sandbox=False):
        self.appkey = appkey
        self.appsecret = appsecret
        self.sandbox = sandbox

    comm = Comm()
    order = Order()
    base = Base()
