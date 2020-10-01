from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.blog, name='index'),
    path('login/',views.loginPage, name='login'),
    path('register/',views.registerPage, name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('post/<slug:slug>/',views.post_detail,name='post_detail'),
    path('tags/<str:tag>/',views.tag_detail,name='tag_detail'),
    path('journalist/<str:journalist_slug>/',views.journalist_detail,name='journalist_detail'),
    path('radio/',views.update_radio,name="radio"),
    path('radio2/',views.radio_test,name="radio2"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    
    
]