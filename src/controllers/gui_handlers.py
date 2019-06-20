from src.controllers.views.painter import paint_button

active_buttons = []


def reset():
    active_buttons.clear()


def handle_all():
    for button in active_buttons:
        button.listen()
        paint_button(button)
