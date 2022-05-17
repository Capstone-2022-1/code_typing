from django.contrib import admin

# Register your models here.


from boardapp.models import PostCategory
from commentapp.models import Comment
from postapp.models import Post


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

