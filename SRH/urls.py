from django.urls import path
from SRH.views import*
app_name='charan'
urlpatterns=[
    path('ipl2/',ipl2,name='ipl2'),

]