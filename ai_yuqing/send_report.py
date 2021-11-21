import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://tjy:tjy010801@39.107.125.156:9000/job/tjyyy/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=' \
                    '797722368bdfac79d1529712213055416b3b2a310c8aa471a46c695e5e6807c7'
        self.error = self.get_allure()

    def get_allure(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号tjy,密码tjy010801",
                    "title": "tiamo" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://tjy:tjy010801@39.107.125.156:9000/job/tjyyy/allure"
                }
            }
            requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
