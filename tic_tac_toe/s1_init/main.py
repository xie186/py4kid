# import the kivy module into our python file
from kivy.app import App

# import the label and button class from kivy
from kivy.uix.label import Label
from kivy.uix.button import Button

#import the BoxLayout widget class from kivy so 
#that we can return these label and button widgets to the main app
from kivy.uix.boxlayout import BoxLayout

class FirstApp(App):
    pass

if __name__ == "__main__":
    FirstApp().run()

