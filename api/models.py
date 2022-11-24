from django.db import models


class Software:
    def __init__(self, Discipline, OpSys, Name, Practicum_Num):
        self.Discipline = Discipline
        self.OpSys = OpSys
        self.Name = Name
        self.Practicum_Num = Practicum_Num