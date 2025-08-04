import flet as ft
import airtable as at

def main(page: ft.Page):

    def guardar_usuario(e: ft.ControlEvent): 
        clave = Text_clave.value
        contra = Text_contra.value
        contra2 = Text_contra2.value
        nombre = Text_nombre.value
        #Validar campos
        if clave == "":
            snackbar  = ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return
        if contra == "":
            snackbar  = ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return
        if contra2 == "":
            snackbar  = ft.SnackBar(ft.Text("Introduce tu confirmacion de contraseña"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return
        if nombre == "":
            snackbar  = ft.SnackBar(ft.Text("Introduce tu nombre de usuario"), bgcolor="orange", show_close_icon=True)
            page.open(snackbar)
            return
        #Confirmar contraseña
        if contra != contra2:
            snackbar  = ft.SnackBar(ft.Text("Contraseñas Incorrectas"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
            return
        #Guardar los datos del usuario en la nube
        nuevo = at.Usuario(
            clave=clave, 
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value
        )
        try:
            nuevo.save()
            snackbar = ft.SnackBar(ft.Text("Usuario registrado"), bgcolor="blue", show_close_icon=True)
            page.open(snackbar)
        except Exception as error:
            snackbar = ft.SnackBar(ft.Text(error), bgcolor="red", show_close_icon=True)
            page.open(snackbar)


    #Configuracion de la pagina
    page.title="Altas"
    page.theme_mode ="light"
    page.window.width =800
    page.window.height = 600
    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo Usuario"),
        center_title=True,
        leading=ft.Icon("Person_add"),
        color="white", 
        bgcolor="blue"
    )

    #Componentes de la pagina
    Text_clave = ft.TextField(label="Clave del usuario")
    Text_contra = ft.TextField(label="Contraseña", password=True)
    Text_contra2 = ft.TextField(label="Confirmar contraseña", password=True)
    Text_nombre = ft.TextField(label="Nombre completo",)
    chk_admin = ft.Checkbox(label="¿Eres Administrador?")
    btm_guardar = ft.FilledButton(
        text="Guardar",
        icon=ft.Icon("Save"),
        on_click=guardar_usuario,
        bgcolor="green"
    )

    btm_cancelar = ft.FilledButton(
        text="Cancelar",
        icon="Cancel",
        bgcolor="red"
    )
    fila = ft.Row(controls=[btm_guardar, btm_cancelar])

    #Añadir componentes a la pagina
    page.add(Text_clave, Text_contra, Text_contra2, Text_nombre, chk_admin, fila)

    page.update()

ft.app(target=main)