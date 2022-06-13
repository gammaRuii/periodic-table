import kivy
import kivy.app
import json
import textwrap
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from colordict import *

sm = ScreenManager()

with open("p.json") as p:
    e = p.read()
    el = json.loads(e)
    elements = el['elements']
    def determineColor(number):
        colors = ColorDict(norm=255, mode='rgb', palettes_path="", is_grayscale=False, palettes='all')
        group = elements[number]["category"]
        if group == "alkali metal":
            color = colors['rustyred']
        elif group == "alkaline earth metal":
            color = colors['fuchsia']
        elif group == "transition metal":
            color = colors['aqua']
        elif group == "metalloid":
            color = colors['green']
        elif group == "noble gas":
            color = colors['coral']
        elif group == "post-transition metal":
            color = colors['orange']
        elif group == "halogen":
            color = colors['yellow']
        elif group == "lanthanide":
            color = colors['lichen']
        elif group == "actinide":
            color = colors['pink']
        else:
            color = colors['blue']
        normalColor = (color[0]/255, color[1]/255, color[2]/255)
        return normalColor

button_size = dp(103)

class MainBody(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 18
        self.orientation = "lr-tb"
        with open("p.json") as p:
            e = p.read()
            el = json.loads(e)
            elements = el['elements']
            b = Button(text = "[size=40]1[/size]\n\n[size=65]H[/size]\n[size=30]Hydrogen[/size]\n[size=30]1.01[/size]", markup = True, halign = "center", size_hint = (None,None), size = (button_size,button_size), background_color = determineColor(0))
            b.bind(on_press= app.callback)
            self.add_widget(b)
            for i in range(16):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            b = Button(text = "[size=40]2[/size]\n\n[size=65]He[/size]\n[size=30]Helium[/size]\n[size=30]4.003[/size]", markup = True, halign = "center", size_hint = (None,None), size = (button_size,button_size), background_color = determineColor(1))
            b.bind(on_press= app.callback)
            self.add_widget(b)
            for i in range(2,4):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            for i in range(10):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            for i in range(4,10):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            for i in range(10,12):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            for i in range(10):
                l = Label(text = "", size_hint = (None,None), size = (button_size,button_size))
                self.add_widget(l)
            for i in range(12,18):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            for i in range(18,56):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            b = Button(text = "Lanthanides", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(57))
            b.bind(on_press= app.callback)
            # open up menu for lanthanides
            self.add_widget(b)
            for i in range(71,88):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            b = Button(text = "Actinides", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(89))
            b.bind(on_press= app.callback)
            # open up menu for actinides
            self.add_widget(b)
            for i in range(103,118):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            for i in range(18):
                l = Label(text = "", size_hint = (None,None), size = (button_size, dp(42)))
                self.add_widget(l)
            for i in range(2):
                l = Label(text = "", size_hint = (None,None), size = (button_size, button_size))
                self.add_widget(l)
            for i in range(56,71):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)
            l = Label(text="", size_hint=(None, None), size=(button_size, button_size))
            self.add_widget(l)
            for i in range(2):
                l = Label(text = "", size_hint = (None,None), size = (button_size, button_size))
                self.add_widget(l)
            for i in range(88,103):
                b = Button(text="[size=40]{}[/size]\n\n[size=65]{}[/size]\n[size=30]{}[/size]\n[size=30]{}[/size]".format(elements[i]["number"],elements[i]["symbol"],elements[i]["name"],elements[i]["atomic_mass"]), markup = True, halign = "center", size_hint=(None, None), size=(button_size, button_size), background_color = determineColor(i))
                b.bind(on_press= app.callback)
                self.add_widget(b)

# screens
class Manager(ScreenManager):
    pass

class ElScreen(Screen):
    pass

class MainScreen(Screen):
    pass

# lanthanide and actinide screen
class SeriesScreen(Screen):
    pass

# layout for element pop-up
class ElementGrid(GridLayout):
    pass

# layout for lanthanide and actinide series
class SeriesBox(BoxLayout):
    pass



class PeriodicTableApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.textWidth = 50


    def callback(self, instance):
        self.root.transition.direction = "left"
        eltext = instance.text
        eltext = eltext.replace("[size=40]", "")
        eltext = eltext.replace("[size=65]", "")
        eltext = eltext.replace("[size=30]", "")
        element = eltext.replace("[/size]", "")
        # print(element)
        elementNum = element.split('\n', 1)[0]
        # print(elementNum)
        with open("p.json") as p:
            e = p.read()
            el = json.loads(e)
            elements = el['elements']
            seriesDict = {
                "Lanthanum": 57,
                "Cerium": 58,
                "Praseodymium": 59,
                "Neodymium": 60,
                "Promethium": 61,
                "Samarium": 62,
                "Europium": 63,
                "Gadolinium": 64,
                "Terbium": 65,
                "Dysprosium": 66,
                "Holmium": 67,
                "Erbium": 68,
                "Thulium": 69,
                "Ytterbium": 70,
                "Lutetium": 71,
                "Actinium": 89,
                "Thorium": 90,
                "Protactinium": 91,
                "Uranium": 92,
                "Neptunium": 93,
                "Plutonium": 94,
                "Americium": 95,
                "Curium": 96,
                "Berkelium": 97,
                "Californium": 98,
                "Einsteinium": 99,
                "Fermium": 100,
                "Mendelevium": 101,
                "Nobelium": 102,
                "Lawrencium": 103
            }
            if elementNum in seriesDict.keys():
                elementNum = str(seriesDict.get(elementNum))
            # print(elementNum)
            try:
                elnum = int(elementNum[:3]) - 1
                self.root.get_screen("element").ids["symbutton2"].text = elements[elnum]["symbol"]
                self.root.get_screen("element").ids["symbutton2"].background_color = determineColor(elnum)
                self.root.get_screen("element").ids["namebutton2"].text = "[b]" + elements[elnum]["name"] + "[/b]"
                self.root.get_screen("element").ids["namebutton2"].background_color = determineColor(elnum)
                self.root.get_screen("element").ids["catbutton2"].text = elements[elnum]["category"].capitalize()
                self.root.get_screen("element").ids["catbutton2"].background_color = determineColor(elnum)
                self.root.get_screen("element").ids["numbutton2"].text = str(elnum + 1)
                self.root.get_screen("element").ids["numbutton2"].background_color = determineColor(elnum)
                self.root.get_screen("element").ids["aaabutton2"].text = str(float(elements[elnum]["atomic_mass"]))
                self.root.get_screen("element").ids["aaabutton2"].background_color = determineColor(elnum)
                self.root.get_screen("element").ids["econfigbutton2"].text = elements[elnum][
                    "electron_configuration_semantic"]
                self.root.get_screen("element").ids["econfigbutton2"].background_color = determineColor(elnum)
                self.root.get_screen("element").ids["sumbutton2"].text = textwrap.fill(elements[elnum]["summary"], width=self.textWidth)
                self.root.get_screen("element").ids["sumbutton2"].background_color = determineColor(elnum)
                self.root.current = "element"
            except ValueError:
                elnum = 1
                if elementNum == "Lanthanides":
                    elnum = 56
                if elementNum == "Actinides":
                    elnum = 88
                else:
                    pass
                self.root.get_screen("series").ids["name"].text = elementNum
                for i in range(1, 16):
                    self.root.get_screen("series").ids["b{}".format(i)].text = elements[elnum]["name"]
                    self.root.get_screen("series").ids["b{}".format(i)].background_color = determineColor(elnum)
                    elnum += 1
                self.root.current = "series"

    def redefWidth(self, instance):

        if app.root.size[0] > app.root.size[1]:
            self.textWidth = 100

        else:
            self.textWidth = 50

        instance.text = textwrap.fill(instance.text, self.textWidth)

        instance.canvas.ask_update()

app = PeriodicTableApp()



app.run()