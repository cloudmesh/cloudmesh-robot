from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
import requests
import sys

data = {
    'ip': '10.0.1.101'
    }
    
layout = """
<Swim>:
    cols: 3
    rows: 4

    Button:
        id: left
        text: 'LEFT'
        on_press: root.left()
    Button:
        id: forward
        text: 'FORWARD'
        on_press: root.forward()
    Button:
        id: right
        text: 'RIGHT'
        on_press: root.right()
    Button:
        id: label4
        text: 'UP'
        on_press: root.up()
    Button:
        id: label5
        text: 'ZERO'
        on_press: root.zero()
    Button:
        id: label6
        text: 'DOWN'
        on_press: root.down()
    Button:
        id: label7
        text: '.' 
    Button:
        id: label8
        text: 'END'
        on_press: root.end()
    Button:
        id: label9
        text: '.'                        
"""

Builder.load_string(layout)


class Swim(GridLayout):
    pass

    def handle(self, button, data):
        data['button'] = button
        try:
            r = requests.get('https://{ip}/{button}').format(**data)
        except Exception as ConnectionError:
            print ("ERROR: can not find device", data['ip'])
        
    def left(self):
        print('left')
        self.handle("left", data)

    def right(self):
        print('right')
        self.handle("right", data)

    def forward(self):
        print('forward')
        self.handle("forward", data)

    def up(self):
        print('up')
        self.handle("up", data)

    def down(self):
        print('down')
        self.handle("down", data)

    def zero(self):
        print('zero')
        self.handle("zero", data)

    def end(self):
        print('end')
        self.handle("end", data)
        sys.exit(0)


class SwimApp(App):
    def build(self):
        return Swim()

if __name__ == '__main__':
    SwimApp().run()
