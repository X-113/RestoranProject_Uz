from django.db import models

# Create your models here.

class Xona(models.Model):
    nomi = models.CharField(max_length=24)
    type = models.CharField(choices=[
        ("oddiy", "Standart Xona"),
        ("vip", "VIP Xona"),
        ("ps5", "PlayStation Xona"),
        ("programming", "Dasturchilar xonasi")
    ])
    son = models.SmallIntegerField("Ichidagi Maksimall Kompyuterlar soni")


class Texnika(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(choices=[
        ("nout","Noutbuk"),
        ("pc","Kompyuter"),
        ("ps","PlayStation"),
    ])
    xarakter = models.JSONField(default=dict)
    status = models.CharField("Holati", choices=[
        ("band", "Band qilingan"),
        ("bosh", "Foydalanish uchun ochiq"),
        ("repair", "Texnik nasos"),
    ])
