import flet


class CardAnimada(flet.Container):
    def __init__(self):
        self._container_icono = flet.Container(
            visible=False,
            width=128,
            height=55,
            bgcolor=flet.Colors.BLUE_800,
            border_radius=25,
            animate_opacity=200,
            offset=flet.transform.Offset(0, 0.25),
            animate_offset=flet.animation.Animation(duration=900, curve=flet.AnimationCurve.EASE),
            content=flet.Row(
                alignment=flet.MainAxisAlignment.CENTER,
                controls=[
                    flet.Text("Mas info", size=12, weight=flet.FontWeight.W_600)
                ]
            )
        )
        self._container_animado = flet.Container(
            width=280,
            height=380,
            bgcolor=flet.Colors.WHITE,
            border_radius=12,
            on_hover=self.animar_card,
            animate=flet.animation.Animation(duration=600, curve=flet.AnimationCurve.EASE),
            border=flet.border.all(2, flet.Colors.WHITE24),
            content=flet.Column(
                alignment=flet.MainAxisAlignment.CENTER,
                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    flet.Container(
                        padding=20,
                        alignment=flet.alignment.bottom_center,
                        content=flet.Text(
                            value="Título",
                            color=flet.Colors.BLACK,
                            size=28,
                            weight=flet.FontWeight.W_800,
                        )
                    ),
                    flet.Container(
                        padding=20,
                        alignment=flet.alignment.bottom_center,
                        content=flet.Text(
                            value="Agregar mas cosas acá...",
                            color=flet.Colors.BLACK,
                            size=14,
                            weight=flet.FontWeight.W_800,
                        )
                    )
                ]
            )
        )
        self._card = flet.Card(
            elevation=0,
            content=flet.Container(
                content=flet.Column(
                    spacing=0,
                    horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                    controls=[
                        self._container_animado,
                    ]
                )
            )
        )
        self._exterior_card = flet.Column(
            spacing=0,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
            controls=[
                self._card,
                self._container_icono,
            ]
        )
        super().__init__(
            content=self._exterior_card
        )

    def animar_card(self, e):
        self._container_icono.visible = True
        self._container_icono.update()

        if e.data == "true":
            # Animación de elevación de la card
            for _ in range(20):
                self._card.elevation += 1
                self._card.update()

            # Animación del borde de la card
            self._container_animado.border = flet.border.all(4, flet.Colors.BLUE_800)
            self._container_animado.update()

            # Animación de la posición del botón
            self._container_icono.offset = flet.transform.Offset(0, -0.75)
            self._container_icono.opacity = 1
            self._container_icono.update()

        else:
            # Animación de elevación de la card
            for _ in range(20):
                self._card.elevation -= 1
                self._card.update()

            # Animación del borde de la card
            self._container_animado.border = None
            self._container_animado.update()

            # Animación de la posición del botón
            self._container_icono.offset = flet.transform.Offset(0, 0.25)
            self._container_icono.opacity = 0
            self._container_icono.update()


def main(page: flet.Page):
    page.bgcolor = flet.Colors.WHITE
    page.window.width = 500
    page.window.height = 800
    app = CardAnimada()
    page.add(app)
    page.update()


flet.app(main)
