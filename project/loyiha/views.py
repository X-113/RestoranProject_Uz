from django.shortcuts import render

# Create your views here.


def index(request):
    # backenddan frontga -> ctx uzatadi!
    # frontdan backendga -> form tagi va inputlar uzatadi!

    telefonlar = [
        {"name":"samsung",
         "color":"red"
        },
        {"name":"iphone",
         "color":"#484848"
        },
        {"name":"redmi",
         "color":"navy"
        },
        {"name":"xiaomi",
         "color":"black"
        },
        {"name":"huawei",
         "color":"darkred"
        },
        {"name":"oppo",
         "color":"green"
        }



    ]

    ctx = {
        "title":"Ma'lumotlarni uzatish Frontendga",
        "ism":"SAMANDARBEK",
        "familiya":"IBODULLAYEV",
        "tel":"Telefon markalari:",
        "telefon":telefonlar,
        "background":"silver"

    }
    return render(request,"index.html", ctx)




