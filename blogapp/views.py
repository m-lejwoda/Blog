from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Tag,EditorProfile,Comment,Poster,MainNews
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm,CommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
from hitcount.views import HitCountDetailView
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
def allnews(request):
    posts=Post.objects.all().order_by('-publish_on')
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'tags':tags, 'editors': editors,'page_obj':page_obj}
    return render(request,'blogapp/news.html',context)
def blog(request):
    posts = Post.objects.all().order_by('-publish_on')
    posters = Poster.objects.all()
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    mainnews = MainNews.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'tags':tags, 'editors': editors,'page_obj':page_obj,'posters':posters,'mainnews':mainnews}
    return render(request,'blogapp/dashboard.html',context)

def main(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    context = {'posts': posts, 'tags':tags, 'editors': editors}
    return render(request,'blogapp/main.html',context)
def post(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    mainnews = MainNews.objects.all()
    context = {'posts': posts, 'tags':tags, 'editors': editors,'mainnews':mainnews}
    return render(request,'blogapp/dashboard.html',context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Nazwa użytkownika lub hasło są niepoprawne')
            
    context={}
    return render(request,'blogapp/loginok.html',context)
@csrf_exempt
def update_radio(request):
    post = Post.objects.all()
    tag = Tag.objects.all()
    editor = EditorProfile.objects.all()
    data = Post.objects.all()
    if request.method == 'POST':
        inp = request.POST.get('input',None)
        author = request.POST.get('author',None)
        user = User.objects.get(username=author)
        if(inp == "radio-two"):
            data = Post.objects.all().order_by()
        elif(inp == "radio-three"):
            data = Post.objects.all().order_by('-publish_on')
        else:
            data= Post.objects.all().order_by('-clicks')
            
    return render(request, 'blogapp/radio2.html',{'data':data})
        
    
@csrf_exempt
def radio_test(request,slug):
    if request.method == 'POST':
        print("readio_test")
    return render(request, 'blogapp/radio2.html')
def addcomment(request):
    if request.method == 'POST':
        print(request.POST)
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Gratulacje utworzyłeś swój profil użytkownika ' + user)
            return redirect('login')
    context={'form': form}
    return render(request,'blogapp/registerok.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
# @csrf_exempt
def radio_posts(request):
    identity = request.GET.get('id')
    author = request.GET.get('author')
    if identity == "radio-one":
        user= User.objects.get(username=author)
        posts = Post.objects.all().order_by('-clicks')
        threeposts = posts[0:3]
        result=serializers.serialize('json',threeposts,fields=('title','image','slug'))
        return JsonResponse(result,safe=False)
    if identity == "radio-two":
        user= User.objects.get(username=author)
        posts = Post.objects.filter(author=user).order_by('-publish_on')
        threeposts = posts[0:3]
        result=serializers.serialize('json',threeposts,fields=('title','image','slug'))
        return JsonResponse(result,safe=False)
    if identity == "radio-three":
        posts = Post.objects.all().order_by('-publish_on')[0:3]
        threeposts = posts[0:3]
        result=serializers.serialize('json',threeposts,fields=('title','image','slug'))
        return JsonResponse(result,safe=False)
    else:
        return None

    


@csrf_exempt
def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    post.clicks = post.clicks + 1
    post.save()
    radioposts=Post.objects.all()
    if request.method == "POST":     
        print(request.POST) 
        if 'textar' in request.POST:
            print("text area znow się ładuje")
            user = User.objects.get(username=request.user)
            text = request.POST.get("textar",None)
            print(text)
            data = {
                'post': post.id,
                'author': user.id,
                'text': text}
            form = CommentForm(data)
            if form.is_valid():
                print("form zwalidowany")
                form.save()
                
        if 'radio' in request.POST:
            print("radio znow się ładuje")
            radio = request.POST.get("input",None)
            if(radio == "radio-two"):
                radioposts=Tag.objects.all()
            elif(radio == "radio-three"):
                radioposts = EditorProfile.objects.all()
            else:
                radioposts = radioposts=Post.objects.all()
            print(radioposts)
    comments = post.comments.filter()
    posts = Post.objects.all()
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    context = {'post': post,'tags':tags,'editors':editors,'posts':posts,'comments':comments,'radioposts':radioposts}
    return render(request,'blogapp/radio2.html',context)
@csrf_exempt
def tag_detail(request,tag):
    tags = Tag.objects.get(slug=tag)
    tag_name = Tag.objects.get(slug=tag)
    posts1 = Post.objects.filter(tags=tags.id).order_by('-publish_on')
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    paginator = Paginator(posts1, 8)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts': posts, 'tags':tags, 'editors': editors,'tag_name':tag_name}
    return render(request,'blogapp/tags.html',context)

def journalist_detail(request,journalist_slug):
    journalist = EditorProfile.objects.get(slug=journalist_slug)
    posts1 = Post.objects.filter(author=journalist.user)
    paginator = Paginator(posts1, 8)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    tags = Tag.objects.all()
    editors = EditorProfile.objects.all()
    context = {'posts': posts, 'tags':tags, 'editors': editors,'journalist':journalist}
    return render(request,'blogapp/journalist.html',context)