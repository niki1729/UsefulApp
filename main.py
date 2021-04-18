from random import randint

from kivy.core.text import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window

from labels import *
from utilities.converter import *
from utilities.calculator_eval import Eval

Window.size = (600, 700)


# For PopupWindow, probably wil be used several times
class P(FloatLayout):
    pass


class HomeScreen(Screen):
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1


class CalculatorScreen(Screen):
    history_text = StringProperty()
    last_result = ""
    last_calc = ""
    new_calc = True
    char_processed = False

    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)

    def print_button_text(self, char):
        self.char_processed = False

        if self.new_calc:
            state = char == "+" or char == "*" or char == "/"  # char == "-" or
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
        if self.ids.calc_inp.text != "":

            try:
                eval = Eval()
                self.last_result = str(self.if_int(round(eval.evaluate(self.ids.calc_inp.text), 4)))
                self.last_calc = self.ids.calc_inp.text
                self.history_text = str(self.ids.calc_inp.text) + "=" + self.last_result
                self.ids.calc_inp.text = ""
                self.new_calc = True
            except:
                # self.last_result = self.ids.calc_inp.text
                # self.ids.calc_inp.text = "Python syntax error!"
                self.show_popup()

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

        print(text)
        if keycode == 40:  # 40 - Enter key pressed#
            print("test")
            self.eval_function()
        return True

    def show_popup(self):
        show = P()
        popup_window = Popup(title="Python syntax error!", content=show, size_hint=(0.5, 0.3), size=(400, 100))
        # show.ids.popuplabel.text = "Python syntax error!"
        popup_window.open()

    def if_int(self, result):
        if int(result) == result:
            return int(result)
        else:
            return result


class ConverterScreen(Screen):
    def react_press_unit_button(self, instance):
        print(str(instance))
        instance.color = .05, .05, .05, 1
        instance.background_color = 1, 0, 0, 1

    def start(self):
        print("HI")

    parameter = ""

    distance_units = ("m", "ft", "inch", "mi", "yd", "ly")
    distance_from_list_button = BoxLayout()
    distance_to_list_button = BoxLayout()
    for symbol in distance_units:
        distance_from_list_button.add_widget(
            Button(text=symbol, background_down="grey_color.png", on_release=react_press_unit_button))
        distance_to_list_button.add_widget(
            Button(text=symbol, background_down="grey_color.png", on_release=react_press_unit_button))
    print(distance_from_list_button, distance_to_list_button)

    time_units = ("s", "min", "h", "y")
    time_from_list_button = []
    time_to_list_button = []

    mass_units = ("g", "t", "lb", "oz")
    mass_from_list_button = []
    mass_to_list_button = []

    energy_units = ("J", "Wh", "cal", "eV")
    energy_from_list_button = []
    energy_to_list_button = []

    def clear_unit_widgets_and_lists(self):
        '''self.distance_from_list_button = []
        self.distance_to_list_button = []

        self.time_from_list_button = []
        self.time_to_list_button = []

        self.mass_from_list_button = []
        self.mass_to_list_button = []

        self.energy_from_list_button = []
        self.energy_to_list_button = []'''
        self.ids.boxlayout_from.clear_widgets()
        self.ids.boxlayout_to.clear_widgets()

    def add_unit_widget(self, symbol, parameter):
        self.ids.units_box.orientation = "horizontal"
        self.ids.units_box_middle.text = ""
        self.ids.boxlayout_from.add_widget(
            Button(text=symbol, background_down="grey_color.png", on_release=self.react_press_unit_button))
        self.ids.boxlayout_to.add_widget(
            Button(text=symbol, background_down="grey_color.png"))

    def display_distance(self):
        if self.parameter != "DISTANCE":
            self.parameter = "DISTANCE"
            self.clear_unit_widgets_and_lists()

            for symbol in self.distance_units:
                self.add_unit_widget(symbol, "time")

            '''self.ids.boxlayout_from.add_widget(self.distance_from_list_button)
            self.ids.boxlayout_to.add_widget(self.distance_from_list_button)'''

    def display_time(self):
        if self.parameter != "TIME":
            self.parameter = "TIME"
            self.clear_unit_widgets_and_lists()

            for symbol in self.time_units:
                self.add_unit_widget(symbol, "time")

    def display_mass(self):
        if self.parameter != "MASS":
            self.parameter = "MASS"
            self.clear_unit_widgets_and_lists()

            for symbol in self.mass_units:
                self.add_unit_widget(symbol, "mass")

    def display_energy(self):
        if self.parameter != "ENERGY":
            self.parameter = "ENERGY"
            self.clear_unit_widgets_and_lists()

            for symbol in self.energy_units:
                self.add_unit_widget(symbol, "energy")

    def display_speed(self):
        if self.parameter != "SPEED":
            self.parameter = "SPEED"
            self.clear_unit_widgets_and_lists()

            speed_units_box_from_distance = BoxLayout()
            speed_units_box_from_time = BoxLayout()
            speed_units_box_to_distance = BoxLayout()
            speed_units_box_to_time = BoxLayout()

            # work more here
            for symbol in self.distance_units:
                speed_units_box_from_distance.add_widget(Button(text=symbol, background_down="grey_color.png"))
                speed_units_box_to_distance.add_widget(Button(text=symbol, background_down="grey_color.png"))

            for symbol in self.time_units:
                speed_units_box_from_time.add_widget(Button(text=symbol, background_down="grey_color.png"))
                speed_units_box_to_time.add_widget(Button(text=symbol, background_down="grey_color.png"))

            self.ids.units_box.orientation = "vertical"

            self.ids.boxlayout_from.add_widget(speed_units_box_from_distance)
            self.ids.boxlayout_from.add_widget(Button(text="", disabled=True, size_hint_x=0.1))
            self.ids.boxlayout_from.add_widget(speed_units_box_to_distance)

            self.ids.boxlayout_to.add_widget(speed_units_box_from_time)
            # self.ids.boxlayout_to.add_widget(Label(size_hint_x=0.1))
            self.ids.boxlayout_to.add_widget(Button(text="", disabled=True, size_hint_x=0.1))
            self.ids.boxlayout_to.add_widget(speed_units_box_to_time)

            self.ids.units_box_middle.text = "------------------------------------------------------------------------"
            self.ids.units_box_middle.font_size = 60

    def display_area(self):
        if self.parameter != "AREA":
            self.parameter = "AREA"
            self.clear_unit_widgets_and_lists()

            for symbol in self.distance_units:
                self.add_unit_widget(symbol + "²", "area")

    def display_volume(self):
        if self.parameter != "VOLUME":
            self.parameter = "VOLUME"
            self.clear_unit_widgets_and_lists()

            for symbol in self.distance_units:
                self.add_unit_widget(symbol + "³", "volume")

    def add_micro(self, instance):
        if instance == "from":
            self.ids.conv_from_inp.text += "μ"

        if instance == "to":
            self.ids.conv_to_inp.text += "μ"

    def start_convert(self):
        print(str(self.ids.conv_from_inp.text), str(self.ids.conv_to_inp.text))


list_images = ["resources/niki.jpg", "resources/roseschloss2.jpg", "resources/tunnel.jpg"]


class DemoScreen(Screen):
    def change_image(self):
        self.ids.demo_image.source = list_images[randint(0, len(list_images) - 1)]
        self.ids.button_change_image.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1


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
