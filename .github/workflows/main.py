import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
class ButtonApp(App):    
    def build(self):
        # use a (r, g, b, a) tuple
        btn1 = Button(text ="devda sir",
                   font_size ="20sp",
                   #background_color =(1, 1, 1, 1),
                   #color =(1, 1, 1, 1),
                   size =(100, 32),
                   size_hint=(None, None),
                   pos =(25, 450))

        # bind() use to bind the button to function callback
        btn1.bind(on_press = self.callback)
        return btn1
    
    
    # callback function tells when button pressed
    def callback(self, event):
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')
        

root = ButtonApp()
root.run()
