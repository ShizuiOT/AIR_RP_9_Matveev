from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Software
from .serializers import SoftwareSerializer
from db_save.func import getSoftware, addSoftware

class SoftwareView(APIView):



    def get(self, request, Discipline, OpSys, Name, Practicum_Num):

        a = getSoftware(Discipline, OpSys, Name, Practicum_Num)
        print(a)
        a = (SoftwareSerializer(instance=st).data for st in a) if a is not None else []

        return Response(a)


    def set(self, request, Discipline, OpSys, Name, Practicum_Num):

        a = addSoftware(Discipline, OpSys, Name, Practicum_Num)
        a.Discipline = SoftwareSerializer(instance=a.Discipline).data
        a.OpSys = SoftwareSerializer(instance=a.OpSys).data
        a.Name = SoftwareSerializer(instance=a.Name).data
        a.Practicum_Num = SoftwareSerializer(instance=a.Practicum_Num).data
