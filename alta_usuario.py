import flet as ft
import airtable as at
import principal as pr  # módulo del menú principal
import main as mn       # módulo pantalla login

def main(page: ft.Page):
    def guardar_usuario(e: ft.ControlEvent):
        clave = Text_clave.value.strip()
        contra = Text_contra.value.strip()
        contra2 = Text_contra2.value.strip()
        nombre = Text_nombre.value.strip()

        # Validaciones
        if clave == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor="red", show_close_icon=True))
            return
        if contra == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor="red", show_close_icon=True))
            return
        if contra2 == "":
            page.open(ft.SnackBar(ft.Text("Confirma tu contraseña"), bgcolor="red", show_close_icon=True))
            return
        if nombre == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu nombre completo"), bgcolor="red", show_close_icon=True))
            return
        if contra != contra2:
            page.open(ft.SnackBar(ft.Text("Contraseñas incorrectas"), bgcolor="red", show_close_icon=True))
            return

        # Guardar datos en Airtable
        nuevo = at.usuario(
            clave=clave,
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value
        )
        try:
            nuevo.save()
            page.open(ft.SnackBar(ft.Text("Usuario registrado"), bgcolor="green", show_close_icon=True))
            # Limpiar campos después de guardar
            Text_clave.value = ""
            Text_contra.value = ""
            Text_contra2.value = ""
            Text_nombre.value = ""
            chk_admin.value = False
            page.update()
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(str(error)), bgcolor="red", show_close_icon=True))

    def regresar(e: ft.ControlEvent):
        page.clean()
        mn.main(page)  # Volver a la pantalla de login

    def principal(e: ft.ControlEvent):
        page.clean()
        pr.main(page)  # Ir al menú principal

    def iniciar_sesion(e: ft.ControlEvent):
        page.clean()
        mn.main(page)  # Ir a pantalla login

    # Configuración de la página
    page.title = "Altas"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 600
    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        center_title=True,
        leading=ft.Icon(ft.Icons.PERSON_ADD),
        color="white",
        bgcolor="blue"
    )


    # Componentes de la página 
    Text_clave = ft.TextField(label="Clave del usuario")
    Text_contra = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    Text_contra2 = ft.TextField(label="Confirmar contraseña", password=True, can_reveal_password=True)
    Text_nombre = ft.TextField(label="Nombre completo")
    chk_admin = ft.Checkbox(label="¿Eres Administrador?")


    btm_guardar = ft.FilledButton(
        text="Guardar",
        icon=ft.Icons.SAVE,
        on_click=guardar_usuario,
        bgcolor="green"
    )
    btm_cancelar = ft.FilledButton(
        text="Cancelar",
        icon=ft.Icons.CANCEL,
        bgcolor="red",
        on_click=regresar
    )
    btm_principal = ft.FilledButton(
        text="Regresar a menú",
        icon=ft.Icons.ARROW_BACK,
        bgcolor="blue",
        on_click=principal
    )
    btm_login = ft.FilledButton(
        text="Iniciar Sesión",
        icon=ft.Icons.LOGIN,
        bgcolor="blue",
        on_click=iniciar_sesion
    )


    fila_botones = ft.Row(
        controls=[btm_principal, btm_guardar, btm_cancelar, btm_login],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    # Agregar al page 
    page.add(Text_clave, Text_contra, Text_contra2, Text_nombre, chk_admin, fila_botones)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)