from django.shortcuts import render

# Create your views here.

#importando os módulos e classes necessárias para criar uma api
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

#
class UserViewSet(viewsets.ModelViewSet): # a classe GroupViewSet, herda viewsets.ModelViewSet.
    """
    Endpoint da API que permite que os usuários sejam visualizados ou editados.
    """
    queryset = User.objects.all().order_by('-date_joined') # pega todos os objetos User, ordenados pela data de entrada (date_joined) em ordem decrescente, para que os usuários mais recentes apareçam primeiro. 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] #garante que apenas usuários autenticados tenham acesso a esta API.


class GroupViewSet(viewsets.ModelViewSet):
    '''
    Endpoint da API que permite que os grupos sejam visualizados ou editados..
    '''
    queryset = Group.objects.all() #pega todos os objetos Group
    serializer_class = GroupSerializer #serializador a ser usado é o GroupSerializer
    permission_classes = [permissions.IsAuthenticated] # garante que apenas usuários autenticados tenham acesso a esta API.