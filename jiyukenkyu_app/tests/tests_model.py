import datetime
import jiyukenkyu_app.tests.setup as test_setup
from jiyukenkyu_app.models import Presentation
from django.test import TestCase
from jiyukenkyu_app.tests.setup import setUp
from django.utils import timezone
from freezegun import freeze_time

class TestModel(TestCase):
    # テストデータの生成
    fixtures = ['jiyukenkyu_app.json']

    def setUp(self):
        setUp()
        self.obj_first = test_setup.object_list.first()
        
    # 型チェック
    def test_model_type(self):
        self.assertEqual(type(self.obj_first), Presentation)
        self.assertEqual(type(self.obj_first.pk), int)
        self.assertEqual(type(self.obj_first.theme), str)
        self.assertEqual(type(self.obj_first.presenter), str)
        self.assertEqual(type(self.obj_first.theme), str)
        self.assertEqual(type(self.obj_first.category), int)
        self.assertEqual(type(self.obj_first.detail), str)
        self.assertEqual(type(self.obj_first.is_presented), bool)
        self.assertEqual(type(self.obj_first.presented_at), datetime.date)
        
    # 登録データ参照
    def test_model_data(self):
        self.assertEqual(self.obj_first.pk, 1)
        self.assertEqual(self.obj_first.presenter, 'テスト太郎')
        self.assertEqual(self.obj_first.theme, 'テスト発表テーマ')
        self.assertEqual(self.obj_first.category, 4)
        self.assertEqual(self.obj_first.detail, 'テスト発表についての概要')
        self.assertEqual(self.obj_first.is_presented, True)
        self.assertEqual(self.obj_first.presented_at, datetime.date(2021, 1, 22))
        
    # 管理画面での表示名
    def test_model_return(self):
        self.assertEqual(self.obj_first.__str__(), '2021-01-22:テスト太郎')
        
    # 日時を固定
    @freeze_time('2023-01-01 01:01:01')
    def test_model_time(self):
        new_presenter = '山村○'
        new_theme = 'しくじり先生 俺みたいな先輩になるな！'
        new_detail ='下に人を付けた際にしくじらないための授業'
        new_is_presented = False
        new_obj = Presentation(presenter = new_presenter,
                    theme = new_theme,
                    detail = new_detail,
                    presented_at = datetime.date(2022, 10, 28),
                    is_presented = new_is_presented)
        new_obj.save()
        # auto_now_add（作成日時）とauto_now（更新日時）に格納
        self.assertEqual(new_obj.created_at, datetime.datetime(2023, 1, 1, 1, 1, 1, tzinfo=timezone.utc))
        self.assertEqual(new_obj.updated_at, datetime.datetime(2023, 1, 1, 1, 1, 1, tzinfo=timezone.utc))
        
        # 日時を固定
        with freeze_time('2023-02-02 02:02:02'):
            new_obj.is_presented = True
            new_obj.save()
            # auto_now（更新日時）のみに格納
            self.assertEqual(new_obj.created_at, datetime.datetime(2023, 1, 1, 1, 1, 1, tzinfo=timezone.utc))
            self.assertEqual(new_obj.updated_at, datetime.datetime(2023, 2, 2, 2, 2, 2, tzinfo=timezone.utc))