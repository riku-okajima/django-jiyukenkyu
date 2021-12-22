from django import forms
from django.forms import widgets
from .models import Presentation

class PresentationForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = (
            'presenter',
            'category',
            'theme',
            'detail',
            'presented_at'
        )
        labels = {
           'presenter': '発表者',
           'category': 'カテゴリ',
           'theme': '発表テーマ',
           'detail': '発表内容',
           'presented_at': '発表日',
        }
        widgets = {
            'presented_at': widgets.NumberInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ラベルの「:」消去
        self.label_suffix = ""
        # 各フィールドにクラス属性付与
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    
    def clean_theme(self):
        theme = self.cleaned_data.get('theme')
        if len(theme) > 30:
            raise forms.ValidationError("発表テーマは30文字以下で入力してください")
        return theme
    
    def clean_detail(self):
        detail = self.cleaned_data.get('detail')
        if len(detail) < 10:
            raise forms.ValidationError("発表内容は10文字以上で入力してください")
        return detail