from pynotifier import Notification

nombre = "Titulo del Mensaje:"
texto = "Mensaje Que Quieras Mostrar, no hay limite para la cantidad de caracteres."
icono = "/home/user/directorio/.../"

Notification(title=nombre, description=texto, icon_path=icono, duration=30, urgency="normal",app_name="Hola").send()
