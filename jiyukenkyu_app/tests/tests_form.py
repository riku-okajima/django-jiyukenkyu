import jiyukenkyu_app.tests.setup as test_setup
from django.test import TestCase
from ..forms import PresentationForm
from .setup import setUp


class TestForm(TestCase):
    def setUp(self):
        setUp()
        self.form = PresentationForm(test_setup.input_data)
        
    def test_ok(self):
        self.assertTrue(self.form.is_valid())
        
    def test_check_category(self):
        ng_category = 5
        test_setup.input_data['category'] = ng_category
        self.form = PresentationForm(test_setup.input_data)
        self.assertEqual(self.form.errors['category'][0], '正しく選択してください。 5 は候補にありません。')

    def test_check_theme(self):
        test_setup.input_data['theme'] = ''
        self.form = PresentationForm(test_setup.input_data)
        self.assertFalse(self.form.is_valid())
        self.assertEqual(self.form.errors['theme'][0], 'このフィールドは必須です。')
        
        ng_theme = '31文字31文字31文字31文字31文字31文字31文字31文'
        test_setup.input_data['theme'] = ng_theme
        self.form = PresentationForm(test_setup.input_data)
        self.assertFalse(self.form.is_valid())
        self.assertEqual(self.form.errors['theme'][0],
                         'この値は 30 文字以下でなければなりません( 31 文字になっています)。')

        ok_theme = '30文字30文字30文字30文字30文字30文字30文字30'
        test_setup.input_data['theme'] = ok_theme
        self.form = PresentationForm(test_setup.input_data)
        self.assertTrue(self.form.is_valid())

    def test_check_detail(self):
        test_setup.input_data['detail'] = ''
        self.form = PresentationForm(test_setup.input_data)
        self.assertFalse(self.form.is_valid())
        self.assertEqual(self.form.errors['detail'][0], 'このフィールドは必須です。')
        
        ng_detail = '9文字9文字9文字'
        test_setup.input_data['detail'] = ng_detail
        self.form = PresentationForm(test_setup.input_data)
        self.assertFalse(self.form.is_valid())
        self.assertEqual(self.form.errors['detail'][0], '発表内容は10文字以上で入力してください')
        
        ok_detail = '10文字10文字10'
        test_setup.input_data['detail'] = ok_detail
        self.form = PresentationForm(test_setup.input_data)
        self.assertTrue(self.form.is_valid())
        
    def test_check_presented_at(self):
        test_setup.input_data['presented_at'] = None
        self.form = PresentationForm(test_setup.input_data)
        self.assertFalse(self.form.is_valid())
        self.assertEqual(self.form.errors['presented_at'][0], 'このフィールドは必須です。')