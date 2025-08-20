from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'Приложение на Django!'
        return context


def about(request):
    return render(
        request,
        'about.html',
    )


# def redirect_view(request):
#     return redirect(reverse('articles', kwargs={'tags': 'Python', 'article_id': 42}))