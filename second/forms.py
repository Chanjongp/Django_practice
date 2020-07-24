from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

# class PostForm(forms.Form):
#     title = forms.CharField(label='title', max_length=200)
#     content = forms.CharField(label='description', widget=forms.Textarea)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        # labels = {
        #     'title' : _('title'),
        #     'content' : _('contents')
        # }
        help_texts = {
            'title' : _('제목을 입력해주세요'),
            'content': _('내용을 입력하세요'),
        }
        error_messages = {
            'name' : {
                'max_length':_("제목이 너무 깁니다. 30자 이하로 해주세요")
            }
        }