from django.http import JsonResponse
from django.template.loader import render_to_string

from ManagementSoftware.models import Article


# Create your views here.
def all_articles(request):
    data = dict()
    if request.method == 'GET':
        articles = Article.objects.all()
        data['table'] = render_to_string(
            'article/articles_table.html',
            {'articles': articles},
            request=request
        )
    return JsonResponse(data)
