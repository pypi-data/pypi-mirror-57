# coding:utf-8
# @Time    : 2019-12-12
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm


class Order(Comm):

    def get_express_number(self, count=1):
        """
        获取运单号接口

        param count: 运单号个数
        """
        method = "open.api.openCommon.queryWaybillNumber"
        return self.post(method, {'count': count}).json()
