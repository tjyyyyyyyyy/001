from ai_yuqing.base_api_AI import BaseApi001


class YuQing(BaseApi001):

    def news(self):
        data = {
            "method": "post",
            "url": 'http://123.56.138.96:3012/api/ainews-espy/api/news/news-list-industry',
            "json": {
                "industry": "all", "start_time": "2021-10-31", "end_time": "2021-11-14",
                "page": 1,
                "page_size": 10,
                "sort_order": "desc"
            },
            "headers":
                {
                    "Content-Type": "application/json;charset=UTF-8",
                    "Authorization": self.wework
                }
        }
        return self.send(data)

    def pure_index(self):
        data = {
            "method": "post",
            "url": 'http://123.56.138.96:3012/api/ainews-espy/api/opinion/company-article-list',
            "json": {"cp_code": ["600466"], "sort_by": "default", "sort_order": "desc", "start_time": "2021-11-01",
                     "end_time": "2021-11-15", "page": 1, "risk_level": [0, 1, 2], "article_type": "all",
                     "matter": "all"},
            "headers":
                {
                    "Content-Type": "application/json;charset=UTF-8",
                    "Authorization": self.wework
                }
        }
        return self.send(data)

    def create(self):
        data = {
            "method": "post",
            "url": 'http://123.56.138.96:3012/api/ainews-user/company-group/create',
            "headers": {
                "Content-Type": "application/json;charset=UTF-8",
                "Authorization": self.wework
            },
            "json": {"name": "tjy"}
        }
        # print(YuQing().create().get("name"))
        return self.send(data)

    def delete(self, id):
        data = {
            "method": "get",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/delete",
            "headers": {
                "Content-Type": "application/json;charset=UTF-8",
                "Authorization": self.wework

            },
            "params": {"id": id}
        }
        # print("parmas")
        return self.send(data)


if __name__ == '__main__':
    print(YuQing().news())
    # print(YuQing().pure_index())
    # print(YuQing().create())
    # print(YuQing().delete(YuQing().create().json().get("id")))
