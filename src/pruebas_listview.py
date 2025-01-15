import flet


class DropDownListView(flet.Container):
    def __init__(self):
        self.selected_index = -1
        super().__init__(
            bgcolor=flet.Colors.WHITE10,
            border_radius=8,
            height=50,
            width=400,
            animate=flet.animation.Animation(600, flet.AnimationCurve.DECELERATE),
            content=flet.Column(
                controls=[
                    flet.Row(
                        controls=[
                            flet.TextField(
                                border_color=flet.Colors.TRANSPARENT,
                                hint_text="DropDown",
                                text_size=12,
                                on_change=self.agregar_elementos,
                                width=400,
                                on_blur=self.desactivar_textfield,
                                on_focus=self.actiar_textfield,
                            ),
                            flet.TextField(
                                border_color=flet.Colors.TRANSPARENT,
                                color=flet.Colors.TRANSPARENT,
                                cursor_color=flet.Colors.TRANSPARENT,
                            )
                        ]
                    ),
                    flet.ListView()
                ]
            )
        )

    def actiar_textfield(self, e):
        self.content.controls[0].controls[1].visible = True

    def desactivar_textfield(self, e):
        self.content.controls[0].controls[1].visible = False

    def agregar_elementos(self, e):
        if e.data == "":
            self.salir()
        else:
            for i in range(5, 52, 2):
                self.content.controls[1].controls.append(
                    flet.ListTile(
                        title=flet.Text(f"Hola{i}", size=12),
                        bgcolor=flet.Colors.WHITE10,
                        selected_color=flet.Colors.WHITE,
                        selected_tile_color=flet.Colors.WHITE24,
                    )
                )

            new_height = 60 + 25 * 22
            self.height = new_height if new_height < 300 else 300
            self.content.controls[1].height = self.height - 60
        self.update()

    def salir(self):
        self.selected_index = -1
        self.content.controls[1].controls.clear()
        self.height = 50

    def moverse_en_listview(self, e: flet.KeyboardEvent):
        if len(self.content.controls[1].controls) > 0:
            if e.key == "Arrow Down":
                self.content.controls[0].controls[1].focus()
                self.content.controls[1].controls[self.selected_index].selected = False
                self.selected_index += 1 if self.selected_index + 1 < len(self.content.controls[1].controls) else 0
                self.content.controls[1].controls[self.selected_index].selected = True
            elif e.key == "Arrow Up":
                self.content.controls[0].controls[1].focus()
                self.content.controls[1].controls[self.selected_index].selected = False
                self.selected_index -= 1 if self.selected_index - 1 >= 0 else 0
                self.content.controls[1].controls[self.selected_index].selected = True
            elif e.key == "Enter":
                self.content.controls[0].controls[0].value = self.content.controls[1].controls[self.selected_index].title.value
                self.content.controls[0].controls[0].focus()
                self.salir()
        self.update()

    def build(self):
        self.page.on_keyboard_event = self.moverse_en_listview


def main(page: flet.Page):
    app = DropDownListView()
    page.add(
        app
    )


flet.app(main)
