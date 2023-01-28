from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from blogapp.models import Article

@registry.register_document
class ArticleDocument(Document):
    author = fields.ObjectField(properties={
        'username': fields.TextField(),
    })
    content = fields.TextField(
        attr='content'
    )
    class Index:
        name = 'articles'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    # description = fields.TextField(attr='get_description')

    class Django:
        model = Article
        fields = [
            # 'content',
            'title',
            # 'tags',
        ]

# class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
#     content = indexes.CharField(document=True, use_template=True)
#     author = indexes.CharField(model_attr='author')
#     created_on = indexes.DateTimeField(model_attr='created_on')
#
#     def get_model(self):
#         return Article
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()