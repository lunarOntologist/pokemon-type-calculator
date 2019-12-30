import calc as calc
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label

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

class DisplayScreen(Screen):
    def __init__(self, **kwargs):
        super(DisplayScreen, self).__init__(**kwargs)
        layout = RelativeLayout()

        self.go_button = Button(text='return', background_color=green, pos_hint={'x':0,'y':.8}, size_hint=(1, .2))
        self.go_button.bind(on_press=self.on_go)
        layout.add_widget(self.go_button)
        self.l = Label(text='', pos_hint={'x': 0, 'y': 0}, size_hint=(1, .8))
        layout.add_widget(self.l)
        self.add_widget(layout)

    def set_text(self, text):
        self.l.text= text

    def on_go(self, instance):
        self.manager.current = 'selection'

class SelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=3)
        self.type_buttons = dict([[name, MyButton(text=name)]
                                  for name in calc.types if name != ""])
        [layout.add_widget(button) for button in self.type_buttons.values()]
        self.go_button = Button(text='go', background_color=green)
        self.go_button.bind(on_press=self.on_go)
        self.reset_button = Button(text='reset', background_color=red)
        self.reset_button.bind(on_press=self.on_reset)
        layout.add_widget(self.reset_button)
        layout.add_widget(self.go_button)
        self.add_widget(layout)

    def on_go(self, instance):
        vals = calc.get_starting_vals()
        [calc.typedefense[button[0]](vals) for button in self.type_buttons.items() if button[1].is_checked()]
        self.manager.get_screen('display').set_text(calc.get_output(vals))
        # self.manager.set_results(calc.get_output(vals))
        self.manager.current = 'display'

    def on_reset(self, instance):
        [button.clear() for button in self.type_buttons.values()]

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        selection = SelectionScreen(name='selection')
        display = DisplayScreen(name='display')
        sm.add_widget(selection)
        sm.add_widget(display)
        sm.current = 'selection'
        return sm

if __name__ == '__main__':
    app = MainApp()
    app.run()