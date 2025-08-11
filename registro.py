import flet as ft
import airtable as at  
import principal as pr
import consulta as c

# Lista de municipios de Tabasco
municipios_tabasco = [
    "Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco", "Cunduacán",
    "Emiliano Zapata", "Huimanguillo", "Jalapa", "Jalpa de Méndez", "Jonuta",
    "Macuspana", "Nacajuca", "Paraíso", "Tacotalpa", "Teapa", "Tenosique"
]

def main(page: ft.Page):

    # Crear SnackBar para mensajes dinámicos
    snackbar = ft.SnackBar(content=ft.Text(""), bg_color="YELLOW", action="Cerrar", on_action=lambda e: snackbar.close())
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
    
    # Campos de texto
    latitud = ft.TextField(width=200)
    longitud = ft.TextField(width=200)
    cantidad = ft.TextField(width=200)
    humedad = ft.TextField(width=200)
    area_cultivada = ft.TextField(width=200)
    contenido_energetico = ft.TextField(width=200)

    # Función mostrar mensaje Snackbar
    def mostrar_snackbar(mensaje: str, color: str):
        snackbar.content = ft.Text(mensaje)
        snackbar.bgcolor = color
        snackbar.open = True
        page.update()

    # Función para registrar (con validaciones y guardado)
    def registrar_biomasa(e: ft.ControlEvent):
        cultivo = cultivo_origen.value
        parte = parte_aprovechada.value
        municipio_seleccionado = municipio.value
        lat_str = latitud.value.strip()
        lon_str = longitud.value.strip()
        cantidad_str = cantidad.value.strip()
        area_str = area_cultivada.value.strip()
        energia_str = contenido_energetico.value.strip()

        # Validaciones
        if not cultivo:
            mostrar_snackbar("Selecciona un Cultivo", "RED")
            return
        if not parte:
            mostrar_snackbar("Selecciona la Parte Aprovechada", "RED")
            return
        if not municipio_seleccionado:
            mostrar_snackbar("Selecciona un Municipio", "RED")
            return
        if not cantidad_str or not cantidad_str.replace(".", "", 1).isdigit() or float(cantidad_str) <= 0:
            mostrar_snackbar("Introduce una Cantidad válida (> 0)", "RED")
            return
        if not area_str or not area_str.replace(".", "", 1).isdigit() or float(area_str) <= 0:
            mostrar_snackbar("Introduce un Área Cultivada válida (> 0)", "RED")
            return
        if not energia_str or not energia_str.replace(".", "", 1).isdigit() or float(energia_str) <= 0:
            mostrar_snackbar("Introduce un Contenido Energético válido (> 0)", "RED")
            return

        try:
            cantidad_val = float(cantidad_str)
            area_val = float(area_str)
            energia_val = float(energia_str)
            lat_val = float(lat_str) if lat_str else 0.0
            lon_val = float(lon_str) if lon_str else 0.0

            nuevo = at.Bioenergia(
                cultivo=cultivo,
                parte=parte,
                cantidad=cantidad_val,
                area=area_val,
                energia=energia_val,
                municipio=municipio_seleccionado,
                latitud=lat_val,
                longitud=lon_val
            )
            nuevo.save()

            mostrar_snackbar("Registro guardado correctamente", "GREEN")

            # Limpiar campos después de guardar
            cultivo_origen.value = None
            parte_aprovechada.value = None
            municipio.value = None
            latitud.value = ""
            longitud.value = ""
            cantidad.value = ""
            humedad.value = ""  # Aunque no se usa para guardar, limpiamos
            area_cultivada.value = ""
            contenido_energetico.value = ""

            page.update()

        except Exception as error:
            mostrar_snackbar(f"Error en guardar registro: {error}", "RED")

    btn_registrar = ft.FilledButton("Registrar Biomasa", on_click=registrar_biomasa, bgcolor="BLUE", width=250)

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
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
