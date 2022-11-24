from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from db_save.func import *


def index(request):
    return HttpResponse("Hello Vladimir")


def ReqgetSoftware(request):
    Discipline = request.GET.get("Discipline")
    OpSys = request.GET.get("OpSys")
    Name = request.GET.get("Name")
    Practicum_Num = request.GET.get("Practicum_Num")
    software = getSoftware(Discipline, OpSys, Name, Practicum_Num)
    print(software)
    return HttpResponse(
        (f"ID ПО: {obj['id']} - Дисциплина: {obj['Discipline']}, ОС: {obj['OpSys']}, Название: {obj['Name']}, "
         f"Номер практики: {obj['Practicum_Num']}<br>" for obj in software)
        if len(software) else f"ПО не существует в базе")


def ReqsetSoftware(request):
    Discipline = request.GET.get("Discipline")
    OpSys = request.GET.get("OpSys")
    Name = request.GET.get("Name")
    Practicum_Num = request.GET.get("Practicum_Num")
    software = addSoftware(Discipline, OpSys, Name, Practicum_Num)
    return HttpResponse(
        (f"ПО с данными: ID ПО: {software['id']} - Дисциплина: {software['Discipline']}, ОС: {software['OpSys']}, "
         f"Название: {software['Name']}, Номер практики: {software['Practicum_Num']}<br>"))

