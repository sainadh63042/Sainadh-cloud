from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
 
 
class PopupApp(App):
    def build(self):
        btn = Button(text='Click here')
        btn.bind(on_press=self.show_popup)
        return btn
 
    def show_popup(self, instance):
        popup = Popup(title='hello world',
                      content=Button(text='hello world'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()
 
 
if __name__ == '__main__':
    PopupApp().run()
