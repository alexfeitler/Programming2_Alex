from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)

gravity = 6.67e-11


class GravityApp(App):
    def build(self):
        return GravityLayout()


class GravityLayout(BoxLayout):
    def calculate(self, first, second, distance):
        try:
            self.display.font_size = 40
            equation = "(" + str(first) + "*" + str(second) + "*" + str(gravity) + ")" + "/" + str(float(distance)**2)
            answer = eval(equation)
            self.display.text = str(answer)
        except ZeroDivisionError:
            self.display.text = "Location must be different"
            self.display.font_size = 30
        except OverflowError:
            self.display.font_size = 30
            self.display.text = "Too many objects"
        except:
            self.display.font_size = 30
            self.display.text = "You must enter a value"


if __name__ == "__main__":
    app = GravityApp()
    app.run()
