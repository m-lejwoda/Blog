from django.shortcuts import render, redirect
from .models import Post, Tag, EditorProfile, Poster, MainNews
from django.contrib import messages
from .forms import CreateUserForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import ListView, View, DetailView
import json


class ArticleListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blogapp/dashboard.html'

    def get_queryset(self):
        posts = Post.objects.filter().order_by('-created_on')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        editors = EditorProfile.objects.all()
        context.update({'tags': tags, 'editors': editors})
        return context


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
            messages.success(request, 'Gratulacje utworzyłeś swój profil użytkownika ' + user)
            return redirect('login')


class LogoutView(View):

    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')


class TagView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blogapp/tags.html'

    def get_queryset(self):
        return super(TagView, self).get_queryset().filter(tags__slug__icontains=self.kwargs.get('tag'))\
            .order_by('-publish_on')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"tag": self.kwargs.get('tag')})
        return context


class SingleArticleView(View):

    @staticmethod
    def get(request, slug):
        post = Post.objects.get(slug=slug)
        post.clicks = post.clicks + 1
        post.save()
        radioposts = Post.objects.all()
        comments = post.comments.filter()
        posts = Post.objects.all()
        editors = EditorProfile.objects.all()
        context = {'post': post, 'editors': editors, 'posts': posts, 'comments': comments,
                   'radioposts': radioposts}
        return render(request, 'blogapp/radio2.html', context)


class AllNewsView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blogapp/news.html'
    queryset = Post.objects.order_by('-publish_on')


class JournalistDetailView(DetailView):
    model = EditorProfile
    template_name = 'blogapp/journalist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_slug_field())
        print(context)
        return context

def journalist_detail(request, journalist_slug):
    journalist = EditorProfile.objects.get(slug=journalist_slug)
    posters = Poster.objects.all().order_by('-date')
    posts1 = Post.objects.filter(author=journalist.user)
    paginator = Paginator(posts1, 8)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    tags = Tag.objects.all()
    context = {'posts': posts, 'tags': tags, 'journalist': journalist, 'posters': posters}
    return render(request, 'blogapp/journalist.html', context)

# def allnews(request):
#     posts = Post.objects.all().order_by('-publish_on')
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     paginator = Paginator(posts, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     posters = Poster.objects.all()
#
#     context = {'posts': posts, 'tags': tags, 'editors': editors, 'page_obj': page_obj, 'posters': posters}
#     return render(request, 'blogapp/news.html', context)
#

# def blog(request):
#     posts = Post.objects.all().order_by('-publish_on')
#     posters = Poster.objects.all()
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     mainnews = MainNews.objects.all()
#     paginator = Paginator(posts, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     print("lest see blog")
#     context = {'posts': posts, 'tags':tags, 'editors': editors,'page_obj':page_obj,'posters':posters,'mainnews':mainnews}
#     return render(request,'blogapp/dashboard.html',context)


# def main(request):
#     posts = Post.objects.all()
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     context = {'posts': posts, 'tags':tags, 'editors': editors}
#     return render(request,'blogapp/main.html',context)

#WTF
# def post(request):
#     posts = Post.objects.all()
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     mainnews = MainNews.objects.all()
#     context = {'posts': posts, 'tags': tags, 'editors': editors, 'mainnews': mainnews}
#     return render(request, 'blogapp/dashboard.html', context)


# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.info(request, 'Nazwa użytkownika lub hasło są niepoprawne')
#
#     context = {}
#     return render(request, 'blogapp/loginok.html', context)

#
# @csrf_exempt
# def update_radio(request):
#     post = Post.objects.all()
#     tag = Tag.objects.all()
#     editor = EditorProfile.objects.all()
#     data = Post.objects.all()
#     if request.method == 'POST':
#         inp = request.POST.get('input', None)
#         author = request.POST.get('author', None)
#         user = User.objects.get(username=author)
#         if (inp == "radio-two"):
#             data = Post.objects.all().order_by()
#         elif (inp == "radio-three"):
#             data = Post.objects.all().order_by('-publish_on')
#         else:
#             data = Post.objects.all().order_by('-clicks')
#
#     return render(request, 'blogapp/radio2.html', {'data': data})
#
#
# @csrf_exempt
# def radio_test(request, slug):
#     if request.method == 'POST':
#         print("readio_test")
#     return render(request, 'blogapp/radio2.html')
#
#
# def addcomment(request):
#     if request.method == 'POST':
#         print(request.POST)


# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Gratulacje utworzyłeś swój profil użytkownika ' + user)
#             return redirect('login')
#     context = {'form': form}
#     return render(request, 'blogapp/registerok.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('login')
#

# @csrf_exempt

def radio_posts(request):
    identity = request.GET.get('id')
    author = request.GET.get('author')
    if identity == "radio-one":
        user = User.objects.get(username=author)
        posts = Post.objects.all().order_by('-clicks')
        threeposts = posts[0:3]
        result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
        y = json.loads(result)
        dictionary = {}
        for el in y:
            post = Post.objects.get(slug=el['fields']['slug'])
            url = post.image.url
            absoluteurl = {"image": url}
            el['fields'].update(absoluteurl)
        endpoint = json.dumps(y)
        return JsonResponse(endpoint, safe=False)

    if identity == "radio-two":
        user = User.objects.get(username=author)
        posts = Post.objects.filter(author=user).order_by('-publish_on')
        threeposts = posts[0:3]
        result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
        y = json.loads(result)
        dictionary = {}
        for el in y:
            post = Post.objects.get(slug=el['fields']['slug'])
            url = post.image.url
            absoluteurl = {"image": url}
            el['fields'].update(absoluteurl)
        endpoint = json.dumps(y)
        return JsonResponse(endpoint, safe=False)
    if identity == "radio-three":
        posts = Post.objects.all().order_by('-publish_on')[0:3]
        threeposts = posts[0:3]
        result = serializers.serialize('json', threeposts, fields=('title', 'image', 'slug'))
        y = json.loads(result)
        dictionary = {}
        for el in y:
            post = Post.objects.get(slug=el['fields']['slug'])
            url = post.image.url
            absoluteurl = {"image": url}
            el['fields'].update(absoluteurl)
        endpoint = json.dumps(y)
        return JsonResponse(endpoint, safe=False)
    else:
        return None


# @csrf_exempt
# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug)
#     post.clicks = post.clicks + 1
#     post.save()
#     radioposts = Post.objects.all()
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
#                 radioposts = Post.objects.all()
#     comments = post.comments.filter()
#     posts = Post.objects.all()
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     context = {'post': post, 'tags': tags, 'editors': editors, 'posts': posts, 'comments': comments,
#                'radioposts': radioposts}
#     return render(request, 'blogapp/radio2.html', context)


# @csrf_exempt
# def tag_detail(request, tag):
#     tags = Tag.objects.get(slug=tag)
#     posters = Poster.objects.all().order_by('-date')
#     tag_name = Tag.objects.get(slug=tag)
#     posts1 = Post.objects.filter(tags=tags.id).order_by('-publish_on')
#     tags = Tag.objects.all()
#     editors = EditorProfile.objects.all()
#     paginator = Paginator(posts1, 8)
#     page_number = request.GET.get('page')
#     posts = paginator.get_page(page_number)
#     context = {'posts': posts, 'tags': tags, 'editors': editors, 'tag_name': tag_name, 'posters': posters}
#     return render(request, 'blogapp/tags.html', context)




def schedule(request):
    posters = Poster.objects.all().order_by('-date')
    editors = EditorProfile.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(posters, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posters': posters, 'tags': tags, 'editors': editors, 'page_obj': page_obj}
    return render(request, 'blogapp/schedule.html', context)
