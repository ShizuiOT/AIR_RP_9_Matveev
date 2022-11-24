from django.urls import path, include
from . import views
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('getSoftwareView/<str:Discipline>/<str:OpSys>/<str:Name>/<str:Practicum_Num>',
         views.SoftwareView.as_view(), name="Getter"),
    path('setSoftwareView/<str:Discipline>/<str:OpSys>/<str:Name>/<str:Practicum_Num>',
         views.SoftwareView.as_view(), name="Setter"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]