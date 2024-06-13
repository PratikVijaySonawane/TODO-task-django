from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',signout,name='logout'),
    path('addtodo/',addtodo,name='addtodo'),
    path('deletetodo/<int:id>',deletetodo,name='deletetodo'),
    path('changestatus/<int:id>/<str:status>',changetodo,name='changetodo'),
]