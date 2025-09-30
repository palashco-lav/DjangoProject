from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogsPost
from .forms import BlogsPostForm


class BlogsPostListView(ListView):
    """Список опубликованных записей"""
    model = BlogsPost
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogsPost.objects.filter(is_published=True)


class BlogsPostDetailView(DetailView):
    """Детальная страница записи"""
    model = BlogsPost
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        """Увеличиваем счетчик просмотров при каждом просмотре"""
        response = super().get(request, *args, **kwargs)
        self.object.increment_views()
        return response


class BlogsPostCreateView(CreateView):
    """Создание новой записи"""
    model = BlogsPost
    form_class = BlogsPostForm
    template_name = 'blogs/post_form.html'
    success_url = reverse_lazy('blogs:post_list')

    def form_valid(self, form):
        """Дополнительные действия при валидной форме"""
        return super().form_valid(form)


class BlogsPostUpdateView(UpdateView):
    """Редактирование записи"""
    model = BlogsPost
    form_class = BlogsPostForm
    template_name = 'blogs/post_form.html'

    def get_success_url(self):
        return reverse_lazy('blogs:post_detail', kwargs={'pk': self.object.pk})


class BlogsPostDeleteView(DeleteView):
    """Удаление записи"""
    model = BlogsPost
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('blogs:post_list')
    context_object_name = 'post'