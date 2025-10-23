import flet as ft
from phasor_plot_view import phasor_plot_screen


def route_handler(route: str, page: ft.Page):
    """Handles page navigation"""

    # Routes Dictionarie
    routes = {
        "/": {
            "view": phasor_plot_screen(page),
        }
    }

    page.controls.clear()

    # Look for the route configuration. If it does not exist, return 404
    route_config = routes.get(route, {
        "view": lambda: ft.Text("404 - Not Found")
    })

    page.add(route_config["view"])
    page.update()
