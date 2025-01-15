import flet
import time


class Sidebar(flet.Container):
    def __init__(self, ):
        super().__init__(
            bgcolor="black",
            width=200,
            alignment=flet.alignment.center,
            padding=flet.Padding(top=15, left=10, right=10, bottom=0),
            animate=flet.animation.Animation(
                duration=300,
                curve=flet.AnimationCurve.DECELERATE
            ),
            content=flet.Column(
                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                controls=[
                    self.datos_usuarios(
                        iniciales="RF",
                        nombre="Ricardo Freccero",
                        descripcion="Ingeniero en Sistemas"
                    ),
                    flet.IconButton(
                        icon=flet.Icons.ARROW_BACK_IOS_ROUNDED,
                        on_click=self.animar_sidebar,
                        bgcolor=flet.Colors.WHITE10,
                        icon_color=flet.Colors.WHITE54,
                    ),
                    flet.Divider(
                        height=5,
                        color=flet.Colors.TRANSPARENT,
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.SEARCH,
                        texto="Search",
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.DASHBOARD_ROUNDED,
                        texto="Dashboard",
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.BAR_CHART,
                        texto="Revenue",
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.NOTIFICATIONS,
                        texto="Norifications",
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.PIE_CHART_ROUNDED,
                        texto="Analytics",
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.FAVORITE_ROUNDED,
                        texto="Likes",
                    ),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.WALLET_ROUNDED,
                        texto="Wallet",
                    ),
                    flet.Divider(height=5, color=flet.Colors.WHITE54),
                    self.icono_sidebar(
                        nombre_icono=flet.Icons.LOGOUT_ROUNDED,
                        texto="Logout",
                    ),
                ]
            )
        )

    def resaltar(self, e):
        if e.data == "true":
            e.control.bgcolor = flet.Colors.WHITE10
            e.control.content.controls[0].icon_color = flet.Colors.WHITE
            e.control.content.controls[1].color = flet.Colors.WHITE
            e.control.update()
        else:
            e.control.bgcolor = None
            e.control.content.controls[0].icon_color = flet.Colors.WHITE54
            e.control.content.controls[1].color = flet.Colors.WHITE54
            e.control.update()

    def datos_usuarios(self, iniciales, nombre, descripcion):
        return flet.Container(
            content=flet.Row(
                controls=[
                    flet.Container(
                        width=42,
                        height=42,
                        bgcolor=flet.Colors.BLUE_GREY_900,
                        alignment=flet.alignment.center,
                        border_radius=8,
                        content=flet.Text(
                            value=iniciales,
                            size=20,
                            weight=flet.FontWeight.BOLD,
                        )
                    ),
                    flet.Column(
                        spacing=1,
                        alignment=flet.MainAxisAlignment.CENTER,
                        controls=[
                            flet.Text(
                                value=nombre,
                                size=11,
                                weight=flet.FontWeight.BOLD,
                                opacity=1,
                                animate_opacity=200,
                            ),
                            flet.Text(
                                value=descripcion,
                                size=9,
                                weight=flet.FontWeight.W_400,
                                color=flet.Colors.WHITE54,
                                opacity=1,
                                animate_opacity=200,
                            ),
                        ]
                    )
                ]
            )
        )

    def icono_sidebar(self, nombre_icono, texto):
        return flet.Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=self.resaltar,
            content=flet.Row(
                controls=[
                    flet.IconButton(
                        icon=nombre_icono,
                        icon_size=18,
                        icon_color=flet.Colors.WHITE54,
                        style=flet.ButtonStyle(
                            shape={
                                "": flet.RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={
                                "": flet.Colors.TRANSPARENT,
                            },
                        ),
                    ),
                    flet.Text(
                        value=texto,
                        color=flet.Colors.WHITE54,
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            )
        )

    def animar_sidebar(self, e):
        items_titulo = self.content.controls[0].content.controls[1].controls
        iconos_sidebar = self.content.controls[3:]
        if self.width != 62:
            for item in items_titulo:
                item.opacity = 0
            for item in iconos_sidebar:
                if isinstance(item, flet.Container):
                    item.content.controls[1].opacity = 0
            self.update()
            time.sleep(0.2)
            self.width = 62
            e.control.icon = flet.Icons.ARROW_FORWARD_IOS_ROUNDED
            self.update()
        else:
            self.width = 200
            self.update()
            time.sleep(0.1)
            for item in items_titulo:
                item.opacity = 1
            for item in iconos_sidebar:
                if isinstance(item, flet.Container):
                    item.content.controls[1].opacity = 1
            e.control.icon = flet.Icons.ARROW_BACK_IOS_ROUNDED
            self.update()


def main(page: flet.Page):
    page.window.width = 250
    page.add(Sidebar())


flet.app(main)
