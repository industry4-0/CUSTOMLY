import time

from app import worker1_lights, worker2_lights, mainline_lights, LightColor, STEP_TIME


class Scenario:

    def __init__(self, order):
        self.order = order

    def run(self):
        time.sleep(4.5)
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        self.step6()
        self.step7()
        self.step8()
        self.step9()
        self.step10()
        self.step11()
        self.step12()
        self.step13()
        self.step14()
        self.step15()

    def step1(self):
        self.reset()
        print("Step {}".format(1))
        worker1_lights['worker1'].color = LightColor.RED
        worker1_lights['light1'].color = LightColor.YELLOW
        worker1_lights['light2'].color = LightColor.YELLOW
        worker1_lights['light3'].color = LightColor.OFF
        worker2_lights['light1'].color = LightColor.YELLOW
        worker2_lights['light2'].color = LightColor.YELLOW
        worker2_lights['worker2'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step2(self):
        self.reset()
        print("Step {}".format(2))
        worker1_lights['worker1'].color = LightColor.RED
        worker1_lights['light1'].color = LightColor.RED
        worker1_lights['light2'].color = LightColor.RED
        worker1_lights['light3'].color = LightColor.OFF
        worker2_lights['light1'].color = LightColor.RED
        worker2_lights['light2'].color = LightColor.RED
        worker2_lights['worker2'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step3(self):
        self.reset()
        print("Step {}".format(3))
        worker1_lights['worker1'].color = LightColor.RED
        worker1_lights['light1'].color = LightColor.GREEN
        worker1_lights['light2'].color = LightColor.GREEN
        worker1_lights['light3'].color = LightColor.YELLOW
        worker2_lights['light1'].color = LightColor.GREEN
        worker2_lights['light2'].color = LightColor.GREEN
        worker2_lights['worker2'].color = LightColor.GREEN
        time.sleep(STEP_TIME)

    def step4(self):
        self.reset()
        print("Step {}".format(4))
        worker1_lights['worker1'].color = LightColor.RED
        worker1_lights['light1'].color = LightColor.RED
        worker1_lights['light2'].color = LightColor.GREEN
        worker1_lights['light3'].color = LightColor.RED
        worker2_lights['light1'].color = LightColor.OFF
        worker2_lights['light2'].color = LightColor.OFF
        worker2_lights['worker2'].color = LightColor.OFF
        mainline_lights['light1'].color = LightColor.YELLOW
        mainline_lights['light2'].color = LightColor.YELLOW
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step5(self):
        self.reset()
        print("Step {}".format(4))
        worker1_lights['worker1'].color = LightColor.GREEN
        worker1_lights['light1'].color = LightColor.GREEN
        worker1_lights['light2'].color = LightColor.GREEN
        worker1_lights['light3'].color = LightColor.GREEN
        mainline_lights['light1'].color = LightColor.RED
        mainline_lights['light2'].color = LightColor.RED
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step6(self):
        self.reset()
        print("Step {}".format(6))
        mainline_lights['light1'].color = LightColor.GREEN
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.YELLOW
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step7(self):
        self.reset()
        print("Step {}".format(7))
        mainline_lights['light1'].color = LightColor.RED
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.RED
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step8(self):
        self.reset()
        print("Step {}".format(8))
        mainline_lights['light1'].color = LightColor.GREEN
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.GREEN
        mainline_lights['light4'].color = LightColor.YELLOW
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step9(self):
        self.reset()
        print("Step {}".format(9))
        mainline_lights['light1'].color = LightColor.RED
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.RED
        mainline_lights['light4'].color = LightColor.RED
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step10(self):
        self.reset()
        print("Step {}".format(10))
        mainline_lights['light1'].color = LightColor.GREEN
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.GREEN
        mainline_lights['light4'].color = LightColor.GREEN
        mainline_lights['light5'].color = LightColor.YELLOW
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step11(self):
        self.reset()
        print("Step {}".format(11))
        mainline_lights['light1'].color = LightColor.RED
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.GREEN
        mainline_lights['light4'].color = LightColor.GREEN
        mainline_lights['light5'].color = LightColor.RED
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step12(self):
        self.reset()
        print("Step {}".format(12))
        mainline_lights['light1'].color = LightColor.GREEN
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.GREEN
        mainline_lights['light4'].color = LightColor.GREEN
        mainline_lights['light5'].color = LightColor.GREEN
        mainline_lights['light6'].color = LightColor.YELLOW
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step13(self):
        self.reset()
        print("Step {}".format(13))
        mainline_lights['light1'].color = LightColor.RED
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.GREEN
        mainline_lights['light4'].color = LightColor.GREEN
        mainline_lights['light5'].color = LightColor.GREEN
        mainline_lights['light6'].color = LightColor.RED
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step14(self):
        self.reset()
        print("Step {}".format(14))
        mainline_lights['light1'].color = LightColor.GREEN
        mainline_lights['light2'].color = LightColor.GREEN
        mainline_lights['light3'].color = LightColor.GREEN
        mainline_lights['light4'].color = LightColor.GREEN
        mainline_lights['light5'].color = LightColor.GREEN
        mainline_lights['light6'].color = LightColor.GREEN
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step15(self):
        self.reset()
        print("Step {}".format(15))
        mainline_lights['light1'].color = LightColor.OFF
        mainline_lights['light2'].color = LightColor.OFF
        mainline_lights['light3'].color = LightColor.OFF
        mainline_lights['light4'].color = LightColor.OFF
        mainline_lights['light5'].color = LightColor.OFF
        mainline_lights['light6'].color = LightColor.OFF
        mainline_lights['worker3'].color = LightColor.OFF
        time.sleep(STEP_TIME)

    def reset(self):
        for l in worker1_lights.values():
            l.color = LightColor.OFF
            l.label = ''
        for l in worker2_lights.values():
            l.color = LightColor.OFF
            l.label = ''
        for l in mainline_lights.values():
            l.color = LightColor.OFF
            l.label = ''
        worker1_lights['light1'].label = self.order.processor
        worker1_lights['light2'].label = self.order.camera
        worker1_lights['light3'].label = self.order.mic
        worker1_lights['worker1'].label = 'Worker1'
        worker2_lights['light1'].label = 'Daughterboard'
        worker2_lights['light2'].label = self.order.speaker
        worker2_lights['worker2'].label = 'Worker2'
        mainline_lights['light1'].label = 'Frame'
        mainline_lights['light2'].label = 'Subassembly 2'
        mainline_lights['light3'].label = 'Subassembly 1'
        mainline_lights['light4'].label = self.order.battery
        mainline_lights['light5'].label = 'Back Case'
        mainline_lights['light6'].label = self.order.screen
        mainline_lights['worker3'].label = 'Worker3'

class ScenarioWithoutCamera(Scenario):


    def step1(self):
        self.reset()
        print("Step {}".format(1))
        worker1_lights['worker1'].color = LightColor.RED
        worker1_lights['light1'].color = LightColor.YELLOW
        worker1_lights['light2'].color = LightColor.OFF
        worker1_lights['light3'].color = LightColor.YELLOW
        worker2_lights['light1'].color = LightColor.YELLOW
        worker2_lights['light2'].color = LightColor.YELLOW
        worker2_lights['worker2'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step2(self):
        self.reset()
        print("Step {}".format(2))
        worker1_lights['worker1'].color = LightColor.RED
        worker1_lights['light1'].color = LightColor.RED
        worker1_lights['light2'].color = LightColor.OFF
        worker1_lights['light3'].color = LightColor.RED
        worker2_lights['light1'].color = LightColor.RED
        worker2_lights['light2'].color = LightColor.RED
        worker2_lights['worker2'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step3(self):
        self.reset()
        print("Step {}".format(3))
        worker1_lights['worker1'].color = LightColor.GREEN
        worker1_lights['light1'].color = LightColor.GREEN
        worker1_lights['light2'].color = LightColor.OFF
        worker1_lights['light3'].color = LightColor.GREEN
        worker2_lights['light1'].color = LightColor.GREEN
        worker2_lights['light2'].color = LightColor.GREEN
        worker2_lights['worker2'].color = LightColor.GREEN
        time.sleep(STEP_TIME)

    def step4(self):
        self.reset()
        print("Step {}".format(4))
        worker1_lights['worker1'].color = LightColor.OFF
        worker1_lights['light1'].color = LightColor.OFF
        worker1_lights['light2'].color = LightColor.OFF
        worker1_lights['light3'].color = LightColor.OFF
        worker2_lights['light1'].color = LightColor.OFF
        worker2_lights['light2'].color = LightColor.OFF
        worker2_lights['worker2'].color = LightColor.OFF
        mainline_lights['light1'].color = LightColor.YELLOW
        mainline_lights['light2'].color = LightColor.YELLOW
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)

    def step5(self):
        self.reset()
        print("Step {}".format(4))
        worker1_lights['worker1'].color = LightColor.OFF
        worker1_lights['light1'].color = LightColor.OFF
        worker1_lights['light2'].color = LightColor.OFF
        worker1_lights['light3'].color = LightColor.OFF
        mainline_lights['light1'].color = LightColor.RED
        mainline_lights['light2'].color = LightColor.RED
        mainline_lights['worker3'].color = LightColor.RED
        time.sleep(STEP_TIME)
