# Os serializers são responsáveis por converter os dados complexos,
#como conjuntos de consultas e instâncias de modelo, em um formato legível por outras aplicações, geralmente JSON ou XML.
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']