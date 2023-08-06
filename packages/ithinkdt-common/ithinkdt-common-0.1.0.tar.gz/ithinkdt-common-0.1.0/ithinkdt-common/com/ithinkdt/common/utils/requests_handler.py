# -*-coding:utf-8-*-
"""
接口请求类,请求接口，返回所需要的数据
"""

import requests


class RequestHandler:

    @staticmethod
    def get(url, params=None, **kwargs):
        """发送get请求"""
        return requests.get(url, params=params, **kwargs)

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        """发送post请求"""
        return requests.post(url, data=data, json=json, **kwargs)

    def visit(self, method, url, params=None, data=None, json=None, **kwargs):
        """定义访问接口的方法"""
        if method.lower() == 'get':
            return self.get(url, params=params, **kwargs)
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, **kwargs)
        else:
            return requests.request(method, url, params=params, data=data, json=json, **kwargs)

    def json(self, method, url, params=None, data=None, json=None, **kwargs):
        """访问接口，返回json数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kwargs)
        return res.json()


# if __name__ == '__main__':
#     # req = RequestHandler()
#     # method = {'method': 'post'}
#     res = requests.post(url='http://new.srm.qa.ithinkdt.com/api/v1/ithinkdt-srm-scm-new/cer/settlement_price_bill/bill_list.do', params='', headers="{'Content-Type':'application/x-www-form-urlencoded','Authorization':'3f881dbd-2b35-4c37-b961-fa7d8359ad1e'}")
#     print(res)

