from django.shortcuts import render, redirect
from django.views.generic.list import MultipleObjectMixin
from .models import Article, Tag, EditorProfile, Schedule, Comment
from django.contrib import messages
from .forms import CreateUserForm, CommentForm, CreateBlogArticleForm, CreateEditorArticleForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import ListView, View, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone
from .choices import News_Category
from blogapp.documents import ArticleDocument
from django.core.cache import cache


class ArticleListView(ListView):
    model = Article
    paginate_by = 2
    template_name = 'blogapp/dashboard.html'

    def get_queryset(self):
        newest_articles = cache.get('newest_articles')
        if newest_articles is None:
            articles = Article.objects.filter().order_by('-created_on')[:15]
            cache.set('newest_articles', articles)
        return newest_articles

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     tags = Tag.objects.all()
    #     editors = EditorProfile.objects.all()
    #     context.update({'tags': tags, 'editors': editors})
    #     return context


class BlogsListView(ListView):
    model = Article
    paginate_by = 10
    template_name = 'blogapp/blogs.html'

    def get_queryset(self):
        articles = Article.objects.filter(category=News_Category.Blog).order_by('-publish_on')
        return articles


class LoginView(View):
    @staticmethod
    def get(request):
        return render(request, 'blogapp/loginok.html')

    @staticmethod
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Nazwa użytkownika lub hasło są niepoprawne')

        context = {}
        return render(request, 'blogapp/loginok.html', context)


class RegisterView(View):
    @staticmethod
    def get(request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'blogapp/registerok.html', context)

    @staticmethod
    def post(request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request, 'Gratulacje utworzyłeś swój profil użytkownika ' + user)
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'blogapp/registerok.html', context)


class LogoutView(View):

    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')


class TagView(ListView):
    model = Article
    paginate_by = 2
    template_name = 'blogapp/tags.html'

    def get_queryset(self):

        return super(TagView, self).get_queryset().filter(tags__slug__icontains=self.kwargs.get('tag'))\
            .order_by('-publish_on')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"tag": self.kwargs.get('tag')})
        return context


class SingleArticleView(DetailView, MultipleObjectMixin):
    model = Article
    template_name = 'blogapp/radio2.html'
    form = CommentForm
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        comments = Comment.objects.filter(post=self.get_object())
        radioposts = Article.objects.all()
        author = self.get_object().author
        context = super(SingleArticleView, self).get_context_data(object_list=comments, author=author, radioposts=radioposts, **kwargs)
        return context

    def post(self, request, slug):
        self.object = self.get_object()
        comments = Comment.objects.filter(post=self.get_object())
        if 'comment' in request.POST:
            text = request.POST.get("comment", None)
            form = CommentForm({'text': text})
            if form.is_valid():
                instance = form.save(commit=False)
                instance.post = self.get_object()
                instance.author = self.request.user
                instance.text = text
                instance.save()
        context = super(SingleArticleView, self).get_context_data(object_list=comments)
        return render(request, self.template_name, {'context': context, 'form': form})


class AllNewsView(ListView):
    model = Article
    paginate_by = 2
    template_name = 'blogapp/news.html'
    queryset = Article.objects.order_by('-publish_on')


class UserBlogDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'blogapp/journalist.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(user=self.get_object())
        context = super(UserBlogDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class JournalistDetailView(DetailView, MultipleObjectMixin):
    model = EditorProfile
    template_name = 'blogapp/journalist.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(editor_profile=self.get_object())
        context = super(JournalistDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class ArchivalScheduleView(ListView):
    model = Schedule
    template_name = 'blogapp/schedule.html'
    paginate_by = 2
    # queryset = Schedule.objects.filter(date__date__lt=timezone.now().date())

    def get_queryset(self):
        archival_schedule = cache.get('archival_schedule')
        if archival_schedule is None:
            archival_schedule = Schedule.objects.filter(date__date__lt=timezone.now().date())
            cache.set('archival_schedule', archival_schedule, 6*3600)
        return archival_schedule


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpcomingScheduleView(ListView):
    model = Schedule
    template_name = 'blogapp/schedule.html'
    paginate_by = 2
    # queryset = Schedule.objects.filter(date__date__gte=timezone.now().date())

    def get_queryset(self):
        upcoming_schedule = cache.get('upcoming_schedule')
        if upcoming_schedule is None:
            upcoming_schedule = Schedule.objects.filter(date__date__gte=timezone.now().date())
            cache.set('upcoming_schedule', upcoming_schedule, 6*3600)
        return upcoming_schedule


class CreateEditorArticleView(UserPassesTestMixin, FormView):
    login_url = '/login/'
    redirect_field_name = '/create_editor_article/'
    template_name = 'blogapp/create_article.html'
    form_class = CreateEditorArticleForm
    success_url = '/blogs/'

    def handle_no_permission(self):
        """ Do whatever you want here if the user doesn't pass the test """
        return HttpResponse('You have been denied')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.editor_profile = self.request.user.editor
        form.show_in_main_news = True
        form.save()
        return super().form_valid(form)


class CreateArticleBlogView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = '/create_blog_post/'
    template_name = 'blogapp/create_blog_article.html'
    form_class = CreateBlogArticleForm
    success_url = '/blogs/'

    def handle_no_permission(self):
        """ Do whatever you want here if the user doesn't pass the test """
        return HttpResponse('You have been denied')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.category = News_Category.Blog
        form.show_in_main_news = False
        form.save()
        return super().form_valid(form)

def search(request):
    s = ArticleDocument.search().query('multi_match', query='test', fields=['title', 'content'])
    for hit in s:
        print(hit.author)
        print(hit.title)
        print(hit.content)

    return HttpResponse("test")

class SearchView(ListView):
    model = ArticleDocument
    paginate_by = 2
    template_name = 'blogapp/tags.html'

    def get_queryset(self):
        articles = ArticleDocument.search().query('multi_match', query='keszke', fields=['title', 'content'])[:30]
        return articles.to_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)


        context.update({'title': "Wyniki wyszukiwania"})
        # print("context")
        # print(context['object_list'])
        # for i in context['object_list']:
        #     print(i.title)
        #     print(i.content)
        # context.update({"tag": self.kwargs.get('tag')})
        return context


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
#         print("result")
#         print(result)
#         y = json.loads(result)
#         dictionary = {}
#         for el in y:
#             post = Article.objects.get(slug=el['fields']['slug'])
#             url = post.image.url
#             absoluteurl = {"image": url}
#             el['fields'].update(absoluteurl)
#         print("y")
#         print(y)
#         endpoint = json.dumps(y)
#         print("endpoint")
#         print(endpoint)
#         return JsonResponse(endpoint, safe=False)
#     else:
#         return None


# @csrf_exempt
# def post_detail(request, slug):
#     post = Article.objects.get(slug=slug)
#     post.clicks = post.clicks + 1
#     post.save()
#     radioposts = Article.objects.all()
#     if request.method == "POST":
#         if 'textar' in request.POST:
#             user = User.objects.get(username=request.user)
#             text = request.POST.get("textar", None)
#             data = {
#                 'post': post.id,
#                 'author': user.id,
#                 'text': text}
#             form = CommentForm(data)
#             if form.is_valid():
#                 form.save()
#
#         if 'radio' in request.POST:
#             radio = request.POST.get("input", None)
#             if (radio == "radio-two"):
#                 radioposts = Tag.objects.all()
#             elif (radio == "radio-three"):
#                 radioposts = EditorProfile.objects.all()
#             else:
#                 radioposts = Article.objects.all()
#     comments = post.comments.filter()
#     posts = Article.objects.all()
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     context = {'post': post, 'tags': tags, 'editors': editors, 'posts': posts, 'comments': comments,
#                'radioposts': radioposts}
#     return render(request, 'blogapp/radio2.html', context)


# @csrf_exempt
# def tag_detail(request, tag):
#     tags = Tag.objects.get(slug=tag)
#     posters = Schedule.objects.all().order_by('-date')
#     tag_name = Tag.objects.get(slug=tag)
#     posts1 = Article.objects.filter(tags=tags.id).order_by('-publish_on')
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     paginator = Paginator(posts1, 8)
#     page_number = request.GET.get('page')
#     posts = paginator.get_page(page_number)
#     context = {'posts': posts, 'tags': tags, 'editors': editors, 'tag_name': tag_name, 'posters': posters}
#     return render(request, 'blogapp/tags.html', context)



# TODO Correct Archival Upcoming or Remove
# def schedule(request):
#     posters = Schedule.objects.all().order_by('-date')
#     editors = EditorProfile.objects.all()
#     tags = Tag.objects.all()
#     paginator = Paginator(posters, 8)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'posters': posters, 'tags': tags, 'editors': editors, 'page_obj': page_obj}
#     return render(request, 'blogapp/schedule.html', context)
