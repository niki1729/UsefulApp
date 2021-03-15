from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from labels import *
from kivy.properties import ObjectProperty, StringProperty



class HomeScreen(Screen):
    pass


class CalculatorScreen(Screen):
    history_text = StringProperty()
    last_result = ""
    last_calc = ""
    new_calc = True
    char_processed = False

    def print_button_text(self, char):
        self.char_processed = False

        if self.new_calc:
            state = char == "+" or char == "-" or char == "*" or char == "/"
            if not self.char_processed and state:
                if self.last_result != "" and self.ids.calc_inp.text == "":
                    self.ids.calc_inp.text = self.last_result + str(char)
                elif self.ids.calc_inp.text == "":
                    self.ids.calc_inp.text = "0" + self.ids.calc_inp.text + str(char)

            elif not self.char_processed and char == "." and self.ids.calc_inp.text == "":
                try:
                    int(self.last_result)
                    self.ids.calc_inp.text = self.last_result + str(char)
                except:
                    self.ids.calc_inp.text = self.last_result

            elif not self.char_processed and self.ids.calc_inp.text == "":
                self.ids.calc_inp.text = self.ids.calc_inp.text + str(char)

            self.char_processed = True

        elif not self.char_processed:
            self.ids.calc_inp.text = self.ids.calc_inp.text + str(char)
        self.new_calc = False

    def eval_function(self):
        try:
            self.last_result = str(eval(self.ids.calc_inp.text))
            self.last_calc = self.ids.calc_inp.text
            self.history_text = str(self.ids.calc_inp.text) + "=" + self.last_result
            self.ids.calc_inp.text = ""
            self.new_calc = True
        except:
            self.ids.calc_inp.text = "Python syntax error!"

    def last_result_print(self):
        self.ids.calc_inp.text = self.last_calc
        self.new_calc = False

    def clear_text_input(self):
        self.ids.calc_inp.text = ""
        self.new_calc = True

    def delete_last_char(self):
        self.ids.calc_inp.text = self.ids.calc_inp.text[:-1]
        if self.ids.calc_inp.text == "":
            self.new_calc = True

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if self.test3.focus and keycode == 40:  # 40 - Enter key pressed
            self.eval_function()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    # https://kivymd.readthedocs.io/en/latest/components/navigation-drawer/
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        self.title = TITLE
        GUI = Builder.load_file("main.kv")
        return GUI


MainApp().run()
