from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from labels import *
from kivy.properties import ObjectProperty


class HomeScreen(Screen):
    pass


class CalculatorScreen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    # https://kivymd.readthedocs.io/en/latest/components/navigation-drawer/
    pass


class MainApp(MDApp):
    def build(self):
        self.title = TITLE
        GUI = Builder.load_file("main.kv")
        return GUI


MainApp().run()
