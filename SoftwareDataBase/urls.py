from api.urls import path, include
from django.contrib import admin
from django.urls import path, include
from db_save import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('QuerryDB/', include('db_show.urls')),
    path('api/', include('api.urls')),
]
