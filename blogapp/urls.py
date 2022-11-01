from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/<slug:slug>/',  views.SingleArticleView.as_view(), name='post_detail'),
    # path('post/<slug:slug>/',  views.post_detail, name='post_detail'),
    path('schedule/', views.schedule, name='schedule_detail'),
    path('tags/<slug:tag>/', views.TagView.as_view(), name='tag_detail'),
    path('journalist/<str:journalist_slug>/', views.journalist_detail,name='journalist_detail'),
    # path('radio/', views.update_radio, name="radio"),
    # path('radio2/', views.radio_test, name="radio2"),
    path('radioposts/', views.radio_posts, name="radio_posts"),
    path('news/', views.allnews, name="news"),

]