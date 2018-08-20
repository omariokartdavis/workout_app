from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class FailedLoginPopup(Popup):
    pass

class InvalidUsernameCreationPopup(Popup):
    pass

class InvalidPasswordCreationPopup(Popup):
    pass

class UsernameAlreadyExistsPopup(Popup):
    pass

class NewAccountPopup(Popup):
    
    valid_email_accounts = ['@gmail', '@yahoo', '@hotmail', '@aol', '@earthlink']
    
    def validate_new_account(self):
        if any(key in self.new_username.text for key in self.valid_email_accounts):
            if self.new_username.text in LoginScreen.login_credentials:
                the_popup = UsernameAlreadyExistsPopup()
                the_popup.open()
            if self.new_password.text in LoginScreen.login_credentials.values():
                the_popup = InvalidPasswordCreationPopup()
                the_popup.open()
            else:
                LoginScreen.login_credentials[self.new_username.text] = self.new_password.text
        else:
            the_popup = InvalidUsernameCreationPopup()
            the_popup.open()

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
            self.manager.current = "mainmenu_screen"
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
    
    added_athlete_spinner_text_input = ObjectProperty()
    spinner_values = ObjectProperty()
    
    athletes = {"first athlete" : "macrocycle_screen", 'second athlete' : 'mesocycle_screen'}
    
    def add_athlete(self):
        # adds athlete to the spinner, adds athlete to the athlete dictionary, clears the text field
        
        # I need to find a way to create a new screen with the athletes name that is
        # that athletes macrocycle screen. this new screen should be the value added to the
        # athletes dictionary
        # maybe create another class that is called NewAthlete() and has a super that is the macrocycle screen?
        # ^this would only give it the properties of the macro screen not all screens.

        #possibly add functionality so when you add an athlete it immediately takes you to
        # their macrocycle screen? Not sure if this would be good because then you have to go back
        # if you are trying to just add multiple athletes at once

        # think about group functionality. add a "group" of athletes that all have the same cycles but just
        # different individual values on the microcycle level

        #always have entered athletes show up with First Letter Capitolized?
        self.spinner_values.values.append(self.added_athlete_spinner_text_input.text)
        self.athletes[self.added_athlete_spinner_text_input.text] = "microcycle_screen"
        self.added_athlete_spinner_text_input.text = ''
        
    def athlete_picked(self, value):
        
        if value in self.athletes:
            self.manager.transition.direction = "up"
            self.manager.transition.duration = 1
            self.manager.current = self.athletes[value]
            self.spinner_values.text = "Athletes"
        else:
            # do something if athlete is not in dictionary. popup that says add athlete first?
            # technically this should never happen as a name in the spinner has to be added
            # to it via the add athlete button or has to be preloaded by me
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
