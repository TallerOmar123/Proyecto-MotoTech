import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import mototech_logic
mototech_logic.cargar_datos()

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# Creamos la pantalla principal para el menú
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # Creamos un layout para organizar los widgets verticalmente
        menu_layout = BoxLayout(orientation="vertical")

        # Creamos un título
        menu_layout.add_widget(Label(text="¡Bienvenido a MotoTech!", size_hint_y=0.2))

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

        # Añadimos los botones al layout
        menu_layout.add_widget(btn_register_client)
        menu_layout.add_widget(btn_register_maintenance)
        menu_layout.add_widget(btn_view_history)
        menu_layout.add_widget(btn_guardar_datos)
        menu_layout.add_widget(btn_exit)

        # Añadimos el layout principal a la pantalla
        self.add_widget(menu_layout)
    
    # Funciones que se llamarán al presionar cada botón
    def ir_a_registrar_cliente(self, instance):
        self.manager.current = 'register_client'

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

# La nueva clase para la pantalla de registro
class RegisterClientScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterClientScreen, self).__init__(**kwargs)

        # Creamos un layout para organizar los widgets verticalmente
        main_layout = BoxLayout(orientation="vertical")

        # Título de la pantalla
        main_layout.add_widget(Label(text="Registro de un Nuevo Cliente", size_hint_y=0.1))

        # Cuadrícula para organizar los campos de texto y etiquetas
        form_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.7, padding=20)
        
        # Widgets para el nombre
        form_layout.add_widget(Label(text="Nombre:"))
        self.name_input = TextInput(multiline=False)
        form_layout.add_widget(self.name_input)

        # Widgets para el teléfono
        form_layout.add_widget(Label(text="Teléfono:"))
        self.phone_input = TextInput(multiline=False)
        form_layout.add_widget(self.phone_input)

        # Widgets para el modelo de moto
        form_layout.add_widget(Label(text="Modelo de Moto:"))
        self.bike_model_input = TextInput(multiline=False)
        form_layout.add_widget(self.bike_model_input)

        # Añadimos la cuadrícula al layout principal
        main_layout.add_widget(form_layout)

        # Mensaje de confirmación (inicialmente vacío)
        self.message_label = Label(text="", size_hint_y=0.1)
        main_layout.add_widget(self.message_label)
        
        # Botones de acción
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        btn_register = Button(text="Registrar Cliente")
        btn_back = Button(text="Volver")
        
        buttons_layout.add_widget(btn_register)
        buttons_layout.add_widget(btn_back)
        main_layout.add_widget(buttons_layout)

        # Finalmente, añadimos el layout principal a la pantalla
        self.add_widget(main_layout)

class MotoTechApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(RegisterClientScreen(name='register_client'))
        return sm


if __name__ == '__main__':
    MotoTechApp().run()


