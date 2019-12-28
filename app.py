import calc as calc
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout

grey = [.3,.3,.3,1]
blue = [0.0,1,1]
green = [0,1,0,1]
red = [1,0,0,1]

class MyButton(ToggleButtonBehavior, Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.background_color = grey
        self.checked = False

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = blue
            self.checked = True
        else:
            self.background_color = grey
            self.checked = False

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=3)
        self.type_buttons = [MyButton(text=name) for name in calc.types if name != ""]
        [layout.add_widget(button) for button in self.type_buttons]
        layout.add_widget(Button(text='reset', background_color=red))
        layout.add_widget(Button(text='go', background_color=green))

        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()