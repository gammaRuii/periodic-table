from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# Declare both screens
class MainScreen(Screen):
    pass

class ElScreen(Screen):
    pass

class WindowManager (ScreenManager):
    pass

kv = Builder.load_file("funnything.kv")

class TestApp(App):

    def build(self):
        return kv

if __name__ == '__main__':
    TestApp().run()