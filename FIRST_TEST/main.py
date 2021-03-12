from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.navigationdrawer import NavigationLayout


class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ContentNavigationDrawer(Screen):
    # https://kivymd.readthedocs.io/en/latest/components/navigation-drawer/
    pass


class MainApp(MDApp):
    def build(self):
        # Creating the GUI
        GUI = Builder.load_file("main.kv")
        return GUI

    def change_screen(self, screen_name):
        # Get the screen manager from kv file
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name
        print(self.root.ids)
        print(screen_name)


MainApp().run()
