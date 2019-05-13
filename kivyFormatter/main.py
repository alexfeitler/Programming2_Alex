from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

Window.clearcolor = (1, 1, 1, 1)
Window.size = (675, 600)

class DemoApp(App):
    def build(self):
        return DemoLayout()

class DemoLayout(BoxLayout):



if __name__ == "__main__":
    demo = DemoApp()
    demo.run()