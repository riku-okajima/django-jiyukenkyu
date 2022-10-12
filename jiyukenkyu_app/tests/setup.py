from jiyukenkyu_app.models import Presentation

def setUp():
    global object_list
    # test_presenter='岡嶋 陸'
    # test_theme='TailwindCSSについて'
    # test_detail='ユーティリティファーストCSSフレームワーク'
    # test_presented_at = datetime.date.today()
    
    # presentation = Presentation()
    # presentation.presenter = test_presenter
    # presentation.theme = test_theme
    # presentation.detail = test_detail
    # presentation.presented_at = test_presented_at
    # presentation.save()
    
    object_list = Presentation.objects.all()