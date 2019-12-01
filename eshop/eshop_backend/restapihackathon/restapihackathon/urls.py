"""restapihackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from orders.models import Order

import time
import json
from threading import Thread
from web3 import Web3
import urllib.parse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    # path('api/token', TokenObtainPairView.as_view()),
    # path('api/token/refresh', TokenObtainPairView.as_view())
]



def my_callback(event):
    urldecodedorder = urllib.parse.unquote(event['args']['phoneConfig'])
    # order = Order.objects.create_order("dshjvhjd", "3")
    jsonorder = json.loads(urldecodedorder)
    # print(jsonorder['battery']['capacity'])
    order = Order.objects.create_order("Hackathon", "test")
    order.components.add(jsonorder['battery']['capacity'], jsonorder['display']['size'], jsonorder['processor']['model'])
    order.user.add(2)


def one_time():
    # obj= Order.objects.filter(id).order_by('-id')[0]
    # print(obj)
    websocket_provider=Web3.WebsocketProvider('ws://172.16.176.19:8544')
    w3=Web3(websocket_provider)
    abi=json.loads("""[
        {
            "constant": false,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "orderId",
                    "type": "uint32"
                }
            ],
            "name": "cancelOrder",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": false,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "orderId",
                    "type": "uint32"
                }
            ],
            "name": "completeOrder",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": false,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "clientId",
                    "type": "uint32"
                },
                {
                    "internalType": "string",
                    "name": "phoneConfig",
                    "type": "string"
                }
            ],
            "name": "newOrder",
            "outputs": [
                {
                    "internalType": "uint32",
                    "name": "orderId",
                    "type": "uint32"
                }
            ],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": false,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "orderId",
                    "type": "uint32"
                }
            ],
            "name": "startOrder",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "uint32",
                    "name": "orderId",
                    "type": "uint32"
                },
                {
                    "indexed": true,
                    "internalType": "uint32",
                    "name": "clientId",
                    "type": "uint32"
                },
                {
                    "indexed": false,
                    "internalType": "string",
                    "name": "phoneConfig",
                    "type": "string"
                }
            ],
            "name": "OrderReceived",
            "type": "event"
        },
        {
            "constant": true,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "",
                    "type": "uint32"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "clientOrders",
            "outputs": [
                {
                    "internalType": "uint32",
                    "name": "",
                    "type": "uint32"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [],
            "name": "testDeployment",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "pure",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "clientId",
                    "type": "uint32"
                }
            ],
            "name": "viewClientOrders",
            "outputs": [
                {
                    "internalType": "uint32[]",
                    "name": "",
                    "type": "uint32[]"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [
                {
                    "internalType": "uint32",
                    "name": "orderId",
                    "type": "uint32"
                }
            ],
            "name": "viewOrder",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ]""")
    contract=w3.eth.contract(
        address = '0xC2E05aE483580E93CdCfd5555921C8eEA7f253f1', abi = abi)

    event_filter=contract.events.OrderReceived.createFilter(
        fromBlock = 0)
    while True:
        for event in event_filter.get_new_entries():
            my_callback(event)

        time.sleep(1)


thread=Thread(target = one_time)
thread.start()
