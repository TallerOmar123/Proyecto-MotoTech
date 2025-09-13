import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import mototech_logic
mototech_logic.cargar_datos()

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
        btn_guardar_datos = Button(text="Guardar datos")
        btn_exit = Button(text="4. Salir")

        # Asignamos acciones a cada botón
        btn_register_client.bind(on_press=self.ir_a_registrar_cliente)
        btn_register_maintenance.bind(on_press=self.ir_a_registrar_mantenimiento)
        btn_view_history.bind(on_press=self.ir_a_ver_historial)
        btn_guardar_datos.bind(on_press=self.guardar_datos_app)
        btn_exit.bind(on_press=self.salir_app)

        # Añadimos los botones a la pantalla
        self.add_widget(btn_register_client)
        self.add_widget(btn_register_maintenance)
        self.add_widget(btn_view_history)
        self.add_widget(btn_guardar_datos)
        self.add_widget(btn_exit)

    # Funciones que se llamarán al presionar cada botón
    def ir_a_registrar_cliente(self, instance):
        print("Botón 'Registrar un nuevo cliente' presionado.")

    def ir_a_registrar_mantenimiento(self, instance):
        print("Botón 'Registrar un mantenimiento' presionado.")

    def ir_a_ver_historial(self, instance):
        print("Botón 'Ver historial de mantenimientos' presionado.")

    def salir_app(self, instance):
        App.get_running_app().stop()
        print("Saliendo de la aplicación.")

    def guardar_datos_app(self, instance):
        mototech_logic.guardar_datos()
        print("Botón 'Guardar datos' presionado.")

class MotoTechApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MotoTechApp().run()



