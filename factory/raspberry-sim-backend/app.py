import json
import time
from queue import Queue
from threading import Thread

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import request


app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origins":"*"}})
api = Api(app)

q = Queue()

STEP_TIME = 2

class Order:
    def __init__(self, cpu, camera, screen, battery, speaker, mic):
        self.processor = cpu
        self.camera = camera
        self.screen = screen
        self.battery = battery
        self.speaker = speaker
        self.mic = mic


class LightColor:
    OFF = 'off'
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


class Light:
    def __init__(self):
        self.label = ''
        self.color = LightColor.OFF

    def toDict(self):
        return {"label": self.label, "color": self.color}


worker1_lights = {'light1': Light(), 'light2': Light(), 'light3': Light(), 'worker1': Light()}


class SubAssembly1(Resource):

    def get(self):
        out_json = dict()
        for key, value in worker1_lights.items():
            out_json[key] = value.toDict()
        return out_json


worker2_lights = {'light1': Light(), 'light2': Light(), 'worker2': Light()}


class SubAssembly2(Resource):

    def get(self):
        out_json = dict()
        for key, value in worker2_lights.items():
            out_json[key] = value.toDict()
        return out_json


mainline_lights = {'light1': Light(), 'light2': Light(), 'light3': Light(), 'light4': Light(), 'light5': Light(),
                   'light6': Light(), 'worker3': Light()}


class Mainline(Resource):

    def get(self):
        out_json = dict()
        for key, value in mainline_lights.items():
            out_json[key] = value.toDict()
        return out_json


@app.route('/orders', methods=['POST'])
def orders():
    if request.method == 'POST':
        data = json.loads(request.data)
        processor = 'Processor({})'.format(''.join("{}: {}".format(key, value)for key, value in data['processor'].items()))
        camera = 'Camera({})'.format(''.join("{}: {}".format(key, value)for key, value in data['camera'].items()))
        screen = 'Screen({})'.format(''.join("{}: {}".format(key, value)for key, value in data['display'].items()))
        battery = 'Battery({})'.format(''.join("{}: {}".format(key, value)for key, value in data['battery'].items()))
        speaker = 'Speaker({})'.format(''.join("{}: {}".format(key, value)for key, value in data['speaker'].items()))
        mic = 'Speaker({})'.format(''.join("{}: {}".format(key, value)for key, value in data['microphone'].items()))
        q.put(Order(processor, camera, screen, battery, speaker, mic))
        return jsonify(success=True)


api.add_resource(SubAssembly1, "/sub1")
api.add_resource(SubAssembly2, "/sub2")
api.add_resource(Mainline, "/main")


def mainloop():
    from scenario import Scenario, ScenarioWithoutCamera

    res = api.resources
    while (True):
        order = q.get()
        if 'false' in order.camera:
            scenario = ScenarioWithoutCamera(order)
        else:
            scenario = Scenario(order)
        scenario.run()


t = Thread(target=mainloop, daemon=True)
t.start()

if __name__ == '__main__':
    app.run(port=5000)
