import flet as ft

def main (page: ft.Page):
    #configuracion de la pagina
    page.title = "Menu principal"
    page.theme_mode = "ligth"
    page.appbar = ft.AppBar(
        title= ft.Text("Sistema de Gestion de Bionergia"),
        leading=ft.Icon("energy_savings_leaf"),
        color="white",
        bgcolor="blue"
    )
    btm_registro = ft.ElevatedButton("Registro")
    btm_consultas = ft.ElevatedButton("Consultas")
    page.add(btm_registro, btm_consultas)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)