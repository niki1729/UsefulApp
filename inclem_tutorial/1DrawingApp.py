from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line, Ellipse

from random import random, randint


class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()
        with self.canvas:
            self.little_collor = Color(1, 1, 1, 1)
            self.little_rect = Rectangle(size=(300, 100),
                                         pos=(300, 200))
        with self.canvas.before:
            self.rect_color = Color(1, 0, 0, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)

        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
        print(self.size, self.pos)

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        with self.canvas:
            if touch.button == "left":
                Color(random(), random(), random(), random())
            elif touch.button == "right":
                Color(0, 1, 0)
            else:
                Color(0,0,0,0)
            coord = randint(10, 20)
            Ellipse(size=(coord, coord), pos=(touch.x - coord / 2, touch.y - coord / 2))
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=2)

        if self.little_rect.pos[0] <= touch.pos[0] <= self.little_rect.pos[0] + self.little_rect.size[0] and \
                self.little_rect.pos[1] <= touch.pos[1] <= self.little_rect.pos[1] + self.little_rect.size[1] and \
                touch.button == "left":
            self.little_collor.rgb = (random(), random(), random())

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.pos[0], touch.pos[1]]

    def on_touch_up(self, touch):
        with self.canvas:
            coord = randint(10, 20)
            Ellipse(size=(coord, coord), pos=(touch.x - coord / 2, touch.y - coord / 2))


class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget


DrawingApp().run()

''' def on_touch_down(self, touch):
        self.rect_color.rgb = (random(), random(), random())
        if self.little_rect.pos[0] <= touch.pos[0] <= self.little_rect.pos[0] + self.little_rect.size[0] and \
                self.little_rect.pos[1] <= touch.pos[1] <= self.little_rect.pos[1] + self.little_rect.size[1]:
            self.little_collor.rgb = (random(), random(), random())

        print("touch postition is {}".format(touch.pos), str(self.rect_color.rgb))'''
