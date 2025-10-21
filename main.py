import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    ia_mag = ft.TextField(
        label="IA Mag",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Only numbers"
    )

    ia_ang = ft.TextField(
        label="IA Angle (degrees)",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Only numbers"
    )

    ib_mag = ft.TextField(
        label="IA Mag",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Only numbers"
    )

    ib_ang = ft.TextField(
        label="IA Angle (degrees)",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Only numbers"
    )

    ic_mag = ft.TextField(
        label="IA Mag",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Only numbers"
    )

    ic_ang = ft.TextField(
        label="IA Angle (degrees)",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Only numbers"
    )

    def generate_chart(e):
        phasors = [
            (float(ia_mag.value), float(ia_ang.value)),
            (float(ib_mag.value), float(ib_ang.value)),
            (float(ic_mag.value), float(ic_ang.value)),
        ]

        fig, ax = plt.subplots(figsize=(page.width/100, page.height/100))

        # Limit the chart size and axis
        max_mod = max(m for m, _ in phasors)
        limite = max_mod * 1.2

        # Chart Setup
        ax.set_aspect("equal")
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-limite, limite)
        ax.set_title("Phasors")
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
        ax.grid(True)

        # Plotting the phasors
        colors_list = ['tab:red', 'tab:blue', 'tab:green']

        for i, (module, ang_deg) in enumerate(phasors):
            ang_rad = np.deg2rad(ang_deg)
            x = module * np.cos(ang_rad)
            y = module * np.sin(ang_rad)
            ax.quiver(
                0, 0, x, y,
                angles="xy", scale_units="xy", scale=1,
                color=colors_list[i % len(colors_list)]
            )
            ax.text(x * 1.05, y * 1.05, f"{module}∠{ang_deg}°")

            # 🔹 Limpa o gráfico anterior e adiciona o novo
            chart_view.controls.clear()
            chart_view.controls.append(MatplotlibChart(fig, expand=True))
            page.update()


    # 🔹 Botão para gerar o gráfico
    btn_generate_chart = ft.ElevatedButton("Gerar Gráfico", on_click=generate_chart)

    # 🔹 Container do gráfico
    chart_view = ft.Column()

    page.add(chart_view, ia_mag, ia_ang, ib_mag, ib_ang, ic_mag, ic_ang, btn_generate_chart)

ft.app(main)
