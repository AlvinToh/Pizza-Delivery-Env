from django.contrib import admin
from django.urls import path
from .views import adminloginview, authenticateadmin, adminhomepageview, adminlogout, addpizza, deletepizza, homepageview, signupuser

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', adminlogout),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('', homepageview, name='homepage'),
    path('signupuser/', signupuser)
]
