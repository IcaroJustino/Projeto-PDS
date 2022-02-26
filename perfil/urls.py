from django.urls import path
from . import views


urlpatterns = [
    path('registrar/', views.Registrar, name='registrar'),
    path('login/', views.Login, name='login'),
    path('logoff/', views.logoff, name='logoff'),
    path('minhasartes/', views.minhasArtes, name='minhasartes'),
    
    

]
