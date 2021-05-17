# -*- coding: utf-8 -*-
init python:

    mods["b2f_main_menu"] =  u"{font=fonts/PressStart2P.ttf}МЕЖ ДВУХ ОГНЕЙ{/font}"

    b2f_old_preview = "mods/B2F/gui/menu_previews/default_idle.webp"#Null(height=1080)

    le = Character("Лёва")

    sa = Character("Саша")
    vi = Character("Витя")
    an = Character("Андрей")

    ku = Character("Кузнец")
    ti = Character("Тихонов")

    di = Character("Диктор")
    su = Character("Судья")
    tr = Character("Тренер")

    fa = Character("Отец")


init python in b2f:

    import store

    # def screen_act():
    #     renpy.display.screen.screens[("original_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]
    #     renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("b2f_main_menu", None)]
    #
    # def screen_deact():
    #     renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("original_main_menu", None)]
    #
    def show_preview(name):

        def show():
            renpy.show(name="preview", at_list=[store.b2f_menu_preview], what=store.Image("mods/B2F/gui/menu_previews/"+name+".webp"))
            renpy.restart_interaction()


        return show

    def init_names():



        globals().update(
            {
                "le": store.Character("Лёва"),

                "sa": store.Character("Саша"),
                "vi": store.Character("Витя"),
                "an": store.Character("Андрей"),

                "ku": store.Character("Кузнец"),
                "ti": store.Character("Тихонов"),

                "di": store.Character("Диктор"),
                "su": store.Character("Судья"),
                "tr": store.Character("Тренер"),

                "fa": store.Character("Отец"),

            }

        )

init:

    transform dev_center():
        xalign 0.5
        yalign 0.0

    transform b2f_menu_preview():
        on replaced:
            ease .2 ypos 0.0 xpos 0

            # pause .1
            ease 1.0 ypos -1.0 xpos 289
        on replace:
            ypos 1.0
            xpos -289
            ease 1.0 ypos 0.0 xpos 0

        on show:
            ypos 1.0
            xpos -289
            ease 1.0 ypos 0.0 xpos 0

    transform b2f_counting():
        align (.5, .5)
        on show:
            alpha 0.0
            zoom .001
            ease 1.0 zoom 1.0 alpha 1.0

        on replace:
            alpha 0.0
            zoom .6
            ease 1.0 zoom 1.0 alpha 1.0

        on replaced:

            ease 1.0 zoom 1.5 alpha 0.0

        on hide:

            ease 1.0 zoom 1.5 alpha 0.0


    transform running():
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.1 pos (-6, -5)
        linear 0.1 pos (0, 0)
        linear 0.1 pos (6, -5)
        linear 0.1 pos (0, 0)
        repeat


    image cg prologue b2f 0 = "mods/B2F/images/cg/prologue_b2f_0.png"
