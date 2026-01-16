from django.db import models

# Create your models here.
# SQL -> Strukturalangan So'rovlar Tili | jadvallardan iborat!
# ORM -> Object Relational Mapping-(Python codelari yordamida baza yarata olamiz)


class Maktab(models.Model):
    soni = models.IntegerField()
    xususiymi = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.soni}-maktab"



class Oquvchi(models.Model):
    ism = models.CharField(max_length=56)
    yosh = models.PositiveIntegerField()    #intejerfield minusliklarni ham qo'shib oladi.
    kasb = models.CharField(max_length=128, choices=[
        ("dasturchi","Dasturchi"),
        ("kassir", "Hisobchi"),
        ("sotuvchi", "Sotuvchi"),
        ("injener", "Muhandis"),
    ])
    pul = models.BigIntegerField(default=0)
    bitirgan = models.BooleanField(default=False)
    tugulgan_sana = models.DateField()
    maktab = models.ForeignKey(Maktab, on_delete=models.DO_NOTHING, null=True, blank=True)         #OneToOneField(bittaga bitta), #OneToManyField(bittagako'p), #ManyToManyField(kopga kop)

    #To'ldirilgan vaqt:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ism} | {self.yosh}-yoshda | {self.maktab.soni}-maktab o'quvchisi "


# Restoran ORMda qilingan ishlar:


class Restoran(models.Model):
    nomi = models.CharField(max_length=100)
    manzil = models.CharField(max_length=200)
    telefon = models.CharField(max_length=20)

    def __str__(self):
        return self.nomi


class Mijoz(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20, unique=True)
    manzil = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.ism


class Xodim(models.Model):
    ism = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50,choices=[
        ('manager', 'Boshqaruvchi'),
        ('admin', 'Administrator'),
        ('oshpaz', 'Oshpaz'),
        ('yordamchi', 'Yordamchi oshpaz'),
        ('afitsant', 'Ofitsiant'),
        ('barmen', 'Barmen'),
        ('pazanda', 'Pazanda (shirinliklar)'),
        ('cleaner', 'Tozalovchi'),
        ('security', 'Xavfsizlik xodimi'),
        ('hisobchi', 'Kassir'),
        ('delivery', 'Yetkazib beruvchi'),
    ])
    ish_haqi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ism} ({self.lavozim})"


class Taom(models.Model):
    nomi = models.CharField(max_length=100, choices=[
        # Milliy taomlar
        ('osh', 'Osh (Palov)'),
        ('somsa', 'Somsa'),
        ('lagmon', 'Lag‘mon'),
        ('shorva', 'Sho‘rva'),
        ('manti', 'Manti'),
        ('norin', 'Norin'),

        # Fast Food
        ('burger', 'Burger'),
        ('pitsa', 'Pitsa'),
        ('hotdog', 'Hot-dog'),
        ('lavash', 'Lavash'),
        ('shaurma', 'Shaurma'),

        # Salatlar
        ('achichuq', 'Achchiq salat'),
        ('olivye', 'Olivye'),
        ('sezar', 'Sezar salat'),
        ('vitamin', 'Vitamin salat'),

        # Ichimliklar
        ('choy', 'Choy (qora/yashil)'),
        ('qatiq', 'Qatiq'),
        ('sharbat', 'Sharbat (olma, uzum, apelsin)'),
        ('cola', 'Cola'),
        ('qahva', 'Qahva (espresso, latte, cappuccino)'),
        ('suv', 'Mineral suv'),

        # Desertlar
        ('tort', 'Tort (Napoleon, Medovik)'),
        ('muzqaymoq', 'Muzqaymoq'),
        ('chakchak', 'Chak-chak'),
        ('shakarob', 'Shakarob mevalar bilan'),
        ('pirog', 'Qaymoqli pirog')

    ])
    kategoriya = models.CharField(max_length=50, choices=[
        ('milliy', 'Milliy taomlar'),
        ('fastfood', 'Fast Food'),
        ('ichimlik', 'Ichimliklar'),
        ('desert', 'Shirinliklar (Desertlar)'),
        ('salat', 'Salatlar'),
        ('asosiy', 'Asosiy taomlar')

    ])   # masalan: Milliy taom, Ichimlik
    narx = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nomi} - {self.narx} so'm"


class Stol(models.Model):
    raqami = models.IntegerField(unique=True)
    status = models.CharField(max_length=20, choices=[('bo\'sh', 'Bo\'sh'), ('band', 'Band')], default="bo'sh")

    def __str__(self):
        return f"Stol {self.raqami} ({self.status})"


class Buyurtma(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    stol = models.ForeignKey(Stol, on_delete=models.SET_NULL, null=True, blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    umumiy_summa = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.mijoz.ism}"


class BuyurtmaTafsilot(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE, related_name="tafsilotlar")
    taom = models.ForeignKey(Taom, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.taom.nomi} x {self.miqdor}"











