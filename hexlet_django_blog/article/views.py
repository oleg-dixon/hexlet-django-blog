from django.http import HttpResponse
from django.views import View


class IndexViewApp(View):
    def get(self, request, *args, **kwargs):
        tags = kwargs.get('tags')
        article_id = kwargs.get('article_id')
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
