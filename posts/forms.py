from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post


class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'newpost.html'
    success_url = reverse_lazy("index")
    fields = ['group', 'text']

    def get_form(self, form_class=None):
        form = super(NewPost, self).get_form(form_class)
        form.fields['group'].required = False
        form.fields['text'].required = True
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewPost, self).form_valid(form)
