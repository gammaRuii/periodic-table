import kivy
import kivy.app
import json
from kivy.uix.label import Label
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class Scrolling(ScrollView):
    pass

class MainBody(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 18
        self.rows = 7
        self.orientation = "lr-tb"
        button_size = dp(103)
        with open("p.json") as p:
            e = p.read()
            el = json.loads(e)
            elements = el['elements']
            b = Button(text = "H", size_hint = (None,None), size = (button_size,button_size))
            self.add_widget(b)
            for i in range(16):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            b = Button(text = "He", size_hint = (None,None), size = (button_size,button_size))
            self.add_widget(b)
            for i in range(2,4):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)
            for i in range(10):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            for i in range(4,10):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)
            for i in range(10,12):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)
            for i in range(10):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            for i in range(12,18):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)
            for i in range(18,56):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)
            b = Button(text = "Lanthanides", size_hint=(None, None), size=(button_size, button_size))
            self.add_widget(b)
            for i in range(71,88):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)
            b = Button(text = "Actinides", size_hint=(None, None), size=(button_size, button_size))
            self.add_widget(b)
            for i in range(103,118):
                b = Button(text="{}".format(elements[i]["symbol"]), size_hint=(None, None), size=(button_size, button_size))
                self.add_widget(b)

class PeriodicTableApp(App):
    pass




app = PeriodicTableApp()
app.run()