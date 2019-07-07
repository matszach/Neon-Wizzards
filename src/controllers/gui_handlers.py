

active_buttons = []
active_decorators = []


def reset():
    active_buttons.clear()
    active_decorators.clear()


def handle_all(surface):

    for button in active_buttons:
        button.listen()
        button.draw_self(surface)

    for decor in active_decorators:
        decor.draw_self(surface)
        decor.animate()
