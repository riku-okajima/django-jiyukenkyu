import datetime
from jiyukenkyu_app.models import Presentation

def setUp():
    # 一覧データ
    global object_list
    object_list = Presentation.objects.all().order_by('presented_at')
    # 入力データ
    global input_data
    input_data = {
            # 発表者
            'presenter' : '西○邦○',
            # カテゴリー
            'category' : '1',
            # テーマ
            'theme' : 'python×機械学習で画像認識してみた',
            # 詳細
            'detail' : '機械学習とは？、実装の紹介、まとめ',
            # 発表日
            'presented_at' : datetime.date(2022, 11, 25),
        }