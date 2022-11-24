from django.urls import path, include
from . import views

urlpatterns = [
    path('getSoftwareView/<str:Discipline>/<str:OpSys>/<str:Name>/<str:Practicum_Num>',
         views.SoftwareView.as_view(), name="Getter"),
    path('setSoftwareView/<str:Discipline>/<str:OpSys>/<str:Name>/<str:Practicum_Num>',
         views.SoftwareView.as_view(), name="Setter")
]