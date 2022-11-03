from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/<slug:slug>/',  views.SingleArticleView.as_view(), name='post_detail'),
    path('archival_schedule/', views.ArchivalScheduleView.as_view(), name='archival_schedule'),
    path('upcoming_schedule/', views.UpcomingScheduleView.as_view(), name='upcoming_schedule'),
    # path('schedule/', views.schedule, name='schedule_detail'),
    path('tags/<slug:tag>/', views.TagView.as_view(), name='tag_detail'),
    path('journalist/<slug:slug>/', views.JournalistDetailView.as_view(),name='journalist_detail'),
    path('radioposts/', views.radio_posts, name="radio_posts"),
    path('news/', views.AllNewsView.as_view(), name="news"),

]