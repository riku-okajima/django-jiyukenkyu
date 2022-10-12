from django.urls import path
from . import views
from django.views.generic import RedirectView

# アプリケーションの名前空間を定義
app_name = 'app'

urlpatterns = [
    # 空のURLで登録画面にリダイレクト
    path('', RedirectView.as_view(url='/create/')),
    path('create/', views.Create.as_view(), name='create'),
    path('list/', views.List.as_view(), name='list'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
]
