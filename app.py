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
        self.clear()

    def is_checked(self):
        return self.checked

    def clear(self):
        self.background_color = grey
        self.checked = False
        self.state = 'normal'

    def mark(self):
        self.background_color = blue
        self.checked = True

    def on_state(self, widget, value):
        if value == 'down':
            self.mark()
        else:
            self.clear()

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=3)
        self.type_buttons = dict([[name, MyButton(text=name)] for name in calc.types if name != ""])
        [layout.add_widget(button) for button in self.type_buttons.values()]
        self.go_button = Button(text='go', background_color=green)
        self.go_button.bind(on_press=self.on_go)
        self.reset_button = Button(text='reset', background_color=red)
        self.reset_button.bind(on_press=self.on_reset)
        layout.add_widget(self.reset_button)
        layout.add_widget(self.go_button)

        return layout

    def on_reset(self, instance):
        [button.clear() for button in self.type_buttons.values()]

    def on_go(self, instance):
        vals = calc.get_starting_vals()
        [calc.typedefense[button[0]](vals) for button in self.type_buttons.items() if button[1].is_checked()]
        calc.print_output(vals)

if __name__ == '__main__':
    app = MainApp()
    app.run()