from django.urls import path
from contatos.views import index, det_contato


urlpatterns = [
    path('', index),
    path('contato', det_contato, name='contato')
    
]
