from kivy.app import App
from kivy.uix.label import Label


# from kivy.lang import Builder

class MainApp(App):
    def build(self):
        text = Label(text="Hello World!", font_size=100, italic=True, markup=True, halign='left')
        text.text = '[color=#ff0000]Hello[/color] [color=#00ff00]world[/color] [color=#0000ff]![/color]'
        return text


MainApp().run()
