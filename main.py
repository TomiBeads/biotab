import flet as ft
from pyairtable.formulas import match
from pyairtable import Api
import principal as pr
import alta_usuario as al 

# Configura tus datos reales de Airtable
API_KEY = "tu_api_key_real"
BASE_ID = "tu_base_id_real"
TABLE_NAME = "Usuario"
api = Api(API_KEY)
base = api.base(BASE_ID)
at = base.table(TABLE_NAME)

def main(page: ft.Page):
    # Barra de mensajes global para evitar superposición
    snackbar = ft.SnackBar(content=ft.Text(""), bgcolor="yellow", show_close_icon=True)
    page.snack_bar = snackbar

    # Función para mostrar pantalla de registro 
    def mostrar_registro(e: ft.ControlEvent):
        page.clean()
        al.main(page)  # O módulo que maneje el registro

    # Función para ingresar 
    def ingresar(e: ft.ControlEvent):
        usuario_valor = txt_usuario.value.strip()
        password_valor = txt_contra.value.strip()

        # Validaciones previas
        if not usuario_valor:
            page.snack_bar.content = ft.Text("Introduce tu usuario")
            page.snack_bar.bgcolor = "red"
            page.snack_bar.open = True
            page.update()
            return

        if not password_valor:
            page.snack_bar.content = ft.Text("Introduce tu contraseña")
            page.snack_bar.bgcolor = "red"
            page.snack_bar.open = True
            page.update()
            return

        try:
            formula = match({"clave": usuario_valor, "contra": password_valor})
            registro = at.first(formula=formula)

            if registro:
                page.snack_bar.content = ft.Text("Inicio de sesión exitoso")
                page.snack_bar.bgcolor = "green"
                page.snack_bar.open = True
                page.update()
                page.clean()
                pr.main(page)  # Ir al menú principal
            else:
                page.snack_bar.content = ft.Text("Usuario o contraseña incorrectos")
                page.snack_bar.bgcolor = "red"
                page.snack_bar.open = True
                page.update()

        except Exception as error:
            page.snack_bar.content = ft.Text(f"Error de conexión: {error}")
            page.snack_bar.bgcolor = "red"
            page.snack_bar.open = True
            page.update()

    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesión"
    page.window_width = 800
    page.window_height = 600

    # Componentes Visuales
    logo = ft.Icon(ft.Icons.PERSON, size=60, color=ft.Colors.BLUE_300)

    global txt_usuario, txt_contra
    txt_usuario = ft.TextField(label="Username/Correo", width=250)
    txt_contra = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=250
    )

    btn_login = ft.FilledButton(
        "Iniciar sesión",
        icon=ft.Icons.LOGIN,
        width=300,
        color="black",
        bgcolor=ft.Colors.BLACK12,
        on_click=ingresar
    )

    # Botón para ir a Registro
    btn_registro = ft.FilledButton(
        "Registro",
        icon=ft.Icons.PERSON_ADD,
        width=300,
        color="white",
        bgcolor=ft.Colors.GREEN,
        on_click=mostrar_registro
    )

    # Barra superior
    page.appbar = ft.AppBar(
        title=ft.Text("Bienvenid@", font_family="Kanit"),
        center_title=True,
        leading=ft.Icon(ft.Icons.PERSON_ADD),
        color="white",
        bgcolor=ft.Colors.BLUE_900,
    )

    # Agregar controles a la página 
    page.add(logo, txt_usuario, txt_contra, btn_login, btn_registro)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)