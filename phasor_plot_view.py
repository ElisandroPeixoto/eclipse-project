import flet as ft
from matplotlib import pyplot as plt

from chart_utils import create_phasor_chart
from flet.matplotlib_chart import MatplotlibChart


def phasor_plot_screen(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    ia_mag = ft.TextField(label="IA Mag", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Only numbers")
    ia_ang = ft.TextField(label="IA Angle (degrees)", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Only numbers")

    ib_mag = ft.TextField(label="IA Mag", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Only numbers")
    ib_ang = ft.TextField(label="IA Angle (degrees)", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Only numbers")

    ic_mag = ft.TextField(label="IA Mag", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Only numbers")
    ic_ang = ft.TextField(label="IA Angle (degrees)", keyboard_type=ft.KeyboardType.NUMBER, hint_text="Only numbers")


    def empty_chart():
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_title("Phasor Chart")
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.grid(True)
        ax.set_aspect('equal')

        return fig

    chart1 = ft.Container(content=MatplotlibChart(empty_chart()), expand=True)
    chart2 = ft.Container(content=MatplotlibChart(empty_chart()), expand=True)

    chart_row = ft.Row(
        controls=[chart1, chart2],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
    )

    def generate_chart(e):
        phasors = [
            (float(ia_mag.value), float(ia_ang.value)),
            (float(ib_mag.value), float(ib_ang.value)),
            (float(ic_mag.value), float(ic_ang.value)),
        ]

        fig1 = create_phasor_chart(phasors, page.width / 2, page.height / 2)
        fig2 = create_phasor_chart(phasors, page.width / 2, page.height / 2)

        chart1.content = MatplotlibChart(fig1, expand=True)
        chart2.content = MatplotlibChart(fig2, expand=True)

        page.update()


    # Botão para gerar o gráfico
    btn_generate_chart = ft.ElevatedButton("Gerar Gráfico", on_click=generate_chart)



    return ft.Column(controls=[chart_row,
                               ia_mag,
                               ia_ang,
                               ib_mag,
                               ib_ang,
                               ic_mag,
                               ic_ang,
                               btn_generate_chart])
