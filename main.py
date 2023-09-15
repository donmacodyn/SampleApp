import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.2.1')


class SplashScreen(BoxLayout):
    def __init__(self):
        super(SplashScreen, self).__init__()


class SampleApp(App):
    def build(self):
        return SplashScreen()


if __name__ == '__main__':
    app = SampleApp()
    app.run()
