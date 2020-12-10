from kivymd.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


GUI = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        print(screen_name)


MainApp().run()
