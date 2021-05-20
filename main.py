import kivy
from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.image import Image


class Tamagochi2App(App):
    
    def build(self):
        button = Button(text="Submit", font_size="30sp",
                        background_color=(1, 1, 1, 1),
                        color=(50, 50, 50, 50),
                        size=(15, 15),
                        size_hint=(.2, .2),
                        pos=(400, 250))

        # bind() use to bind the button to function click
        button.bind(on_press=self.click)
        return button


    # click function tells when button pressed
    def click(self, event):
        print("Button pressed")
        print('Yummy')



if __name__ == "__main__":
    Tamagochi2App().run()
