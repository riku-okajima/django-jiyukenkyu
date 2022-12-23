import django
from django.db import models
# from django.conf import settings
# settings.configure()
# django.setup()

''' じゆうけんきゅうモデル '''
class Presentation(models.Model):
    class Meta:
        app_label = 'jiyukenkyu_app'
        db_table = 'presentations'
    
    CHOICES = (
        (1, '技術系'),
        (2, '業務系'),
        (3, 'ビジネススキル'),
        (4, 'その他'),
    )

    # 発表者
    presenter = models.CharField(max_length=20)
    # テーマ
    theme = models.CharField(max_length=30)
    # カテゴリー
    category = models.IntegerField(choices=CHOICES, default=CHOICES[0][0])
    # 詳細
    detail = models.TextField()
    # 発表日
    presented_at = models.DateField()
    # 発表済みフラグ
    is_presented = models.BooleanField(default=True)
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.presented_at) + ':' + self.presenter