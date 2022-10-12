import datetime
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
        global obj_count
        obj_count = test_setup.object_list.count()

    # 頭に必ず「test_」をつける
    def test_url_redirect(self):
        response = self.client.get('')
        self.assertRedirects(
            response=response,
            expected_url=reverse('app:create'),
            status_code=HttpResponseRedirect.status_code,
            target_status_code=HttpResponse.status_code,
            fetch_redirect_response=True)

    def test_url_create(self):
        path = reverse('app:create')
        view = resolve(path)
        response = self.client.get(path)
        
        self.assertEqual(view.func.view_class, Create)
        self.assertEqual(HttpResponse.status_code, response.status_code)

    def test_url_list(self):
        path = reverse('app:list')
        view = resolve(path)
        response = self.client.get(path)
        
        self.assertEqual(view.func.view_class, List)
        self.assertEqual(HttpResponse.status_code, response.status_code)

    def test_url_update(self):
        # モデルのIDでなければならない
        path_ok = reverse('app:update', kwargs={'pk': obj_count})
        path_ng = reverse('app:update', kwargs={'pk': obj_count + 1})
        view = resolve(path_ok)
        response_success = self.client.get(path_ok)
        response_not_found = self.client.get(path_ng)
        
        self.assertEqual(view.func.view_class, Update)
        self.assertEqual(HttpResponse.status_code, response_success.status_code)
        self.assertEqual(HttpResponseNotFound.status_code, response_not_found.status_code)

    def test_url_detail(self):
        path_ok = reverse('app:detail', kwargs={'pk': obj_count})
        path_ng = reverse('app:detail', kwargs={'pk': obj_count + 1})
        view = resolve(path_ok)
        response_success = self.client.get(path_ok)
        response_not_found = self.client.get(path_ng)
        
        self.assertEqual(view.func.view_class, Detail)
        self.assertEqual(HttpResponse.status_code, response_success.status_code)
        self.assertEqual(HttpResponseNotFound.status_code, response_not_found.status_code)

    def test_url_delete(self):
        path_ok = reverse('app:delete', kwargs={'pk': obj_count})
        path_ng = reverse('app:delete', kwargs={'pk': obj_count + 1})
        view = resolve(path_ok)
        response_success = self.client.get(path_ok)
        response_not_found = self.client.get(path_ng)
        
        self.assertEqual(view.func.view_class, Delete)
        self.assertEqual(HttpResponse.status_code, response_success.status_code)
        self.assertEqual(HttpResponseNotFound.status_code, response_not_found.status_code)
