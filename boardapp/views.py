from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from boardapp.forms import CategoryCreationForm
from boardapp.models import PostCategory
from postapp.models import Post


class CategoryCreateView(CreateView):
    model = PostCategory
    form_class = CategoryCreationForm
    template_name = 'boardapp/create.html'

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk':self.object.pk})


class CategoryDetailView(DetailView, MultipleObjectMixin):
    model = PostCategory
    context_object_name = 'target_category'
    template_name = 'boardapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(category=self.get_object())
        return super(CategoryDetailView, self).get_context_data(object_list=object_list, **kwargs)


class CategoryListView(ListView):
    model = PostCategory
    context_object_name = 'category_list'
    template_name = 'boardapp/list.html'
    paginate_by = 5
