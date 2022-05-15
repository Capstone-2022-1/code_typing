from django.forms import ModelForm

from postapp.models import Post


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'post_title', 'image', 'post_content']