from django.contrib.auth.models import User
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
