from cgi import test
import datetime
import jiyukenkyu_app.tests.setup as test_setup
from django.test import TestCase
from jiyukenkyu_app.tests.setup import setUp

class TestModel(TestCase):
    # テストデータの生成
    fixtures = ['jiyukenkyu_app.json']

    def setUp(self):
        setUp()
        
    def test_model_count(self):
        obj_count = test_setup.object_list.count()
        self.assertEqual(obj_count, 22)
        
    def test_model_data(self):
        obj_first = test_setup.object_list.first()
        
        self.assertEqual(obj_first.pk, 1)
        self.assertEqual(obj_first.presenter, 'テスト太郎')
        self.assertEqual(obj_first.theme, 'テスト発表テーマ')
        self.assertEqual(obj_first.category, 4)
        self.assertEqual(obj_first.detail, 'テスト発表についての概要')
        self.assertEqual(obj_first.is_presented, True)
        self.assertEqual(obj_first.presented_at, datetime.date(2021, 1, 22))
        