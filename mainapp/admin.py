from django.contrib import admin

# Register your models here.


from boardapp.models import PostCategory
from commentapp.models import Comment
from postapp.models import Post
from practiceapp.models import Practice, Language

from upracticeapp.models import Upractice

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Upractice)
admin.site.register(Practice)
admin.site.register(Language)

