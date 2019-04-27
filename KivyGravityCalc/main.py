from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

gravity = 6.67e-11

Window.size = (800, 500)


class GravityApp(App):
    def build(self):
        return GravityLayout()


class GravityLayout(BoxLayout):
    def calculate(self, first, second, distance):
        try:
            self.display.font_size = 50
            equation = "(" + str(first) + "*" + str(second) + "*" + str(gravity) + ")" + "/" + str(float(distance)**2)
            answer = eval(equation)
            self.display.text = str(answer)
        except ZeroDivisionError:
            self.display.text = "Can't be in same location."
            self.display.font_size = 40
        except OverflowError:
            self.display.font_size = 40
            self.display.text = "Too many items. "
        except:
            self.display.font_size = 40
            self.display.text = "Please Enter all values."


if __name__ == "__main__":
    app = GravityApp()
    app.run()