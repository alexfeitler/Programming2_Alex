from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1, 0, 1, 0)

class FormatApp(App):
    def build(self):
        return FormatLayout()

class FormatLayout(BoxLayout):
    def text_on(self, number):
        if number:
            self.label.color = 1, 1, 1, 1
        else:
            self.label.color = 1, 0, 1, 0

    def text_change(self, text):
        self.label.text = text

    def font_change(self, font):
        if font == "Free Sans Bold":
            self.label.font_name = "freesansbold.ttf"
            self.spinner.font_name = "freesansbold.ttf"
        if font == "Test Sans":
            self.label.font_name = "test_sans.ttf"
            self.spinner.font_name = "test_sans.ttf"

    def change_window(self, r=1, g=0, b=1):
        Window.clearcolor = (r, g, b, 1)

if __name__ == "__main__":
    app = FormatApp()
    app.run()