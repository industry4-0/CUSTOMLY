from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
import collections
# Create your models here.


class Component(models.Model):
    componentType = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    attributes = JSONField(default="{}")

    def __str__(self):
        return self.name


class OrdersManager(models.Manager):
    def create_order(self, name, completed,hash):
        order = self.create(name=name,
                            completed=completed,orderHash=orderHash)
        # do something with the book
        return order


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=30)
    components = models.ManyToManyField(Component, blank=False)
    orderHash = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    objects = OrdersManager()

    def __str__(self):
        return self.name
