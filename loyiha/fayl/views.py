from django.shortcuts import render,HttpResponse

# Create your views here.
# Asosiy funksiyalar yoziladigan joy!!! #views.py!

def index(request):
    return HttpResponse("""
<html>
<head>
    <title>Django Sayt</title>
</head> 
<body style='
    background-image: url(https://plus.unsplash.com/premium_photo-1681400783826-8ae188a981b7?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Z2FtZSUyMGJhY2tncm91bmR8ZW58MHx8MHx8fDA%3D);
    background-position: absolute;
    background-size: cover;
'>
    <h1 style='color:blue;'>FLASH UP</h1>   
    <h1 style='color:green;'>FLASH UP ENERGY ORIGINAL</h1>
    <h1 style='color:red;'>FLASH UP ENERGY ORIGINAL</h1>
    <h1 style='color:blue;'>FLASH UP ENERGY ORIGINAL</h1>
    <h1 style='color:yellow;'>FLASH UP ENERGY ORIGINAL</h1>
    <h1 style='color:green;'>FLASH UP ENERGY ORIGINAL</h1>        
</body>
</html>
    
    """)











