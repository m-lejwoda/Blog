from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'choose_3_articles', views.Choose3Articles, basename='choose_3_articles')
router.register(r'load_more_articles', views.LoadMoreArticles, basename='load_more_articles')
urlpatterns = router.urls
