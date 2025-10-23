import matplotlib
import flet as ft
from routes import route_handler


matplotlib.use("svg")


def main(page: ft.Page):

    def on_route_change(e):
        route_handler(page.route, page)

    page.on_route_change = on_route_change
    page.go(page.route)


ft.app(target=main)
