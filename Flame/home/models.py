from django.db import models

# Create your models here. São modelos de dados, representações do db

class Artigo(models.Model):
	resumo=models.CharField(max_length=2000)
	resume=models.CharField(max_length=2000)
	autor=models.CharField(max_length=100)
	titulo=models.CharField(max_length=200)
	palavraschave=models.CharField(max_length=100)
	direitosdeuso=models.CharField(max_length=100)
	local=models.CharField(max_length=100)
	datapubli=models.DateField()
	Doe=models.CharField(max_length=50)
	Revista=models.CharField(max_length=50)
