from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'choose_3_articles', views.Choose3Articles, basename='choose_3_articles')
urlpatterns = router.urls
# urlpatterns = [
#     path('choose_3_articles/', views.Choose3Articles.as_view(), name="choose_3_articles"),
# ]