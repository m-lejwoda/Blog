from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    # path('search/', include('haystack.urls')),
    path('api/v1/', include('blogapp.api.v1.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),

]

urlpatterns += [
    path('', include('cms.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)