from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('orders', views.OrdersView)
router.register('components', views.ComponentView)
# router.register('ordersAll', views.OrdersAllView)


urlpatterns = [
    path('', include(router.urls)),
]
