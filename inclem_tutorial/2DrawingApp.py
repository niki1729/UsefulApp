from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line


class DrawingWidget(Widget):
    def __init__(self):
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
            print(self.color)
            Color(*self.color)
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)
            #  touch.ud["line"] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
        # touch.ud["line"].points += [touch.pos[0], touch.pos[1]]


class DrawingApp(App):

    def build(self):
        root_widget = BoxLayout(orientation="vertical")
        drawing_widget = DrawingWidget()

        red_slider = Slider(min=0, max=1, value=0.5, size_hint_y=None, height=50)
        green_slider = Slider(min=0, max=1, value=0.5, size_hint_y=None, height=50)
        blue_slider = Slider(min=0, max=1, value=0.5, size_hint_y=None, height=50)
        alpha_slider = Slider(min=0, max=1, value=1, size_hint_y=None, height=50)

        colour_row = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)

        colour_label = Label(text="Output colour:")
        colour_widget = Widget()

        # We draw a Rectangle on colour_widget exactly the same way as
        # with DrawingWidget, just without making a new class
        with colour_widget.canvas:
            output_colour = Color(red_slider.value, green_slider.value, blue_slider.value, alpha_slider.value)
            output_rectangle = Rectangle()

        def update_colour_widget_rect(instance, value):
            output_rectangle.pos = colour_widget.pos
            output_rectangle.size = colour_widget.size

        colour_widget.bind(pos=update_colour_widget_rect, size=update_colour_widget_rect)

        def update_colour_widget_colour(instance, value):
            output_colour.rgba = (red_slider.value, green_slider.value, blue_slider.value, alpha_slider.value)
            drawing_widget.color = output_colour.rgba

        red_slider.bind(value=update_colour_widget_colour)
        green_slider.bind(value=update_colour_widget_colour)
        blue_slider.bind(value=update_colour_widget_colour)
        alpha_slider.bind(value=update_colour_widget_colour)

        root_widget.add_widget(drawing_widget)
        root_widget.add_widget(red_slider)
        root_widget.add_widget(green_slider)
        root_widget.add_widget(blue_slider)
        root_widget.add_widget(alpha_slider)
        root_widget.add_widget(colour_row)

        colour_row.add_widget(colour_label)
        colour_row.add_widget(colour_widget)

        return root_widget


DrawingApp().run()
