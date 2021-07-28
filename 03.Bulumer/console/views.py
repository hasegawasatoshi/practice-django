import json
from django.views import generic
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def index(request):
#     content = {'object_list': {}}
#     return render(request, 'console/index.html', content)


class IndexView(generic.TemplateView):
    template_name = "console/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = [
            {
                'id': 1,
                'name': 'ABC-123456',
                'onwner': 'ABC Corp.'
            },
            {
                'id': 2,
                'name': 'CZY-66442',
                'onwner': 'ABC Corp.'
            },
            {
                'id': 3,
                'name': 'DXZ-987123',
                'onwner': 'ZYX Inc.'
            }
        ]
        context['labels'] = ["8月1日", "8月2日", "8月3日",
                             "8月4日", "8月5日", "8月6日", "8月7日", "8月8日"]
        context['tempareture'] = [28.4, 24.4, 31.2, 28, 25.5, 23, 22.9, 25.6]
        return context


@api_view(['GET'])
def get_data(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = {
            'labels': ["8月1日", "8月2日", "8月3日",
                       "8月4日", "8月5日", "8月6日", "8月7日", "8月8日"],
            'tempareture': [28.4, 24.4, 31.2, 28, 25.5, 23, 22.9, 25.6]
        }
        return Response(data)
