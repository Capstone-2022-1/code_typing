from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
        labels = {
            'comment_content': '댓글 작성'
        }