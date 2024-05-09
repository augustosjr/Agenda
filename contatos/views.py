from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
# Create your views here.



def index(request):
    return render(request, 'contatos/index.html')
    
def det_contato(request):
    return render(request, 'contatos/det_contato.html')