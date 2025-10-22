import matplotlib
import flet as ft
from flet.matplotlib_chart import MatplotlibChart
from phasors_plot.chart_utils import create_phasor_chart

matplotlib.use("svg")


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    ia_mag = ft.TextField(label="IA Mag",keyboard_type=ft.KeyboardType.NUMBER,hint_text="Only numbers")
    ia_ang = ft.TextField(label="IA Angle (degrees)",keyboard_type=ft.KeyboardType.NUMBER,hint_text="Only numbers")

    ib_mag = ft.TextField(label="IA Mag",keyboard_type=ft.KeyboardType.NUMBER,hint_text="Only numbers")
    ib_ang = ft.TextField(label="IA Angle (degrees)",keyboard_type=ft.KeyboardType.NUMBER,hint_text="Only numbers")

    ic_mag = ft.TextField(label="IA Mag",keyboard_type=ft.KeyboardType.NUMBER,hint_text="Only numbers")
    ic_ang = ft.TextField(label="IA Angle (degrees)",keyboard_type=ft.KeyboardType.NUMBER,hint_text="Only numbers")

    def generate_chart(e):
        phasors = [
            (float(ia_mag.value), float(ia_ang.value)),
            (float(ib_mag.value), float(ib_ang.value)),
            (float(ic_mag.value), float(ic_ang.value)),
        ]

        fig = create_phasor_chart(phasors, page.width, page.height)

        chart_view.controls.clear()
        chart_view.controls.append(MatplotlibChart(fig, expand=True))

        page.update()


    # Botão para gerar o gráfico
    btn_generate_chart = ft.ElevatedButton("Gerar Gráfico", on_click=generate_chart)

    # Container do gráfico
    chart_view = ft.Column()

    page.add(chart_view, ia_mag, ia_ang, ib_mag, ib_ang, ic_mag, ic_ang, btn_generate_chart)

ft.app(main)
