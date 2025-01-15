import flet


class DropDownAutoComplete(flet.Container):
    def __init__(self, lista):
        self.lista = lista
        self.controles = {}
        super().__init__(
            content=self.dropdown()
        )

    def checkear_lista(self, e, height):
        dropdown = self.controles["dropdown"]
        if height == 0:
            self.salir(e)
        else:
            dropdown.height = 60 + height * 22 if 60 + height * 22 <= 300 else 300
            dropdown.update()

    def salir(self, e):
        dropdown = self.controles["dropdown"]
        dropdown.height = 50
        dropdown.update()

    def filtrar_lista(self, e):
        dropdown = self.controles["dropdown"]
        if e.data.lower() == "":
            dropdown.content.controls[1].controls.clear()
            dropdown.update()
            self.salir(e)
        else:
            dropdown.content.controls[1].controls.clear()

            contador = 0
            lista_filtrada = list(filter(lambda d: e.data.lower() in d["nombre"].lower(), self.lista))
            lista_ordenada = sorted(lista_filtrada, key=lambda persona: persona["nombre"])
            lista_ordenada = sorted(
                lista_ordenada,
                key=lambda persona: persona["nombre"].lower().find(e.data.lower())
            )
            # print(lista_ordenada)
            # print(lista_ordenada_filtrada)
            for elemento in lista_ordenada:
                # print(elemento["nombre"])
                if e.data.lower() in elemento["nombre"].lower():
                    dropdown.content.controls[1].controls.append(
                        flet.Row(
                            alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                flet.Text(
                                    value=elemento["nombre"],
                                    size=12
                                ),
                                flet.Text(
                                    value=elemento["key"],
                                    italic=True,
                                    size=10,
                                    color=flet.Colors.WHITE54,
                                )
                            ]
                        )
                    )
                    contador += 1
            self.checkear_lista(e, contador)

    def dropdown(self):
        dropdown = flet.Container(
            width=450,
            height=50,
            bgcolor=flet.Colors.WHITE10,
            border_radius=6,
            padding=flet.Padding(top=15, left=21, right=21, bottom=15),
            clip_behavior=flet.ClipBehavior.HARD_EDGE,
            animate=flet.animation.Animation(400, flet.AnimationCurve.DECELERATE),
            content=flet.Column(
                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                alignment=flet.MainAxisAlignment.START,
                controls=[
                    flet.TextField(
                        hint_text="Dropdown",
                        border_color=flet.Colors.TRANSPARENT,
                        height=20,
                        text_size=12,
                        content_padding=2,
                        cursor_color=flet.Colors.WHITE,
                        cursor_width=1,
                        on_change=self.filtrar_lista,
                    ),
                    flet.Column(
                        scroll=flet.ScrollMode.AUTO,
                        expand=True,
                        spacing=5,
                    )
                ]
            )
        )
        self.controles["dropdown"] = dropdown
        return dropdown


def main(page: flet.Page):
    lista = [
        {"nombre": "Camila", "key": 1},
        {"nombre": "Sofia", "key": 2},
        {"nombre": "Micaela", "key": 3},
        {"nombre": "Morena", "key": 4},
        {"nombre": "Mora", "key": 5},
        {"nombre": "Martin", "key": 6},
        {"nombre": "Matias", "key": 7},
        {"nombre": "Agustin", "key": 8},
        {"nombre": "Gonzalo", "key": 9},
        {"nombre": "Tortonese", "key": 10},
        {"nombre": "Lucas", "key": 11},
        {"nombre": "Debora", "key": 12},
        {"nombre": "Luisina", "key": 13},
        {"nombre": "Tito", "key": 14},
        {"nombre": "Ariana", "key": 15},
        {"nombre": "Patricia", "key": 16},
        {"nombre": "Nestor", "key": 17},
        {"nombre": "Cintia", "key": 18},
        {"nombre": "Ramiro", "key": 19},
        {"nombre": "Lily", "key": 20},
        {"nombre": "Maxi", "key": 21},
        {"nombre": "Axel", "key": 22},
        {"nombre": "Carina", "key": 23},
    ]

    app = DropDownAutoComplete(lista)
    page.add(app)


flet.app(main)
