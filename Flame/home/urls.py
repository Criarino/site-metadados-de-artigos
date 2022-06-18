from django.urls import path

from . import views

urlpatterns = {
	path('', views.index),
	path('lista.html', views.lista),
	path('index.html', views.index),
	path('add.html', views.adicionar),
	#path('delete/', views.delete, name='delete'),
	path('add/', views.add, name='add')
}
