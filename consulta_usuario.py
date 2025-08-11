# consulta_usuario.py
import flet as ft
import airtable as at
import principal as pr  # importa el archivo que contiene tu menú principal

def main(page: ft.Page):
    page.title = "Consulta"
    page.theme_mode = "light"
    page.window.width = 500
    page.window.height = 650
    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de Usuario en la Nube"),
        leading=ft.Icon("cloud"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_900,
        color="white"
    )

    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre Completo")),
        ft.DataColumn(ft.Text("Es Administrador"))
    ]

    filas = []
    datos = at.usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra, color="white", selectable=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Text(d.admin))
        fila = ft.DataRow([celda1, celda2, celda3, celda4])
        filas.append(fila)

    tbl_usuarios = ft.DataTable(encabezado, filas)

    def regresar_al_menu(e: ft.ControlEvent):
        page.clean()
        pr.main(page)  # vuelve a la página principal

    btn_regresar = ft.ElevatedButton("Regresar",color= "White", icon= "ARROW_BACK",icon_color="white", bgcolor= "BLACK12", on_click=regresar_al_menu)

    page.clean()
    page.add(btn_regresar, tbl_usuarios)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)