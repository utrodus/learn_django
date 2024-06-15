from django.views.generic import ListView, TemplateView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "home"
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "detail_post"


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "about"
        return context
