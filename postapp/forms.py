from django.forms import ModelForm

from postapp.models import Post


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'post_title', 'image', 'post_content']
        labels = {
            'category': '카테고리',
            'post_title': '제목',
            'image': '이미지',
            'post_content': '내용'
        }