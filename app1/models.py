from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=56)
    type = models.CharField(max_length=128, choices=[
        ("milliy","Milliy taomlar"),
        ("ichimlik","Salqin ichimliklar"),
        ("kofe","Coffee"),
        ("salat","Salatlar"),
        ("desert","Shirinliklar"),
        ("fast","Fast Food")
    ])

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"




class Ovqat(models.Model):
    nomi = models.CharField(max_length=256)
    tarkibi = models.TextField() # uzunligi cheksiz bo'lgan charfield
    narxi = models.PositiveIntegerField()
    image = models.ImageField()
    kaloriya = models.IntegerField(default=250, verbose_name="Kaloriya(Kkal)")
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Ovqat"
        verbose_name_plural = "Ovqatlar"


