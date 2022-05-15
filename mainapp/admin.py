from django.contrib import admin

# Register your models here.


from boardapp.models import PostCategory
from postapp.models import Post


admin.site.register(Post)
admin.site.register(PostCategory)

