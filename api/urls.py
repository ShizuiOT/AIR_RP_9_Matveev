from django.urls import path
from . import views

urlpatterns = [
    path('getSoftwareView/<str:Disciline>/<str:OpSys>/<str:Name>/<str:Practicum_Num>',
         views.SoftwareView.as_view(), name="Getter"),
    path('setSoftwareView/<str:Disciline>/<str:OpSys>/<str:Name>/<str:Practicum_Num>',
         views.SoftwareView.as_view(), name="Setter")
]