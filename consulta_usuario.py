import flet as ft
import airtable as at

def main(page: ft.Page):
    page.title = "Consulta"
    page.theme_mode = "light"
    page.window.height = 600
    page.window.width = 800
    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de los usuarios en la nube"),
        leading=ft.Icon("cloud"),
        center_title=True,
        bgcolor="green",
        color="white"
    )
    #Tabla de usuarios
    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre completo")),
        ft.DataColumn(ft.Text("Es administrador"))
    ]
    filas = []
    datos = at.Usuario.all()
    for d in datos:
        celda = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra, color="white", selectable=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Text(d.admin))
        fila = ft.DataRow([celda, celda2, celda3, celda4])
        filas.append(fila)
    tbl_usuarios = ft.DataTable(encabezado, filas)
    
    page.add(tbl_usuarios)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)