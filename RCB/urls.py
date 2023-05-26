from django.urls import path
from RCB.views import*
app_name='king'
urlpatterns=[
    path('ipl/',ipl,name='ipl'),

]