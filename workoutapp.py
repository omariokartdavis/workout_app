from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class FailedLoginPopup(Popup):
    pass

class NewAccountPopup(Popup):
    
    def add_credentials(self):
        LoginScreen.login_credentials[self.new_username.text] = self.new_password.text
    
class LoginScreen(Screen):
    username = ObjectProperty()
    password = ObjectProperty()
    new_username: ObjectProperty()
    new_password: ObjectProperty()
    
    login_credentials = {'omari' : 'davis', '' : ''}
    
    def check_credentials(self):
        
        if self.username.text in self.login_credentials and self.password.text == self.login_credentials[self.username.text]:
            self.username.text = ""
            self.password.text = ""
            self.manager.transition.direction = "up"
            self.manager.transition.duration = 1
            self.manager.current = "macrocycle_screen"
        else:
            self.username.text = ""
            self.password.text = ""
            self.failed_login()
        
    def failed_login(self):
        the_popup = FailedLoginPopup()
        the_popup.open()

    def new_account(self):
        the_popup = NewAccountPopup()
        the_popup.open()
        
class MainMenuScreen(Screen):
    pass

class MacrocycleScreen(Screen):
    pass

class MesocycleScreen(Screen):
    pass

class MicrocycleScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class WorkoutApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return

sample_app = WorkoutApp()
sample_app.run()
