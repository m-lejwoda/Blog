from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'choose_3_articles', views.Choose3Articles, basename='choose_3_articles')
urlpatterns = router.urls