import flet as ft
from simpledt import SQLDataTable

def main(page: ft.Page):
    #configuracion de la pagina
    page.title = "Consultas"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.appbar = ft.AppBar(
        title = ft.Text("Lista de usuarios"),
        center_title=True,
        leading = ft.Icon("people"),
        bgcolor = "blue", 
        color = "white"
    )

    base_datos = SQLDataTable("sqlite", "base_datos.db", "usuario")
    tbl_usuario = base_datos.datatable

    page.add(tbl_usuario)
    page.update()
if __name__ == "__main__":
    ft.app(target=main)