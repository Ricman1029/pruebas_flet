import flet
import time
from math import pi


class SidebarDestination(flet.Container):
    def __init__(self, icono: flet.Icons, texto: str):
        super().__init__(
            key="",
            width=180,
            height=45,
            border_radius=10,
            on_hover=self.hover,
            content=flet.Row(
                controls=[
                    flet.IconButton(
                        icon=icono,
                        icon_size=18,
                        style=flet.ButtonStyle(
                            shape=flet.RoundedRectangleBorder(radius=7),
                            overlay_color=flet.Colors.TRANSPARENT,
                        ),
                    ),
                    flet.Text(
                        value=texto,
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            )
        )

    def hover(self, e):
        if e.control.key != "seleccionado":
            if e.data == "true":
                e.control.bgcolor = flet.colors.SURFACE_VARIANT
                e.control.content.controls[0].icon_color = flet.Colors.ON_SURFACE_VARIANT
                e.control.content.controls[1].color = flet.Colors.ON_SURFACE_VARIANT
            else:
                e.control.bgcolor = None
                e.control.content.controls[0].icon_color = flet.Colors.PRIMARY
                e.control.content.controls[1].color = flet.Colors.ON_SURFACE
            e.control.update()


class Sidebar(flet.Column):
    def __init__(
            self,
            iniciales,
            nombre,
            descripcion,
            destinations: [SidebarDestination],
            on_click=None,
            log_out: SidebarDestination | None = None
    ):
        self.destinations = [destination for destination in destinations]
        for destination in self.destinations:
            destination.on_tap_down = self.seleccionar
            destination.on_click = on_click
        super().__init__(
            expand=True,
            width=200,
            controls=[
                flet.Container(
                    expand=True,
                    bgcolor=flet.Colors.SURFACE,
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
                                iniciales=iniciales,
                                nombre=nombre,
                                descripcion=descripcion
                            ),
                            flet.IconButton(
                                icon=flet.Icons.ARROW_BACK_IOS_ROUNDED,
                                on_click=self.animar_sidebar,
                                rotate=flet.transform.Rotate(0, alignment=flet.alignment.center),
                                animate_rotation=flet.animation.Animation(300, flet.AnimationCurve.DECELERATE),
                            ),
                            flet.Divider(
                                height=5,
                                color=flet.Colors.TRANSPARENT,
                            ),
                            *self.destinations,
                            (flet.Divider(height=5), log_out) if log_out else flet.Container()
                        ]
                    )
                )
            ]
        )

    def seleccionar(self, e):
        # Le quitamos el color a todos
        for destination in self.destinations:
            if isinstance(destination, flet.Container):
                destination.key = ""
                destination.bgcolor = None
                destination.content.controls[0].icon_color = flet.Colors.PRIMARY
                destination.content.controls[1].color = flet.Colors.ON_SURFACE_VARIANT

        # Le damos el color al elemento seleccionado
        e.control.key = "seleccionado"
        e.control.bgcolor = flet.Colors.SECONDARY_CONTAINER
        e.control.content.controls[0].icon_color = flet.Colors.ON_SECONDARY_CONTAINER
        e.control.content.controls[1].color = flet.Colors.ON_SECONDARY_CONTAINER
        self.update()

    def datos_usuarios(self, iniciales, nombre, descripcion):
        return flet.Container(
            content=flet.Row(
                controls=[
                    flet.Container(
                        width=42,
                        height=42,
                        bgcolor=flet.Colors.TERTIARY,
                        alignment=flet.alignment.center,
                        border_radius=8,
                        content=flet.Text(
                            value=iniciales,
                            size=20,
                            weight=flet.FontWeight.BOLD,
                            color=flet.Colors.ON_TERTIARY,
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
                                width=130,
                                max_lines=2,
                                overflow=flet.TextOverflow.ELLIPSIS
                            ),
                            flet.Text(
                                value=descripcion,
                                size=9,
                                weight=flet.FontWeight.W_400,
                                opacity=1,
                                animate_opacity=200,
                                width=130,
                                max_lines=2,
                                overflow=flet.TextOverflow.ELLIPSIS
                            ),
                        ]
                    )
                ]
            )
        )

    def animar_sidebar(self, e):
        items_titulo = self.content.controls[0].content.controls[1].controls
        if self.width != 62:
            for item in items_titulo:
                item.opacity = 0
            for item in self.destinations:
                if isinstance(item, flet.Container):
                    item.content.controls[1].opacity = 0
            e.control.rotate.angle += pi
            self.update()
            time.sleep(0.2)
            self.width = 62
        else:
            self.width = 200
            e.control.rotate.angle -= pi
            self.update()
            time.sleep(0.1)
            for item in items_titulo:
                item.opacity = 1
            for item in self.destinations:
                if isinstance(item, flet.Container):
                    item.content.controls[1].opacity = 1
        self.update()


def main(page: flet.Page):
    page.theme = flet.Theme(
        color_scheme=flet.ColorScheme(
            primary="#6750A4",
            on_primary="#FFFFFF",
            primary_container="#EADDFF",
            on_primary_container="#4F378B",
            secondary="#625B71",
            on_secondary="#FFFFFF",
            secondary_container="#E8DEF8",
            on_secondary_container="#4A4458",
            tertiary="#7D5260",
            on_tertiary="#FFFFFF",
            tertiary_container="#FFD8E4",
            on_tertiary_container="#633B48",
            error="#B3261E",
            on_error="#FFFFFF",
            error_container="#F9DEDC",
            on_error_container="#8C1D18",
            surface="#FEF7FF",
            on_surface="#1D1B20",
            surface_variant="#E7E0EC",
            on_surface_variant="#49454F",
            surface_container_high="#ECE6F0",
            surface_container="#F3EDF7",
            surface_container_low="#F7F2FA",
            surface_container_lowest="#FFFFFF",
            inverse_surface="#322F35",
            on_inverse_surface="#F5EFF7",
            surface_tint="#6750A4",
            outline="#79747E",
            outline_variant="#CAC4D0",
        )
    )
    page.dark_theme = flet.Theme(
        color_scheme=flet.ColorScheme(
            primary="#D0BCFF",
            on_primary="#381E72",
            primary_container="#4F378B",
            on_primary_container="#EADDFF",
            secondary="#CCC2DC",
            on_secondary="#332D41",
            secondary_container="#4A4458",
            on_secondary_container="#E8DEF8",
            tertiary="#EFB8C8",
            on_tertiary="#492532",
            tertiary_container="#633B48",
            on_tertiary_container="#FFD8E4",
            error="#F2B8B5",
            on_error="#601410",
            error_container="#8C1D18",
            on_error_container="#F9DEDC",
            surface="#141218",
            on_surface="#E6E0E9",
            surface_variant="#49454F",
            on_surface_variant="#CAC4D0",
            surface_container_high="#2B2930",
            surface_container="#211F26",
            surface_container_low="#1D1B20",
            surface_container_lowest="#0F0D13",
            inverse_surface="#E6E0E9",
            on_inverse_surface="#322F35",
            surface_tint="#D0BCFF",
            outline="#938F99",
            outline_variant="#49454F",
        )
    )
    page.window.width = 250

    def change(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.controls[1].icon = flet.Icons.LIGHT_MODE
        else:
            page.theme_mode = "dark"
            page.controls[1].icon = flet.Icons.DARK_MODE
        page.update()

    page.theme_mode = "dark"
    page.add(
        Sidebar(
            iniciales="ALB",
            nombre="Albano Construcciones S.R.L. y mas texto para ver la ellipsis",
            descripcion="Construcción",
            destinations=[
                SidebarDestination(
                    icono=flet.Icons.SEARCH,
                    texto="Search",
                ),
                SidebarDestination(
                    icono=flet.Icons.SEARCH,
                    texto="Search",
                ),
                SidebarDestination(
                    icono=flet.Icons.SEARCH,
                    texto="Search",
                ),
                SidebarDestination(
                    icono=flet.Icons.SEARCH,
                    texto="Search",
                ),
            ]
        ),
        flet.IconButton(icon=flet.Icons.MODE_NIGHT, on_click=change)
    )


flet.app(main)
