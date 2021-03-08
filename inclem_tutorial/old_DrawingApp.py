from kivy.app import App
from kivy.properties import ObjectProperty

from kivy.uix.slider import Slider

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line



global colors_width
colors_width = [0.5, 0.5, 0.5, 0.5, 2]


class DrawingWidget(Widget):
    def __init__(self, **kwargs):
        super(DrawingWidget, self).__init__()
        self.color = (0.5, 0.5, 0.5, 1)

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if not self.collide_point(*touch.pos):
            return

        with self.canvas:
            # print(self.color)
            self.color = (colors_width[0], colors_width[1], colors_width[2], colors_width[3])
            Color(*self.color)
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=colors_width[4])

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


class Interface(BoxLayout):
    pass


class DrawingApp(App):

    def build(self):
        root_widget = Interface()
        return root_widget

    def my_value_red(self, value):
        colors_width[0] = value
        print(colors_width)

    def my_value_green(self, value):
        colors_width[1] = value
        print(colors_width)

    def my_value_blue(self, value):
        colors_width[2] = value
        print(colors_width)

    def my_value_alpha(self, value):
        colors_width[3] = value
        print(colors_width)

    def my_value_width(self, value):
        colors_width[4]=value


DrawingApp().run()

"""Label:
            text: "R: "+ str(round(red_slider.value, 2))+"  G: "+ str(round(green_slider.value, 2))+"  B: "+ str(round(blue_slider.value, 2))+" A: "+str(round(alpha_slider.value),2)
"""
