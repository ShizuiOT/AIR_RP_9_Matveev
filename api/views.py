from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Software
from .serializers import SoftwareSerializer
from db_save.func import getSoftware, addSoftware
from drf_spectacular.utils import extend_schema


class getSoftwareView(APIView):
    @extend_schema(request=SoftwareSerializer, responses=SoftwareSerializer)
    def get(self, request, Discipline, OpSys, Name, Practicum_Num):
        conference = getSoftware(Discipline, OpSys, Name, Practicum_Num)
        print(conference)
        conference = (SoftwareSerializer(instance=st).data for st in conference) if conference is not None else []

        return Response(conference)

class AddSoftwareView(APIView):
    @extend_schema(request=SoftwareSerializer, responses=SoftwareSerializer)
    def get(self, request, Discipline, OpSys, Name, Practicum_Num):
        conference = addSoftware(Discipline, OpSys, Name, Practicum_Num)
        return Response(conference)