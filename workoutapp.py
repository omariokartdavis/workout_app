from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class WorkoutApp(App):
    pass

sample_app = WorkoutApp()
sample_app.run()
