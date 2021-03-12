from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Calculator(App):
    def build(self):
        root_widget = BoxLayout(orientation="vertical")

        # output_label = Label(size_hint_y=1)

        # delete_one = Button(text="delete one", size_hint_y=1)

        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')

        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        input_grid = GridLayout(cols=3, size_hint_y=1)
        input_grid.add_widget(Label(size_hint_y=1, size_hint_x=5, halign="center"))
        input_grid.add_widget(Button(text="del", font_size=30, size_hint_y=1, size_hint_x=1))
        input_grid.add_widget(Button(text="clear", size_hint_y=1, size_hint_x=1))
        print(input_grid.children[0], input_grid.children[1], input_grid.children[2])

        def print_button_text(instance):
            input_grid.children[2].text += instance.text

        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)

        def resize_label_text(label, new_height):
            label.font_size = 0.5 * label.height

        input_grid.children[2].bind(height=resize_label_text)

        def evaluate_result(instance):
            try:
                print(input_grid.children[2].text)
                input_grid.children[2].text = str(eval(input_grid.children[2].text))

            except SyntaxError:
                input_grid.children[2].text = "Python syntax error!"

        button_grid.children[0].bind(on_press=evaluate_result)

        def clear_label(instance):
            input_grid.children[2].text = ""

        input_grid.children[0].bind(on_press=clear_label)

        def delete_one_chr(insatnce):
            input_grid.children[2].text = input_grid.children[2].text[:-1]

        input_grid.children[1].bind(on_press=delete_one_chr)

        root_widget.add_widget(input_grid)
        root_widget.add_widget(button_grid)
        # root_widget.add_widget(clear_button)
        # root_widget.add_widget(input_grid.children[1])

        return root_widget


Calculator().run()
