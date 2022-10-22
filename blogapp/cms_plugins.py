from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase, CMSPlugin
from blogapp.models import Post
from django.db import models

class HotArticles(CMSPlugin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def copy_relations(self, oldinstance):
        self.post.all().delete()
        for post in oldinstance.post.all():
            post.pk = None
            post.post = self
            post.save()


@plugin_pool.register_plugin
class HotArticlesPlugin(CMSPluginBase):
    model = HotArticles
    name = "Hot Articles Plugin"
    render_template = 'plugins/hot_articles_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(HotArticlesPlugin, self).render(context, instance, placeholder)
        context.update({
            'post': instance.post
        })
        return context

