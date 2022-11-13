from django.contrib.auth.models import User
from django.views import View
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from .serializers import ArticleSerializer
from blogapp.models import Article


class Choose3Articles(ListModelMixin, viewsets.GenericViewSet):
    def get_queryset(self):
        if self.request.query_params.get('id') == 'radio-one':
            return Article.objects.all().order_by('-clicks')[:3]
        elif self.request.query_params.get('id') == 'radio-two':
            user = User.objects.get(username=self.request.query_params.get('author'))
            return Article.objects.filter(author=user).order_by('-publish_on')[:3]
        elif self.request.query_params.get('id') == 'radio-three':
            return Article.objects.all().order_by('-publish_on')[:3]
        else:
            return Article.objects.all().order_by('-clicks')[:3]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

# class Choose3Articles(View):
#     def get(self, request):
#         identity = request.GET.get('id')
#         author = request.GET.get('author')
#         if identity == "radio-one":
#             user = User.objects.get(username=author)
#             posts = Article.objects.all().order_by('-clicks')
#             threeposts = posts[0:3]
#             result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
#             y = json.loads(result)
#             dictionary = {}
#             for el in y:
#                 post = Article.objects.get(slug=el['fields']['slug'])
#                 url = post.image.url
#                 absoluteurl = {"image": url}
#                 el['fields'].update(absoluteurl)
#             endpoint = json.dumps(y)
#             return JsonResponse(endpoint, safe=False)




# def radio_posts(request):
#     identity = request.GET.get('id')
#     author = request.GET.get('author')
#     if identity == "radio-one":
#         user = User.objects.get(username=author)
#         posts = Article.objects.all().order_by('-clicks')
#         threeposts = posts[0:3]
#         result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
#         y = json.loads(result)
#         dictionary = {}
#         for el in y:
#             post = Article.objects.get(slug=el['fields']['slug'])
#             url = post.image.url
#             absoluteurl = {"image": url}
#             el['fields'].update(absoluteurl)
#         endpoint = json.dumps(y)
#         return JsonResponse(endpoint, safe=False)
#
#     if identity == "radio-two":
#         user = User.objects.get(username=author)
#         posts = Article.objects.filter(author=user).order_by('-publish_on')
#         threeposts = posts[0:3]
#         result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
#         y = json.loads(result)
#         dictionary = {}
#         for el in y:
#             post = Article.objects.get(slug=el['fields']['slug'])
#             url = post.image.url
#             absoluteurl = {"image": url}
#             el['fields'].update(absoluteurl)
#         endpoint = json.dumps(y)
#         return JsonResponse(endpoint, safe=False)
#     if identity == "radio-three":
#         posts = Article.objects.all().order_by('-publish_on')[0:3]
#         threeposts = posts[0:3]
#         result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
#         y = json.loads(result)
#         dictionary = {}
#         for el in y:
#             post = Article.objects.get(slug=el['fields']['slug'])
#             url = post.image.url
#             absoluteurl = {"image": url}
#             el['fields'].update(absoluteurl)
#         endpoint = json.dumps(y)
#         return JsonResponse(endpoint, safe=False)
#     else:
#         return None
