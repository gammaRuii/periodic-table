import kivy
import kivy.app
import json

from kivy.lang import Builder
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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.bubble import Bubble, BubbleButton
from colordict import *

sm = ScreenManager()
with open("p.json") as p:
    e = p.read()
    el = json.loads(e)
    elements = el['elements']
    def determineColor(number):
        colors = ColorDict()
        group = elements[number]["category"]
        if group == "alkali metal":
            color = colors['truered']
        elif group == "alkaline earth metal":
            color = colors['fuchsiarose']
        elif group == "transition metal":
            color = colors['aquasky']
        elif group == "metalloid":
            color = colors['green']
        elif group == "noble gas":
            color = colors['livingcoral']
        elif group == "post-transition metal":
            color = colors['orange']
        elif group == "halogen":
            color = colors['yellow']
        elif group == "lanthanide":
            color = colors['greenery']
        elif group == "actinide":
            color = colors['pink']
        else:
            color = colors['blue']
        normalColor = (color[0]/255, color[1]/255, color[2]/255)
        return normalColor

button_size = dp(103)

def callback(number, **instance):
    print (instance, number)
    sm.current = "element"
# Builder.load_file("periodictable.kv")

class MainBody(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 18
        self.orientation = "lr-tb"
        with open("p.json") as p:
            e = p.read()
            el = json.loads(e)
            elements = el['elements']
            b = Button(text = "[size=15]1[/size]\n\n[size=25]H[/size]\n[size=10]Hydrogen[/size]\n[size=10]1.01[/size]", markup = True, halign = "center", size_hint = (None,None), size = (button_size,button_size), background_color = determineColor(0))
            b.bind(on_press=callback)
            self.add_widget(b)
            for i in range(16):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            b = Button(text = "[size=15]2[/size]\n\n[size=25]He[/size]\n[size=10]Helium[/size]\n[size=10]4.003[/size]", markup = True, halign = "center", size_hint = (None,None), size = (button_size,button_size), background_color = determineColor(1))
            b.bind(on_press=callback)
            self.add_widget(b)
            for i in range(2,4):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            for i in range(10):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            for i in range(4,10):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            for i in range(10,12):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            for i in range(10):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            for i in range(12,18):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            for i in range(18,56):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            b = Button(text = "Lanthanides", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(57))
            b.bind(on_press=callback)
            # open up menu for lanthanides
            self.add_widget(b)
            for i in range(71,88):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            b = Button(text = "Actinides", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(89))
            b.bind(on_press=callback)
            # open up menu for actinides
            self.add_widget(b)
            for i in range(103,118):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            for i in range(18):
                l = Label(text = "", size_hint = (None,None), size = (button_size, dp(42)))
                self.add_widget(l)
            for i in range(2):
                l = Label(text = "", size_hint = (None,None), size = (button_size, button_size))
                self.add_widget(l)
            for i in range(56,71):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)
            l = Label(text="", size_hint=(None, None), size=(button_size, button_size))
            self.add_widget(l)
            for i in range(2):
                l = Label(text = "", size_hint = (None,None), size = (button_size, button_size))
                self.add_widget(l)
            for i in range(88,103):
                b = Button(text="[size=15]{}[/size]\n\n[size=25]{}[/size]\n[size=10]{}[/size]\n[size=10]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press=callback)
                self.add_widget(b)

class Element(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        with open("p.json") as p:
            e = p.read()
            el = json.loads(e)
            elements = el['elements']

class Manager(ScreenManager):
    pass

class ElScreen(Screen):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     box = BoxLayout()
    #     self.add_widget(box)
    #     box.add_widget(Button(text = "hi"))
    pass

class MainScreen(Screen):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     main = MainBody()
    #     self.add_widget(main)
    pass

# sm.add_widget(MainScreen(name = "main"))
# sm.add_widget(ElScreen(name = "element"))
# sm.current = "main"



class PeriodicTableApp(App):
    pass

app = PeriodicTableApp()
app.run()