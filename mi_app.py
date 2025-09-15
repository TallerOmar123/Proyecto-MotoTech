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
        self.manager.current = 'register_maintenance' 

    def ir_a_ver_historial(self, instance):
        self.manager.current = 'maintenance_history'

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
        btn_register.bind(on_press=self.registrar_cliente)
        btn_back = Button(text="Volver")
        
        buttons_layout.add_widget(btn_register)
        buttons_layout.add_widget(btn_back)
        main_layout.add_widget(buttons_layout)

        # Finalmente, añadimos el layout principal a la pantalla
        self.add_widget(main_layout)

class RegisterMaintenanceScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterMaintenanceScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation="vertical")
        
        main_layout.add_widget(Label(text="Registro de Mantenimiento", font_size='24sp', size_hint_y=0.1))
        
        form_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.7, padding=20)
        
        # Widgets para la matrícula de la moto
        form_layout.add_widget(Label(text="Matrícula de la moto:"))
        self.bike_plate_input = TextInput(multiline=False)
        form_layout.add_widget(self.bike_plate_input)

        # Widgets para la fecha del mantenimiento
        form_layout.add_widget(Label(text="Fecha del mantenimiento:"))
        self.date_input = TextInput(multiline=False, hint_text='Ej: 25/10/2025')
        form_layout.add_widget(self.date_input)

        # Widgets para la descripción del servicio
        form_layout.add_widget(Label(text="Servicio realizado:", valign='top'))
        self.service_input = TextInput(multiline=True)
        form_layout.add_widget(self.service_input)

        # Widgets para el costo
        form_layout.add_widget(Label(text="Costo:"))
        self.cost_input = TextInput(multiline=False, input_filter='float')
        form_layout.add_widget(self.cost_input)
        
        main_layout.add_widget(form_layout)
        
      

        # Botones de acción
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)

        btn_register_maintenance = Button(text="Registrar Mantenimiento")
        btn_register_maintenance.bind(on_press=self.registrar_mantenimiento)

        # Widgets para el vover
        btn_back = Button(text="Volver")
        btn_back.bind(on_press=self.volver_al_menu)

        buttons_layout.add_widget(btn_register_maintenance)
        buttons_layout.add_widget(btn_back)
        
        main_layout.add_widget(buttons_layout)

        
        self.add_widget(main_layout)

    def volver_al_menu(self, instance):
        self.manager.current = 'main'


    def registrar_mantenimiento(self, instance):
    # Recupera los datos de los campos de texto
        matricula = self.bike_plate_input.text
        fecha = self.date_input.text
        servicio = self.service_input.text
        self.cost_input.text = ""

    # Llama a la lógica de negocio para guardar el mantenimiento
    # Asegúrate de que mototech_logic.registrar_mantenimiento está creado y recibe 4 argumentos
        mototech_logic.registrar_mantenimiento(matricula, fecha, servicio, costo)

    # Opcional: muestra un mensaje de confirmación
        print(f"Mantenimiento registrado para la moto con matrícula: {matricula}")
    
    # Opcional: limpia los campos de texto
        self.bike_plate_input.text = ""
        self.date_input.text = ""
        self.service_input.text = ""
        self.cost_input = "" 


class MaintenanceHistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(MaintenanceHistoryScreen, self).__init__(**kwargs)
        self.main_layout = BoxLayout(orientation="vertical")
        
        # Título de la pantalla
        self.main_layout.add_widget(Label(text="Historial de Mantenimientos", font_size='24sp', size_hint_y=0.1))
        
        # Layout para la lista de mantenimientos
        self.history_layout = BoxLayout(orientation='vertical', spacing=5, padding=10)
        self.main_layout.add_widget(self.history_layout)

        # Botón para volver
        btn_back = Button(text="Volver", size_hint_y=0.1)
        btn_back.bind(on_press=self.volver_al_menu)
        self.main_layout.add_widget(btn_back)
        
        self.add_widget(self.main_layout)

    # Función que se ejecuta cada vez que la pantalla se muestra
    def on_enter(self, *args):
        self.actualizar_historial()

    def actualizar_historial(self):
        # Limpia el contenido anterior del historial
        self.history_layout.clear_widgets()

        # Obtiene la lista de mantenimientos
        mantenimientos = mototech_logic.obtener_mantenimientos()

        if not mantenimientos:
            self.history_layout.add_widget(Label(text="No hay mantenimientos registrados."))
        else:
            for mantenimiento in mantenimientos:
                info = f"Matrícula: {mantenimiento['matricula']} | Fecha: {mantenimiento['fecha']} | Servicio: {mantenimiento['servicio']} | Costo: {mantenimiento['costo']}"
                self.history_layout.add_widget(Label(text=info, size_hint_y=None, height=40))

    def volver_al_menu(self, instance):
        self.manager.current = 'main'



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
        btn_register.bind(on_press=self.registrar_cliente) # <--- AHORA CON LA FUNCIÓN EXISTENTE
        btn_back = Button(text="Volver")
        btn_back.bind(on_press=self.volver_al_menu)
        
        buttons_layout.add_widget(btn_register)
        buttons_layout.add_widget(btn_back)
        main_layout.add_widget(buttons_layout)

        # Finalmente, añadimos el layout principal a la pantalla
        self.add_widget(main_layout)

    # --- AQUÍ EMPIEZAN LAS FUNCIONES DE LA CLASE ---

    def volver_al_menu(self, instance):
        self.manager.current = 'main'
    
    
    def registrar_cliente(self, instance):
        nombre = self.name_input.text
        telefono = self.phone_input.text
        modelo_moto = self.bike_model_input.text
        
        mototech_logic.registrar_cliente(nombre, telefono, modelo_moto)
        
        self.message_label.text = "Cliente registrado con éxito."
        
        self.name_input.text = ""
        self.phone_input.text = ""
        self.bike_model_input.text = ""

class MotoTechApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(RegisterClientScreen(name='register_client'))
        sm.add_widget(RegisterMaintenanceScreen(name='register_maintenance')) 
        sm.add_widget(MaintenanceHistoryScreen(name='maintenance_history')) # <--- ¡AÑADE ESTA LÍNEA!
        return sm


if __name__ == '__main__':
    MotoTechApp().run()


