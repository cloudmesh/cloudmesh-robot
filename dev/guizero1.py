from guizero import App, TextBox, PushButton, Slider, CheckBox, Text, ButtonGroup, Box


def action_test():
    print("LEFT", left.get())
    print("RIGHT", right.get())
    fields = ['ticks', 'cm', 'in']
    print("CHOICE", fields[int(choice.get())])
    print("ANGLE", angle.get())


def action_angle(angle):
    print(angle)


def textinput(label):
    box = Box(app, layout="grid")
    label_text = Text(box, label, grid=[0, 0])
    text = TextBox(box, grid=[0, 1])
    return text


app = App(title="Hello world")

left = textinput("Left")
right = textinput("Right")

update = PushButton(app, command=action_test, text="Press me")

angle = Slider(app, command=action_angle, start=-90, end=90)

choice = ButtonGroup(app,
                     options=[["ticks", 0],
                              ["cm", 1],
                              ["in", 2]],
                     selected=0)
app.display()
