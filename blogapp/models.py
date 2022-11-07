from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from .choices import Ranks, News_Category


# class Category(models.Model):
#     name = models.CharField(max_length=32)
#
#     class Meta:
#         verbose_name_plural = "Categories"
#
#     def __str__(self):
#         return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    image = models.ImageField(default="")
    date = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)


class EditorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor')
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    avatar = models.ImageField()
    slug = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField()
    rank = models.CharField(
        max_length=20,
        choices=Ranks,
        default=Ranks.Redaktor,
    )

    def __str__(self):
        return self.user.username


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_articles')
    editor_profile = models.ForeignKey(EditorProfile, on_delete=models.CASCADE, blank=True, null=True)
    show_in_main_news = models.BooleanField(default=True)
    category = models.CharField(
        max_length=20,
        choices=News_Category,
        default=News_Category.News,
    )
    title = models.CharField(max_length=64)
    # short_description = models.CharField(max_length=200, default="")
    image = models.ImageField(default="")
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    clicks = models.IntegerField(default=0, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False, )
    created_on = models.DateTimeField(auto_now=True, null=False, blank=False, )
    publish_on = models.DateTimeField(auto_now=True, null=False, blank=False, )
    list_display = ('title', 'category', 'tags', 'author', 'publish_on', 'created_on', 'updated_on')
    search_fields = ['title', 'byline', 'symbol']
    list_filter = ['publish_on', 'created_on']
    date_hierarchy = 'pub_date'
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',
                                        related_query_name='hit_count_generic_relation')

    @property
    def get_absolute_image_url(self):
        return '{}'.format(self.image.url)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


class Link(models.Model):
    content = models.URLField()
    url = models.URLField()
    slug = models.SlugField(max_length=128)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Social(models.Model):
    content = models.URLField()
    url = models.URLField()
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Social networks"




# class MainNews(models.Model):
#     post = models.ManyToManyField(Article, related_name='posts')


def editor_create_slug(instance, new_slug=None):
    slug = slugify(instance.user.first_name) + "_" + slugify(instance.user.last_name)
    if new_slug is not None:
        slug = new_slug
    qs = EditorProfile.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return editor_create_slug(instance, new_slug=new_slug)
    return slug


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


def pre_save_editor_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = editor_create_slug(instance)


def tag_create_slug(instance, new_slug=None):
    txt = instance.name.replace(" ", "_")
    slug = slugify(txt)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return tag_create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_tag_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = tag_create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Article)
pre_save.connect(pre_save_editor_receiver, sender=EditorProfile)
pre_save.connect(pre_save_tag_receiver, sender=Tag)
