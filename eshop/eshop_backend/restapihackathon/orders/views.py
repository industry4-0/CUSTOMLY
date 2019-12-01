from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Component
from .serializers import OrderSerializer, ComponentSerializer, OrdersAllSerializer

# Create your views here.


class OrdersView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ComponentView(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class OrdersAllView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersAllSerializer
