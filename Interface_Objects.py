import pygame as game
from pygame.locals import *
from debugger import *

log('Started', 'Interface_Object.py')

log('Initialising constants', 'Interface_Object.py')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (60, 100, 50)
BLUE = (0, 0, 255)
BROWN = (70, 50, 30)
YELLOW = (255, 243, 67)

game.font.init()

gost_font_48 = game.font.Font('Fonts/GOST_BU.TTF', 48)
gost_font_36 = game.font.Font('Fonts/GOST_BU.TTF', 36)
gost_font_18 = game.font.Font('Fonts/GOST_BU.TTF', 18)

alphabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_eng = 'ADCDEFGHIYKLMNOPQRSTUVWXYZ'
alphabet_dig = '1234567890'
alphabet_sym = '@#_- '

alphabet = alphabet_rus + alphabet_eng + alphabet_dig + alphabet_sym

log('Constants initialised', 'Interface_Object.py')


class Button:
    def __init__(self, name, sprite, function=None, font=gost_font_48, colour=BLACK, text='Кнопка', desc=None):
        log(f'Button {name} initialising', 'Interface_Object.py')
        self.name = name

        if type(sprite) == game.sprite.Sprite:
            self.idle = sprite
            self.pressed = None
            self.aimed = None
            self.button_type = 'static'
        elif type(sprite) == list:
            self.idle = sprite[0]
            self.aimed = sprite[1]
            self.pressed = sprite[2]
            self.button_type = 'dynamic'
        log(f'Button {name} initialised as {self.button_type}', 'Interface_Object.py')

        self.rect = self.idle.rect
        self.image = self.idle.image

        if function:
            self.function = function

        self.font = font
        self.text = text
        self.desc = desc

        self.colour = colour
        log(f'Button {name} initialised', 'Interface_Object.py')

    def render(self, display):
        log(f'Button {self.name} rendering', 'Interface_Object.py')
        display.blit(self.image, self.rect)
        text = self.font.render(self.text, True, self.colour)
        display.blit(text, text.get_rect(center=(self.rect.x + self.rect.width / 2,
                                                 self.rect.y + self.rect.height / 2)))

    def connect(self, function):
        log(f'Button {self.name} connecting to function', 'Interface_Object.py')
        self.function = function

    def is_intersect(self, event):
        log(f'Button {self.name} intersection check', 'Interface_Object.py')
        if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.button_type == 'dynamic':
                    self.image = self.aimed.image
                log(f'Button {self.name} intersection check passed', 'Interface_Object.py')
                return True
            else:
                if self.button_type == 'dynamic':
                    self.image = self.idle.image
                log(f'Button {self.name} intersection check failed', 'Interface_Object.py')
                return False

    def is_pressed(self, event):
        log(f'Button {self.name} press check', 'Interface_Object.py')
        if event.type == MOUSEBUTTONDOWN:
            if self.button_type == 'dynamic':
                self.image = self.pressed.image

            if self.is_intersect(event):
                self.function()
                log(f'Button {self.name} press check passed', 'Interface_Object.py')
                return True
        elif event.type == MOUSEBUTTONUP:
            if self.button_type == 'dynamic':
                self.image = self.idle.image
        log(f'Button {self.name} intersection check failed', 'Interface_Object.py')
        return False


class TextBar:
    def __init__(self, name, sprite, text='', symbols=alphabet, font=gost_font_18, sym_cap=16, colour=GREEN):
        log(f'Textbar {name} initialising', 'Interface_Object.py')
        self.name = name
        self.image = sprite.image
        self.rect = sprite.rect
        self.symbols = symbols
        self.font = font
        self.cap = sym_cap
        self.text = text
        self.blocked = True
        self.colour = colour

    def type_text(self, event):
        log(f'Typing in textbar {self.name}', 'Interface_Object.py')
        if not self.blocked:
            if event.type == KEYDOWN:
                if event.key == K_a:
                    self.text += 'a'

    def render(self, display):
        log(f'Textbar {self.name} rendering', 'Interface_Object.py')
        display.blit(self.image, self.rect)
        text = self.font.render(self.text, True, self.colour)
        display.blit(text, text.get_rect(topleft=(self.rect.x, self.rect.y - self.rect.height / 2)))


class InfoBar:
    def __init__(self, name):
        log(f'Infobar {name} initialising', 'Interface_Object.py')
        self.name = name


class Screen:
    pass


def exit_app():
    log(f'Exit function activated', 'Interface_Object.py')
    exit()


log('Interface objects initialising', 'Interface_Object.py')
sprites = []
buttons = []
textbars = []
infobars = []

screen_dummy = game.sprite.Sprite()
screen_dummy.image = game.image.load('Dummies/screen_dummy.png')
screen_dummy.rect = Rect(640, 0, 640, 480)
sprites.append(screen_dummy)

info_dummy = game.sprite.Sprite()
info_dummy.image = game.image.load('Dummies/info_dummy.png')
info_dummy.rect = Rect(0, 0, 640, 480)
sprites.append(info_dummy)

settings_dummy = game.sprite.Sprite()
settings_dummy.image = game.image.load('Dummies/settings_dummy.png')
settings_dummy.rect = Rect(0, 480, 1280, 240)
sprites.append(settings_dummy)

exit_button_sprite_idle = game.sprite.Sprite()
exit_button_sprite_idle.image = game.image.load('Img/button_template.png')

exit_button_sprite_aimed = game.sprite.Sprite()
exit_button_sprite_aimed.image = game.image.load('Img/aimed_button.png')

exit_button_sprite_pressed = game.sprite.Sprite()
exit_button_sprite_pressed.image = game.image.load('Img/pressed_button.png')

exit_button_sprite_idle.rect = Rect(1024, 640, 256, 80)
exit_button_sprite_aimed.rect = exit_button_sprite_idle.rect
exit_button_sprite_pressed.rect = exit_button_sprite_idle.rect

temp = [exit_button_sprite_idle, exit_button_sprite_aimed, exit_button_sprite_pressed]

exit_button = Button('exit', temp, exit_app, colour=BLUE, text='Выход')
buttons.append(exit_button)

start_typing_button_sprite_idle = game.sprite.Sprite()
start_typing_button_sprite_idle.image = game.image.load('Img/button_template.png')

start_typing_button_sprite_aimed = game.sprite.Sprite()
start_typing_button_sprite_aimed.image = game.image.load('Img/aimed_button.png')

start_typing_button_sprite_pressed = game.sprite.Sprite()
start_typing_button_sprite_pressed.image = game.image.load('Img/pressed_button.png')

start_typing_button_sprite_idle.rect = Rect(0, 560, 256, 80)
start_typing_button_sprite_aimed.rect = exit_button_sprite_idle.rect
start_typing_button_sprite_pressed.rect = exit_button_sprite_idle.rect

temp = [start_typing_button_sprite_idle, start_typing_button_sprite_aimed, start_typing_button_sprite_pressed]

start_typing_button = Button('start_typing', temp, exit_app, colour=BLUE, text='Вписать адрес камеры',
                             font=gost_font_18)
buttons.append(start_typing_button)

stop_typing_button_sprite_idle = game.sprite.Sprite()
stop_typing_button_sprite_idle.image = game.image.load('Img/button_template.png')

stop_typing_button_sprite_aimed = game.sprite.Sprite()
stop_typing_button_sprite_aimed.image = game.image.load('Img/aimed_button.png')

stop_typing_button_sprite_pressed = game.sprite.Sprite()
stop_typing_button_sprite_pressed.image = game.image.load('Img/pressed_button.png')

stop_typing_button_sprite_idle.rect = Rect(256, 560, 256, 80)
stop_typing_button_sprite_aimed.rect = exit_button_sprite_idle.rect
stop_typing_button_sprite_pressed.rect = exit_button_sprite_idle.rect

temp = [stop_typing_button_sprite_idle, stop_typing_button_sprite_aimed, stop_typing_button_sprite_pressed]

stop_typing_button = Button('stop_typing', temp, exit_app, colour=BLUE, text='Прекратить ввод',
                            font=gost_font_18)
buttons.append(stop_typing_button)


cam_id_textbar_sprite = game.sprite.Sprite()
cam_id_textbar_sprite.image = game.image.load('Img/textbar_template.png')
cam_id_textbar_sprite.rect = Rect(0, 480, 512, 80)

temp = [stop_typing_button_sprite_idle, stop_typing_button_sprite_aimed, stop_typing_button_sprite_pressed]

cam_id_textbar = TextBar('cam_id_textbar', cam_id_textbar_sprite)
textbars.append(cam_id_textbar)

log(f'Interface objects initialised', 'Interface_Object.py')
