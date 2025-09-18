import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: ft.Page):

    phasors = [
        (8000, 0),
        (8000, -120),
        (8000, 120),
    ]

    fig, ax = plt.subplots()

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

    page.add(MatplotlibChart(fig, expand=True))


ft.app(main)
