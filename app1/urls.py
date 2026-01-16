from django.urls import path
from .views import index,ctg_qosh,ovqat


urlpatterns = [
    path('',index,name='home'),
    path('ctg/',ctg_qosh, name='ctg'),
    path('food/',ovqat, name='food')
]


