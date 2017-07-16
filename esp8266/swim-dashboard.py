from guizero import App, TextBox, PushButton, Slider, Text, ButtonGroup, Box
import sys


def action_test():
    print("LEFT", left.get())
    print("RIGHT", right.get())
    fields = ['ticks', 'cm', 'in']
    print("CHOICE", fields[int(choice.get())])
    print("ANGLE", angle.get())


def action_angle(angle):
    print(angle)


def action_exit(angle):
    sys.exit(0)


def NamedSlider(label, value=0, command=None, start=-90, end=90):
    box = Box(app, layout="grid")
    label_text = Text(box, label, grid=[0, 0])
    slider = Slider(box, command=command, start=start, end=end)
    return slider

def NamedText(label, text=""):
    box = Box(app, layout="grid")
    label_text = Text(box, label, grid=[0, 0])
    text = TextBox(box, text=text, grid=[0, 1])
    return text


app = App(title="Cloudmesh Fish Dashboard")

ip = NamedText("ip", text="10.0.1.101")

angle_fin_left = NamedText("Angle Left", text="90")
angle_fin_right = NamedText("Angle Right", text="90")
angle_fin_middle = NamedText("Angle Middle", text="0")

angle_pitch = NamedText("Angle Pitch", text="10")
angle_ptch_equal = NamedText("Angle Pitch", text="10")

update = PushButton(app, command=action_test, text="Submit")
exit = PushButton(app, command=action_exit, text="exit")

angle = NamedSlider(app, command=action_angle, start=-90, end=90)
'''
choice = ButtonGroup(app,
                     options=[["ticks", 0],
                              ["cm", 1],
                              ["in", 2]],
                     selected=0)
                     
'''
app.display()
