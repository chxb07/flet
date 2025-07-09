from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        # Root layout
        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20
        )

        # App logo (You must replace this with a local image file)
        logo = Image(
            source="logo.png",  # replace with your local image path
            size_hint=(1, 0.3),
            allow_stretch=True,
        )

        # Welcome text
        welcome_label = Label(
            text="Welcome to Kivy!",
            font_size='24sp',
            size_hint=(1, 0.1)
        )

        # Name input
        self.name_field = TextInput(
            hint_text="Type your name...",
            size_hint=(1, 0.1),
            multiline=False,
            padding_y=(10, 10),
            background_normal='',
            background_color=(0.9, 0.9, 1, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0.2, 0.4, 1, 1)
        )

        # Greeting label
        self.greeting_label = Label(
            text="",
            font_size='18sp',
            size_hint=(1, 0.1),
            color=(0.1, 0.2, 0.8, 1)
        )

        # Greet button
        greet_button = Button(
            text="Greet Me",
            size_hint=(1, 0.15),
            background_normal='',
            background_color=(0.2, 0.5, 1, 1),
            color=(1, 1, 1, 1),
            font_size='18sp'
        )
        greet_button.bind(on_press=self.greet_clicked)

        # Add widgets to layout
        layout.add_widget(logo)
        layout.add_widget(welcome_label)
        layout.add_widget(self.name_field)
        layout.add_widget(greet_button)
        layout.add_widget(self.greeting_label)

        return layout

    def greet_clicked(self, instance):
        name = self.name_field.text.strip()
        if name:
            self.greeting_label.text = f"Hello, {name}!"
        else:
            self.greeting_label.text = "Please enter your name"


if __name__ == '__main__':
    MainApp().run()
