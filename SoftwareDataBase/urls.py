from api.urls import path, include
from django.contrib import admin
from django.urls import path, include
from db_save import views
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('QuerryDB/', include('db_show.urls')),
    path('api/', include('api.urls')),
    path("docs/", SpectacularAPIView.as_view(url_name="schema"), name="swagger-ui")
]
