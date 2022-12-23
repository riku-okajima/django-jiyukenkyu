import jiyukenkyu_app.tests.setup as test_setup
from django.urls import reverse
from .setup import setUp
from django.test import TestCase
from django.http import HttpResponse, HttpResponseRedirect

# Create your tests here.
class TestViews(TestCase):
    fixtures = ['jiyukenkyu_app.json']

    def setUp(self):
        setUp()

    def test_create_ok(self):
        response = self.client.post(reverse('app:create'), test_setup.input_data)
        # DBに登録されたことの確認
        self.assertEqual(test_setup.object_list.filter(theme='python×機械学習で画像認識してみた').count(), 1)
        # 一覧画面へのリダイレクト確認
        self.assertRedirects(
            response=response,
            expected_url=reverse('app:list'),
            status_code=HttpResponseRedirect.status_code,
            target_status_code=HttpResponse.status_code,
            fetch_redirect_response=True)

    def test_create_ng(self):
        test_setup.input_data['detail'] = ''
        response = self.client.post(reverse('app:create'), test_setup.input_data)
        # エラーメッセージの確認
        self.assertFormError(
            response=response,
            form='form',
            field='detail',
            errors='このフィールドは必須です。')
        # DBに登録されていないことの確認
        self.assertEqual(test_setup.object_list.filter(theme='python×機械学習で画像認識してみた').count(), 0)
        # フォーム画面のままであることの確認
        self.assertTemplateUsed(response, 'form.html')

    def test_list(self):
        response = self.client.get(reverse('app:list'))
        presentations = response.context['object_list']
        # レンダリングするテンプレート
        self.assertTemplateUsed(response, 'list.html')
        # リストの件数は等しいか
        self.assertEqual(test_setup.object_list.count(), len(presentations))
        # リストの内容とソート順は等しいか
        self.assertQuerysetEqual(test_setup.object_list, presentations, ordered=True)