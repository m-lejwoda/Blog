from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase, CMSPlugin
from django.contrib.auth.models import User

from blogapp.choices import News_Category
from blogapp.models import Article, Schedule, Tag, EditorProfile
from django.db import models
from django.core.cache import cache


"""CMS Plugin models"""


class Event(CMSPlugin):
    poster = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='poster')


class HotArticles(CMSPlugin):
    first_post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='first_post')
    second_post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='second_post')
    third_post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='third_post')

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


@plugin_pool.register_plugin
class JournalistsPlugin(CMSPluginBase):
    name = 'Journalists Plugin'
    render_template = 'plugins/journalists_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        all_editors = cache.get('all_editors')
        if all_editors is None:
            all_editors = EditorProfile.objects.all()
            cache.set('all_editors', all_editors)
        context.update({"editors": all_editors})
        return context


@plugin_pool.register_plugin
class TagPlugin(CMSPluginBase):
    name = 'Tag Plugin'
    render_template = 'plugins/tag_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        all_tags = cache.get('all_tags')
        if all_tags is None:
            all_tags = Tag.objects.all()
            cache.set('all_tags', all_tags)
        context.update({"tags": all_tags})
        return context


@plugin_pool.register_plugin
class ActiveBlogUsersPlugin(CMSPluginBase):
    name = 'Active Blog Users Plugin'
    render_template = 'plugins/active_blog_user_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        active_blog_users = cache.get('active_blog_users')
        if active_blog_users is None:
            active_blog_users = User.objects.filter(author_articles__category=News_Category.Blog).annotate(
                number_of_blogs=models.Count('author_articles')).order_by('-number_of_blogs')[:10]
            cache.set('active_blog_users', active_blog_users, 3*3600)
        context.update({'users': active_blog_users})
        return context


@plugin_pool.register_plugin
class MostUsersCommentsPlugin(CMSPluginBase):
    name = 'Most Users Comments Plugin'
    render_template = 'plugins/most_users_comments_plugin.html'
    cache = True

    def render(self, context, instance, placeholder):
        most_users_comments = cache.get('most_users_comments')
        if most_users_comments is None:
            most_users_comments = User.objects.annotate(
                number_of_comments=models.Count('comments')).order_by('-number_of_comments')[:10]
            cache.set('most_users_comments', most_users_comments, 3*3600)
        context.update({'users': most_users_comments})
        return context

