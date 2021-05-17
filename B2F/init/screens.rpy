# -*- coding: utf-8 -*-
init:

    # screen b2f_main_menu_stable():
    #
    #     add b2f_old_preview
    #
    #     zorder 801
    #
    # # Для смены превью кнопок
    # screen b2f_main_menu_preview(what=Null()):
    #
    #     zorder 802
    #
    #     add b2f_old_preview:
    #         at transform:
    #             ypos 0.0
    #             xpos 0
    #             ease 1.0 ypos -1.0 xpos 289
    #
    #     add what:
    #         at transform:
    #             ypos 1.0
    #             xpos -289
    #             ease 1.0 ypos 0.0 xpos 0
    #
    #
    #     timer 1 action (Show("b2f_main_menu_stable"), SetVariable("b2f_old_preview", what), Hide("b2f_main_menu_preview", dissolve))
    #
    #
    # # Главное меню мода
    # screen b2f_main_menu():
    #
    #     modal True
    #     zorder 800
    #     tag menu
    #
    #     add "mods/B2F/gui/menu/menu_insensitive.webp":
    #         at transform:
    #             xoffset 4000
    #             ease .7 xoffset 0
    #
    #     imagemap:
    #         at transform:
    #             alpha 0.0
    #             pause .7
    #             ease .7 alpha 1.0
    #         ground "mods/B2F/gui/main_menu_ground.webp"
    #         auto "mods/B2F/gui/menu/menu_%s.webp"
    #
    #         # hotspot (1327, 45, 600, 254) hovered Show("b2f_main_menu_preview", dissolve, "mods/B2F/gui/menu_previews/start_hover.webp") unhovered Hide("b2f_main_menu_preview", dissolve) action NullAction()
    #         # hotspot (1082, 324, 588, 232) hovered Show("b2f_main_menu_preview", dissolve, "mods/B2F/gui/menu_previews/load_hover.webp") unhovered Hide("b2f_main_menu_preview", dissolve) action NullAction()
    #         # hotspot (1170, 583, 592, 223) hovered Show("b2f_main_menu_preview", dissolve, "mods/B2F/gui/menu_previews/settings_hover.webp") unhovered Hide("b2f_main_menu_preview", dissolve) action NullAction()
    #         # hotspot (924, 852, 582, 223) hovered Show("b2f_main_menu_preview", dissolve, "mods/B2F/gui/menu_previews/exit_hover.webp") unhovered Hide("b2f_main_menu_preview", dissolve) action Jump("b2f_true_exit")
    #
    #         hotspot (1327, 45, 600, 254) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/start_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp") action Jump("b2f_start")#(MainMenu(), Start("b2f_start"))
    #         hotspot (1082, 324, 588, 232) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/load_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp")# action NullAction()
    #         hotspot (1170, 583, 592, 223) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/settings_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp")# action NullAction()
    #         hotspot (924, 852, 582, 223) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/exit_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp") action Jump("b2f_true_exit")



    ##################################################################################################################

    # screen b2f_main_menu():
    #
    #
    #     tag menu
    #
    #     add "mods/B2F/gui/main_menu_ground.webp"
    #
    #     add b2f_old_preview
    #
    #     use b2f_navigation
    #
    # screen b2f_navigation():
    #
    #     modal True
    #     zorder 900
    #
    #     add "mods/B2F/gui/menu/menu_insensitive.webp":
    #         at transform:
    #             xoffset 4000
    #             ease .7 xoffset 0
    #
    #     imagemap:
    #         at transform:
    #             alpha 0.0
    #             pause .7
    #             ease .7 alpha 1.0
    #         auto "mods/B2F/gui/menu/menu_%s.webp"
    #
    #         hotspot (1327, 45, 600, 254) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/start_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp") action Jump("b2f_start")#(MainMenu(), Start("b2f_start"))
    #         hotspot (1082, 324, 588, 232) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/load_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp")# action NullAction()
    #         hotspot (1170, 583, 592, 223) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/settings_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp")# action NullAction()
    #         hotspot (924, 852, 582, 223) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/exit_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp") action Jump("b2f_true_exit")
    #
    # screen b2f_main_menu_preview(what=Null()):
    #
    #     zorder 850
    #
    #     add b2f_old_preview:
    #         at transform:
    #             ypos 0.0
    #             xpos 0
    #             ease 1.0 ypos -1.0 xpos 289
    #
    #     add what:
    #         at transform:
    #             ypos 1.0
    #             xpos -289
    #             ease 1.0 ypos 0.0 xpos 0
    #
    #
    #     timer 1 action (SetVariable("b2f_old_preview", what), Hide("b2f_main_menu_preview", dissolve))

    screen b2f_main_menu():

        modal True
        zorder 900

        add "mods/B2F/gui/menu/menu_insensitive.webp":
            at transform:
                xoffset 4000
                ease .7 xoffset 0

        imagemap:
            at transform:
                alpha 0.0
                pause .7
                ease .7 alpha 1.0
            auto "mods/B2F/gui/menu/menu_%s.webp"



            hotspot (1327, 45, 600, 254) hovered b2f.show_preview("start_hover") unhovered b2f.show_preview("default_idle") action Jump("b2f_start")#(MainMenu(), Start("b2f_start"))
            hotspot (1082, 324, 588, 232) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/load_hover.webp")  unhovered  b2f.show_preview("default_idle")# action NullAction()
            hotspot (1170, 583, 592, 223) hovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/settings_hover.webp") unhovered Show("b2f_main_menu_preview", what="mods/B2F/gui/menu_previews/default_idle.webp")# action NullAction()
            hotspot (924, 852, 582, 223) hovered  b2f.show_preview("exit_hover") unhovered  b2f.show_preview("default_idle") action Jump("b2f_true_exit")

    # python: # Я уй его знает, хотел в другом файле инициализовать, оффсеты не помогают - не может найти b2f_menu_preview
    #
    #     def b2f.show_preview(name):
    #
    #         def show():
    #             renpy.show(name="preview", at_list=[b2f_menu_preview], what=Image("mods/B2F/gui/menu_previews/"+name+".webp"))
    #             renpy.restart_interaction()
    #
    #
    #         return show



label b2f_main_menu:
    window hide
    scene image "mods/B2F/gui/main_menu_ground.webp"
    call screen b2f_main_menu()
    pause
    #$ b2f.screen_act()
    return

label b2f_true_exit:

    window hide dissolve
    # hide screen b2f_main_menu
    # hide screen b2f_main_menu_stable
    # hide screen b2f_main_menu_preview
    scene black
    with fade
    pause 1
    # $ b2f.screen_deact()
    $ MainMenu(confirm=False)()
