import pygame as game
from pygame.locals import *
import Brain
from cgf_parser import parse
from Interface_Objects import *
from debugger import *

log('Started', 'Interface.py')


def render():
    log('Rendering', 'Interface.py')

    for sprite in sprites:
        log(f'Rendering sprite', 'Interface.py')
        screen.blit(sprite.image, sprite.rect)

    for button in buttons:
        button.render(screen)

    for textbar in textbars:
        textbar.render(screen)

    for infobar in infobars:
        pass


log('Initialising display', 'Interface.py')

config = parse('config.cfg')

screen = game.display.set_mode((config['resolution']['width'], config['resolution']['height']))
game.display.set_caption('Наблюдатель')
game.display.set_icon(game.image.load('icon.ico'))

log('Display initialised', 'Interface.py')

while True:
    log('Main cycle iteration', 'Interface.py')

    game.time.Clock().tick(60)
    screen.fill(BLACK)
    events = game.event.get()

    for event in events:
        for button in buttons:
            button.is_intersect(event)
            button.is_pressed(event)

    render()
    game.display.update()
