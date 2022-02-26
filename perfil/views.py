from perfil.forms import RegistrationForm
import perfil
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login as loginn
from .models import Arte
# Create your views here.

def Registrar(request):
    form = RegistrationForm()
    if request.method != 'POST': 
        
        contexto = {
                'form': form,
            }
        return render(request, 'perfil/registrar.html', context=contexto)
    
    form = RegistrationForm(request.POST)

    if form.is_valid():
       
        form.save()
        termo = request.POST['username']
        tipo = request.POST['tipoconta']
        
        if tipo == 'Artista':
            grupo = get_object_or_404(Group, name='Artista')

        else:
            grupo = get_object_or_404(Group, name='Comprador')
       
            
        user =  User.objects.get(username=termo)
        user.groups.add(grupo)

        
    form = RegistrationForm()
    contexto = {
                'form': form,
            }
    
    return render(request, 'perfil/registrar.html', context=contexto)



def Login(request):
    form = AuthenticationForm()
    contexto ={
        'form':form,
    }


    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            loginn(request,user)
            return redirect('listar_arte')
    
    form = AuthenticationForm()
    contexto ={
        'form':form,
    }
    return render(request, 'perfil/login.html',context=contexto)


def logoff(request):
    logout(request)
    return redirect('listar_arte')



def minhasArtes(request):
    usuario = request.user
    print(usuario)
    myartes = Arte.objects.filter(user=usuario)
    print(myartes)

    contexto = {
        'myartes': myartes,
  
    }

    return render(request, 'perfil/perfil.html', context=contexto)
