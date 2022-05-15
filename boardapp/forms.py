from django.forms import ModelForm

from boardapp.models import PostCategory


class CategoryCreationForm(ModelForm):
    class Meta:
        model = PostCategory
        fields = ['post_category']
