# coding:utf-8
# @Time    : 2019-12-12
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm


class Base(Comm):

    def get_express_time(self, commonDistrID=None):
        """
        时效查询
        """
        method = "open.api.openCommon.queryTimeliness"
        pass

    def get_address(self, distrctId=None):
        """五级地址多级联动查询(V1.0)"""

        method = "open.api.openCommon.queryKyeAddress"
        data = {
            "commonDistrID": distrctId
        }
        return self.post(method, data=data).json()

    def is_cross_district(self, adresses, company_no=None):
        """根据收件地址判断是否在派送区域内"""
        method = "open.api.openCommon.queryOverZoneInfo"
        data = {
            "companyNo": company_no,
            "addressData": adresses
        }
        return self.post(method, data).json()

    def get_route_info(self, express_nos=None, codes=None):
        """查询路由信息"""
        method = "open.api.openCommon.queryPublicRoute"
        data = {
            "waybillNumbers": express_nos,
            "productCodes": codes,
        }
        return self.post(method, data).json()
