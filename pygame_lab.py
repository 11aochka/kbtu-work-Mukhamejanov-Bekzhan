import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()

done = False
micky_path = r'images\back.jpg'
second_hand_path = r'images\minutes.png'
minute_hand_path = r'images\hours.png'

micky = pg.image.load(micky_path)
second_hand = pg.image.load(second_hand_path)
minute_hand = pg.image.load(minute_hand_path)

img_width, img_height = micky.get_width(), micky.get_height()
x = (800 - img_width) // 2
y = (800 - img_height) // 2

s_angle, m_angle = 0, 0

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill((255, 100, 20))
    screen.blit(micky, (x, y))

    s_angle -= 6 / 60
    m_angle -= (6 / 3600)

    rotate_second = pg.transform.rotate(second_hand, s_angle)
    rotate_minute = pg.transform.rotate(minute_hand, m_angle)
    s_rect = rotate_second.get_rect(center=(400, 400))
    m_rect = rotate_minute.get_rect(center=(400, 440))

    screen.blit(rotate_second, s_rect.topleft)
    screen.blit(rotate_minute, m_rect.topleft)

    pg.display.flip()
    clock.tick(60)

pg.quit()