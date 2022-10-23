from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase, CMSPlugin
from blogapp.models import Post, Poster
from django.db import models

class EventPlugin(CMSPlugin):
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE, related_name='poster')

class HotArticles(CMSPlugin):
    firstpost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='firstpost')
    secondpost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='secondpost')
    thirdpost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='thirdpost')

    def copy_relations(self, oldinstance):
        self.firstpost.all().delete()
        self.secondpost.all().delete()
        self.thirdpost.all().delete()
        for post1 in oldinstance.firstpost.all():
            post1.pk = None
            post1.post = self
            post1.save()
        for post2 in oldinstance.secondpost.all():
            post2.pk = None
            post2.post = self
            post2.save()
        for post3 in oldinstance.thirdpost.all():
            post3.pk = None
            post3.post = self
            post3.save()


@plugin_pool.register_plugin
class HotArticlesPlugin(CMSPluginBase):
    model = HotArticles
    name = "Hot Articles Plugin"
    render_template = 'plugins/hot_articles_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(HotArticlesPlugin, self).render(context, instance, placeholder)
        context.update({
            'firstpost': instance.firstpost,
            'secondpost': instance.secondpost,
            'thirdpost': instance.thirdpost
        })
        return context

@plugin_pool.register_plugin
class NewArticlesPlugin(CMSPluginBase):
    model = CMSPlugin
    name = "New Articles Plugin"
    render_template = 'plugins/new_articles_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(NewArticlesPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class EventPlugin(CMSPluginBase):
    model = EventPlugin
    name = "Event Plugin"
    render_template = 'plugins/event_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(EventPlugin, self).render(context, instance, placeholder)
        return context

