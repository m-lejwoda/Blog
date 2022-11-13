from rest_framework import serializers

from blogapp.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'image', 'slug', 'author']