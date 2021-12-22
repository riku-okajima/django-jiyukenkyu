from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .models import Presentation
from .forms import PresentationForm
from datetime import date
from django.db import connection

''' 共通利用ラベル '''
def common_label(self):
    context = {}
    context['presented_at_label'] = '発表日'
    context['presenter_label'] = '発表者'
    context['category_label'] = 'カテゴリ'
    context['theme_label'] = '発表テーマ'
    context['detail_label'] = '詳細'
    context['status_label'] = 'ステータス'
    context['before_presentation'] = '発表前'
    context['after_presentation'] = '発表済み'
    context['list_btn'] = '発表リスト'
    context['add_btn'] = '発表を追加する'
    context['detail_btn'] = '詳細'
    context['modify_btn'] = '修正'
    context['delete_btn'] = '削除'
    context['back_btn'] = '戻る'
    return context

''' 登録 '''
class Create(CreateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'form.html'
    success_url = reverse_lazy('app:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(common_label(self))
        context['create_title'] = 'じゆうけんきゅうを追加する'
        context['submit_btn'] = '新規登録'
        context['is_create'] = True
        Presentation.objects.all()
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        today = date.today()
        if obj.presented_at > today:
            obj.is_presented = False
        return super().form_valid(form)
 
    def form_invalid(self, form):
        return super().form_invalid(form)
    
''' 一覧 '''
class List(ListView):
    model = Presentation
    template_name = 'list.html'
    ordering = 'presented_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(common_label(self))
        context['list_title'] = 'じゆうけんきゅう一覧'
        list_count = len(self.object_list)
        context['count'] = '件数全 / {} 件'.format(list_count)
        return context

''' 詳細 '''
class Detail(DetailView):
    model = Presentation
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(common_label(self))
        return context

''' 更新 '''
class Update(UpdateView):
    template_name = 'form.html'
    model = Presentation
    form_class = PresentationForm
    success_url = reverse_lazy('app:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(common_label(self))
        context['update_title'] = '発表内容更新'
        context['update_btn'] = '更新'
        context['is_update'] = True
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        today = date.today()
        if obj.presented_at > today:
            obj.is_presented = False
        return super().form_valid(form)
 
    def form_invalid(self, form):
        return super().form_invalid(form)

''' 削除 '''
class Delete(DeleteView):
    template_name = 'delete.html'
    model = Presentation
    success_url = reverse_lazy('app:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(common_label(self))
        context['delete_title'] = 'この発表を削除しますか？'
        return context





# SQLバージョン
# def get_list_sql():
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM jiyukenkyu_app_presentation"
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         return data