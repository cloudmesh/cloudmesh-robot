class Car(object):
    def __init__(self, leftmotor, rightmotor, leftrpm, rightrpm):
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.leftrpm = leftrpm
        self.rightrpm = rightrpm

    def rpmtest(self):
        self.leftmotor.forward()
        self.rightmotor.forward()
        for i in range(0, 10):
            l = self.leftrpm.get()
            r = self.rightrpm.get()
            print(l)
            print(r)

    def dutyadjuster(self):
        rpmr = self.rightrpm.get()
        rpml = self.leftrpm.get()
        if rpmr > rpml:
            self.rightmotor.setduty(self.right)

    def tune(self):
        self.leftmotor.forward()
        self.rightmotor.forward()
        for i in range(0, 20):
            leftduty = self.leftmotor.d
            rightduty = self.rightmotor.d
            speedright = self.rightrpm.get()
            speedleft = self.leftrpm.get()
            if speedright > speedleft:
                self.rightmotor.dutyset(rightduty - 2)
                self.rightmotor.forward()
                print('rpm right:')
                print(speedright)
                print('rpm left:')
                print(speedleft)
                time.sleep(.5)
            if speedright < speedleft:
                self.leftmotor.dutyset(leftduty - 2)
                self.leftmotor.forward()
                print('rpm right:')
                print(speedright)
                print('rpm left:')
                print(speedleft)
                time.sleep(.5)
            else:
                pass
        self.leftmotor.stop()
        self.rightmotor.stop()