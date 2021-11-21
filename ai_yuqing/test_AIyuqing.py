import pytest

from ai_yuqing.api_corp_tag_AI import YuQing


class TestCorpTap:
    def setup_class(self):
        self.yuqing = YuQing()

    # @pytest.mark.parametrize()
    def test_get_corp_tag_list(self):
        r = self.yuqing.news()
        print(r.json())
        assert r.status_code == 200
        assert r.json().get("ok") == True

    def test_get_pure_index(self):
        r = self.yuqing.pure_index()
        assert r.status_code == 200
        assert r.json().get("ok") == True

    def test_get_delete(self):
        s = self.yuqing.create()
        id = s.json().get("id")
        r = self.yuqing.delete(id)
        assert r.status_code == 200

    def test_get_create(self):
        r = self.yuqing.create()
        assert r.status_code == 300
