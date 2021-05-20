from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


# main window that will have the main options
class MainWindow(Screen):
    pass

# coding window
class CodingWindow(Screen):
     def schedule(self):
        schedule_popup()

class ExercisingWindow(Screen):
    def schedule(self):
        schedule_popup()

class ReadingWindow(Screen):
    def timer(self):
        timer_popup()

class TimerWindow(FloatLayout):
    pass

class ScheduleWindow(FloatLayout):
    pass


class WindowManager(ScreenManager):
    pass


def schedule_popup():
    show = ScheduleWindow()

    popupWindow = Popup(title="Schedule Window", content=show, size_hint=(None, None), size=(400, 400))

    popupWindow.open()


def timer_popup():
    show = TimerWindow()

    popupWindow = Popup(title="Timer Window", content=show, size_hint=(None, None), size=(400, 400))

    popupWindow.open()


class TamagochiApp(App):
    def build(self):
        pass


if __name__ == "__main__":
    TamagochiApp().run()
