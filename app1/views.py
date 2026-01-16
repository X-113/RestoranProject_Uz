from django.shortcuts import render
from .models import Ovqat,Category
from .forms import CategoryForm, OvqatForm


# Create your views here.

def index(request):
    ovqatlar = Ovqat.objects.all()

    ctx = {
        "ovqatlar": ovqatlar
    }
    return render(request,'index.html',ctx)

def ctg_qosh(request):
    # ctx-backdan frontga | form-> frontdan backga | frontdan kirgan ma'lumotlar -> request.POST kirib keladi ma'lumotlar
    ctx = {}

    if request.POST:
        form = CategoryForm(request.POST) # Frontdan kelayotganini bazaga yuborarkan
        # print("\n\nFrontdan malumot kelyabdi", request.POST)
        if form.is_valid():   # bazaga mosmi? tekshiradi.
            form.save()     # bazaga saqlaydi
            ctx['success'] = "Categoriya Muvaffaqiyatli qo'shildi"
        else:
            ctx['error'] = form.errors  # kamchilikni ko'rsatadi

    return render(request, "ctg.html", ctx)



def ovqat(request):
    ctx = {
        "ctgs":Category.objects.all()
    }

    if request.POST:
        form = OvqatForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            ctx['success'] = "Ovqat muvaffaqiyatli qo'shildi"
        else:
            ctx['error'] = form.errors




    return render(request, 'food.html', ctx)

