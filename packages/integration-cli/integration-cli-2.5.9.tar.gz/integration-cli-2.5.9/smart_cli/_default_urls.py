from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls
from api.base_views import HomeAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('api/', HomeAPIView.as_view(), name="home"),
]
