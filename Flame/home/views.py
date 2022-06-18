from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads

from home.models import Artigo

# Create your views here.
def index(request):
	return render(request,'index.html')
	
def lista(request):
	#b = Artigo(resumo='Esse artigo é um teste', resume='This paper is a test', autor='Richard Fernandes', titulo='Teste', palavraschave='teste, artigo', direitosdeuso='Livre', local='UFVJM', datapubli=datetime.date(2022, 6, 13), Doe='sei lá', Revista='FDS')
	#b.save()
	tudo={"art": Artigo.objects.all(), 
			"N": len(Artigo.objects.all())}
	
	return render(request,'lista.html', tudo)
	
def adicionar(request):
	return render(request,'add.html')
	
@csrf_exempt
def add(request):
	if request.method == "POST":
		titulo = request.POST['titulo']
		resumo = request.POST['resumo']
		resume = request.POST['resume']
		autor = request.POST['autor']
		chaves = request.POST['palavraschave']
		direitos = request.POST['direitosdeuso']
		local = request.POST['local']
		datab = request.POST['datapubli']
		doe = request.POST['doe']
		revista = request.POST['revista']
		data = Artigo(titulo=titulo, resumo=resumo, resume=resume, autor=autor, palavraschave=chaves, direitosdeuso=direitos, local=local, datapubli=datab, Doe=doe, Revista=revista)
		data.save()
		return render(request, 'add.html')

@csrf_exempt
def edit(request):
    if request.method == "POST":
	    try:
	    	note_edit = loads(request.body)
	    	artigo = Artigo.objects.get(id=note_edit["id"])
	    	artigo.titulo = note_edit["titulo"]
	    	artigo.resumo = note_edit["resumo"]
	    	artigo.save()
	    	return JsonResponse({"status": 0})
	    except:
	    	return JsonResponse({"status": 1})
