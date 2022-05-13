from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from postapp.forms import PostCreationForm
from postapp.models import Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk':self.object.pk})



class PostDetailView(DetailView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'postapp/detail.html'
