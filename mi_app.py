import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Creamos la pantalla principal para el menú
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        
        # Creamos un título
        self.add_widget(Label(text="¡Bienvenido a MotoTech!", size_hint_y=0.2))

        # Creamos los botones del menú
        btn_register_client = Button(text="1. Registrar un nuevo cliente")
        btn_register_maintenance = Button(text="2. Registrar un mantenimiento")
        btn_view_history = Button(text="3. Ver historial de mantenimientos")
        btn_exit = Button(text="4. Salir")

        # Añadimos los botones a la pantalla
        self.add_widget(btn_register_client)
        self.add_widget(btn_register_maintenance)
        self.add_widget(btn_view_history)
        self.add_widget(btn_exit)

class MotoTechApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MotoTechApp().run()





