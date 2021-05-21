from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (375, 812)
# Window position on your computer screen
Window.top = 100
Window.left = 750


class TamagochiProject(Widget):
    feedButton = ObjectProperty(None)

    def bindButton(self):
        self.feedButton.bind(on_press=self.feedTamagochi)

    def feedTamagochi(self, instance):
        print("Mmm.. Yummy!")

class ProjectPage(Widget):
    addProjectButton = ObjectProperty(None)

    def setup(self):
        self.addProjectButton.bind(on_press=self.addProject)

    def addProject(self, instance):
        tamagochiProject = TamagochiProject()
        tamagochiProject.bindButton()
        self.remove_widget(self.addProjectButton)
        self.add_widget(tamagochiProject)

    def update(self, dt):
        pass

class SimpleTamagochiApp(App):

    def build(self):
        projectPage = ProjectPage()
        projectPage.setup()
        Clock.schedule_interval(projectPage.update, 1.0 / 60.0)
        return projectPage


if __name__ == '__main__':
    SimpleTamagochiApp().run()