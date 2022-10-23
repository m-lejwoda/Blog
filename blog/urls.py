from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),

]

urlpatterns += [
    path('', include('cms.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)