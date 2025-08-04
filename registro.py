import flet as ft

# Lista de municipios de Tabasco 
municipios_tabasco = [
    "Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco", "Cunduacán",
    "Emiliano Zapata", "Huimanguillo", "Jalapa", "Jalpa de Méndez", "Jonuta",
    "Macuspana", "Nacajuca", "Paraíso", "Tacotalpa", "Teapa", "Tenosique"
]

def main(page: ft.Page):

    # Crear SnackBar para mensajes
    snackbar = ft.SnackBar(content=ft.Text(""), bgcolor="yellow", show_close_icon=True)
    page.snack_bar = snackbar

    # Campos desplegables
    cultivo_origen = ft.Dropdown(
        label="Cultivo Origen",
        options=[
            ft.dropdown.Option("Caña de Azúcar"),
            ft.dropdown.Option("Cacao"),
            ft.dropdown.Option("Maíz"),
            ft.dropdown.Option("Coco"),
            ft.dropdown.Option("Plátano"),
        ],
        width=250,
    )

    parte_aprovechada = ft.Dropdown(
        label="Parte Aprovechada",
        options=[
            ft.dropdown.Option("Tallo"),
            ft.dropdown.Option("Cáscara"),
            ft.dropdown.Option("Bagazo"),
            ft.dropdown.Option("Rastrojo"),
        ],
        width=250,
    )

    municipio = ft.Dropdown(
        label="Municipio",
        options=[ft.dropdown.Option(m) for m in municipios_tabasco],
        width=250,
    )

    # Función para crear fila con etiqueta a la izquierda y cuadro a la derecha
    def fila_etiqueta_campo(etiqueta_texto, campo_texto):
        return ft.Row(
            [
                ft.Container(ft.Text(etiqueta_texto, size=16), width=150, alignment=ft.alignment.center_left),
                campo_texto
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            width=400
        )

    # Campos de texto
    latitud = ft.TextField(width=200)
    longitud = ft.TextField(width=200)
    cantidad = ft.TextField(width=200)
    humedad = ft.TextField(width=200)
    area_cultivada = ft.TextField(width=200)
    contenido_energetico = ft.TextField(width=200)

    def registrar_biomasa(e: ft.ControlEvent):
        snackbar.content = ft.Text("Registro guardado correctamente")
        snackbar.open = True
        page.update()

    btn_registrar = ft.FilledButton("Registrar Biomasa", on_click=registrar_biomasa, bgcolor="blue", width=250)

    # Agrupar los dropdowns en una fila 
    dropdowns_row = ft.Row(
        [cultivo_origen, parte_aprovechada, municipio],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
    )

    # Centrar contenido de la página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Registro"
    page.window_width = 600  
    page.window_height = 800

    # Añadir controles a la página
    page.add(
        ft.Text("Registro de Biomasa en Tabasco", size=30, weight="bold"),
        dropdowns_row,
        fila_etiqueta_campo("Latitud:", latitud),
        fila_etiqueta_campo("Longitud:", longitud),
        fila_etiqueta_campo("Cantidad (ton):", cantidad),
        fila_etiqueta_campo("% Humedad:", humedad),
        fila_etiqueta_campo("Área Cultivada:", area_cultivada),
        fila_etiqueta_campo("Contenido Energético:", contenido_energetico),
        btn_registrar,
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
