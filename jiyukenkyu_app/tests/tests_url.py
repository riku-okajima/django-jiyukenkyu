import jiyukenkyu_app.tests.setup as test_setup
from django.test import TestCase
from django.urls import reverse, resolve
from jiyukenkyu_app.tests.setup import setUp
from jiyukenkyu_app.views import Create, Delete, Detail, List, Update
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your tests here.
class TestUrls(TestCase):
    fixtures = ['jiyukenkyu_app.json']

    # コンストラクタメソッド
    def setUp(self):
        setUp()
        self.obj_last_pk = test_setup.object_list.last().pk

    # 頭に必ず「test_」をつける
    def test_redirect(self):
        response = self.client.get('')
        self.assertRedirects(
            response=response,
            expected_url=reverse('app:create'),
            status_code=HttpResponseRedirect.status_code,
            target_status_code=HttpResponse.status_code,
            fetch_redirect_response=True)

    def test_create(self):
        path = reverse('app:create')
        view = resolve(path)
        response = self.client.get(path)
        
        self.assertEqual(view.func.view_class, Create)
        self.assertEqual(HttpResponse.status_code, response.status_code)

    def test_list(self):
        path = reverse('app:list')
        view = resolve(path)
        response = self.client.get(path)
        
        self.assertEqual(view.func.view_class, List)
        self.assertEqual(HttpResponse.status_code, response.status_code)

    def test_update_ok(self):
        # モデルのIDでなければならない
        path_ok = reverse('app:update', kwargs={'pk': self.obj_last_pk})
        view = resolve(path_ok)
        response_success = self.client.get(path_ok)
        
        self.assertEqual(view.func.view_class, Update)
        self.assertEqual(HttpResponse.status_code, response_success.status_code)
        
    def test_update_ng(self):
        path_ng = reverse('app:update', kwargs={'pk': self.obj_last_pk + 1})
        response_not_found = self.client.get(path_ng)
        self.assertEqual(HttpResponseNotFound.status_code, response_not_found.status_code)

    def test_detail_ok(self):
        path_ok = reverse('app:detail', kwargs={'pk': self.obj_last_pk})
        view = resolve(path_ok)
        response_success = self.client.get(path_ok)
        
        self.assertEqual(view.func.view_class, Detail)
        self.assertEqual(HttpResponse.status_code, response_success.status_code)

    def test_detail_ng(self):
        path_ng = reverse('app:detail', kwargs={'pk': self.obj_last_pk + 1})
        response_not_found = self.client.get(path_ng)
        self.assertEqual(HttpResponseNotFound.status_code, response_not_found.status_code)
        
    def test_delete_ok(self):
        path_ok = reverse('app:delete', kwargs={'pk': self.obj_last_pk})
        view = resolve(path_ok)
        response_success = self.client.get(path_ok)
        
        self.assertEqual(view.func.view_class, Delete)
        self.assertEqual(HttpResponse.status_code, response_success.status_code)

    def test_delete_ng(self):
        path_ng = reverse('app:delete', kwargs={'pk': self.obj_last_pk + 1})
        response_not_found = self.client.get(path_ng)
        self.assertEqual(HttpResponseNotFound.status_code, response_not_found.status_code)