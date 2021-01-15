from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Produtos
from .serializers import ProdutosSerializer


class ListaProdutosView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer