import json

import requests


class BaseApi001:
    def __init__(self):
        self.wework = self.gettoken()

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=1, ensure_ascii=False))
        return r

    def gettoken(self):
        # todo:获取 access_token
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/user/login",
            "json": {"name": "lsj1", "password": "123123"},
            "headers":
                {
                 "Content-Type": "application/json;charset=UTF-8",
                }
        }
        token = self.send(data).json()['access_token']
        return token


if __name__ == '__main__':
    r = BaseApi001()
    print(r.gettoken())
