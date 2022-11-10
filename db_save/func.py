from .models import *
def addSoftware (Discipline, OpSys, Name, Practicum_Num):
    software = Software(Discipline=Discipline, OpSys=OpSys, Name=Name, Practicum_Num=Practicum_Num)
    software.save()
    return software

def getSoftware (Discipline, OpSys, Name, Practicum_Num):
    software = Software.objects.filter(Discipline__icontains=Discipline)\
               & Software.objects.filter(OpSys__icontains=OpSys) & \
               Software.objects.filter(Name__icontains=Name) & \
               Software.objects.filter(Practicum_Num__icontains=Practicum_Num)
    return software
