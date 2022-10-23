from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase, CMSPlugin
from blogapp.models import Post, Poster
from django.db import models


"""CMS Plugin models"""


class Event(CMSPlugin):
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE, related_name='poster')


class HotArticles(CMSPlugin):
    first_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='first_post')
    second_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='second_post')
    third_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='third_post')

    def copy_relations(self, oldinstance):
        self.first_post.all().delete()
        self.second_post.all().delete()
        self.third_post.all().delete()
        for first in oldinstance.first_post.all():
            first.pk = None
            first.post = self
            first.save()
        for second in oldinstance.second_post.all():
            second.pk = None
            second.post = self
            second.save()
        for third in oldinstance.third_post.all():
            third.pk = None
            third.post = self
            third.save()


"""CMS Plugin Base models"""


@plugin_pool.register_plugin
class HotArticlesPlugin(CMSPluginBase):
    model = HotArticles
    name = "Hot Articles Plugin"
    render_template = 'plugins/hot_articles_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(HotArticlesPlugin, self).render(context, instance, placeholder)
        context.update({
            'first_post': instance.first_post,
            'second_post': instance.second_post,
            'third_post': instance.third_post
        })
        return context



@plugin_pool.register_plugin
class EventPlugin(CMSPluginBase):
    model = Event
    name = "Event Plugin"
    render_template = 'plugins/event_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(EventPlugin, self).render(context, instance, placeholder)
        return context
