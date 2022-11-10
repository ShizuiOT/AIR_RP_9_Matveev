from django.db import models

class Software(models.Model):
    Discipline = models.TextField()
    OpSys = models.TextField()
    Name = models.TextField()
    Practicum_Num = models.TextField()
