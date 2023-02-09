character = Actor("rainbow_ghost")
character.pos = 50, 50

WIDTH = 500
HEIGHT = character.height + 20


def draw():
    screen.clear()
    character.draw()


def update():
    character.left += 3
    if character.left > WIDTH:
        character.right = 6

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("40 papa it a mobster turn your brain to pasta!")
        character.image = 'dark_rainbow_ghost'


