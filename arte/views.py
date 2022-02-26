from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect

import arte
from .models import Arte, Comentario, Tags
from .forms import FormPublicar
from PIL import Image
from django.db.models import Q, Value
from django.db.models.functions import Concat

from arte import models

# Create your views here.

@login_required
def PublicarArte(request):

    if request.method == "GET":
        form = FormPublicar()
        tag_hl = Tags.nome
        contexto = {
            'form': form,
            'tag_hl': tag_hl,
        }
        return render(request, 'arte/publicar_arte.html', context=contexto)

    else:
        form = FormPublicar(request.POST, request.FILES)

        if form.is_valid(): 
            form.instance.user = request.user
            arte = form.save()
            tags_provs = request.POST['tag_hl']
            lista_tags = tags_provs.split(sep=' ')

            for texto in lista_tags:
                tags_prov = None
                try:
                    tags_prov = Tags.objects.get(nome=texto)
                except Tags.DoesNotExist:
                    tags_prov = Tags(nome=texto)
                    tags_prov.save()

                arte.tags.add(tags_prov)
        

            form = FormPublicar()

        contexto = {
            'form': form
        }

        return render(request, 'arte/publicar_arte.html', context=contexto)


def ListarArte(request):
    TodasArtes = Arte.objects.all()
    TodasTags = Tags.objects.all()

    contexto = {
        'TodasArtes': TodasArtes,
        'TodasTags': TodasTags
    }

    return render(request, 'arte/listar_arte.html', context=contexto)


def busca(request):
    termonome = request.GET.get('termonome')
    termoprecomin = request.GET.get('termoprecomin')
    termoprecomax = request.GET.get('termoprecomax')

    campos = Concat('nome', Value(' '), 'nome', Value(
        ' '), 'nome', Value(' '), 'nome', Value(' '), 'nome')

    contexto = {}

    if (termoprecomin is None or not termoprecomin) or (termoprecomax is None or not termoprecomax):
        if termonome is None or not termonome:
            return render(request, 'arte/busca.html', context=contexto)

        TodasArtes = Arte.objects.annotate(
            nome_completo=campos
        ).filter(nome_completo__icontains=termonome)

        contexto = {
            'TodasArtes': TodasArtes,
        }
        return render(request, 'arte/busca.html', context=contexto)

    TodasArtes = Arte.objects.annotate(
        nome_completo=campos
    ).filter(Q(nome_completo__icontains=termonome) & Q(Q(preco__gte=termoprecomin) & Q(preco__lte=termoprecomax)))

    contexto = {
        'TodasArtes': TodasArtes,
    }
    return render(request, 'arte/busca.html', context=contexto)

def DetalharArte(request, slug):
    
    artedetalhe = Arte.objects.get(slug=slug)
    idarte = artedetalhe.id
    todoscomentarios = Comentario.objects.all()
    print(todoscomentarios)
    contexto = {
        'artedetalhe': artedetalhe,
        'todoscomentarios': todoscomentarios
    }
    return render(request, 'arte/detalhar_arte.html',context=contexto)

def AdicionarCarrinho(request):
    pass
    
    return render(request, 'arte/adicionar_carrinho.html')