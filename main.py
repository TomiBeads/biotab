import flet as ft
from pyairtable.formulas import match
from pyairtable import Api
import principal as pr


# Configura tus datos reales de Airtable aquí
API_KEY = "tu_api_key_real"
BASE_ID = "tu_base_id_real"
TABLE_NAME = "Usuario"
api = Api(API_KEY)
base = api.base(BASE_ID)
at = base.table(TABLE_NAME)

def main(page: ft.Page):
    # Función para ingresar (simula login)
    def ingresar(e: ft.ControlEvent):
        usuario = txt_usuario.value
        password = txt_contra.value

        if not usuario or not password:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor ingresa usuario y contraseña"))
            page.snack_bar.open = True
            page.update()
            return

        try:
            formula = match({"clave": usuario, "contra": password})
            registro = at.first(formula=formula)

            if registro:
                print("Funciona!")
                page.clean()
                pr.main(page)
            else:
                print(f"Usuario '{usuario}' no encontrado.")
                page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"))
                page.snack_bar.open = True
                page.update()

        except Exception as error:
            print(f"Error de Airtable: {error}")
            page.snack_bar = ft.SnackBar(ft.Text(f"Error en conexión: {error}"))
            page.snack_bar.open = True
            page.update()

    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesión"
    page.window_width = 800
    page.window_height = 600
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

    # Componentes de la página
    logo = ft.Icon("person", size=60, color=ft.Colors.BLUE_300)

    page.appbar = ft.AppBar(
        title=ft.Text("Bienvenid@", font_family="Kanit"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor=ft.Colors.BLUE_900,
    )

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

    page.add(logo, txt_usuario, txt_contra, btn_login)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)  