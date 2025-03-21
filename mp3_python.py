import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
back = pg.image.load(r'background.jpg')

pg.font.init()
font = pg.font.Font(None, 36)

music_files = [("songs\\Ark Patrol - let Go (slowed)", "covers/money.jpg", "Ark Patrol - let Go (slowed)"), 
               ("songs\\the-verkkars_-_ez4ence", "covers/Ez4ence.jpg", "the-verkkars_-_ez4ence"), 
               ("songs\\Dean Martin - Let It Snow, Let It Snow, Let It Snow (Remastered)", "covers/simple.png", "Dean Martin - Let It Snow, Let It Snow, Let It Snow (Remastered)")]
current_track = 0
pg.mixer.music.load(music_files[current_track][0])

playing = False  

def load_cover():
    try:
        return pg.image.load(music_files[current_track][1])
    except pg.error:
        return None

cover_img = load_cover()

def play_music():
    global playing
    pg.mixer.music.play(-1)
    playing = True  

def pause_music():
    global playing
    if playing:
        pg.mixer.music.pause()
        playing = False
    else:
        pg.mixer.music.unpause()
        playing = True

def next_track():
    global current_track, cover_img
    current_track = (current_track + 1) % len(music_files)  
    pg.mixer.music.load(music_files[current_track][0])
    play_music()
    cover_img = load_cover()

done = False

while not done:
    screen.blit(back, (0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                play_music()
            elif event.key == pg.K_RIGHT:
                next_track()
            elif event.key == pg.K_p:
                pause_music()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 350 <= x <= 450 and 450 <= y <= 650:
                play_music()
            elif 590 <= x <= 700 and 500 <= y <= 600:
                next_track()
            elif 100 <= x <= 180 and 500 <= y <= 590:
                pause_music()

    play_triangle = [(350, 450), (350, 650), (450, 550)]
    pg.draw.polygon(screen, black, play_triangle)

    pg.draw.rect(screen, black, (150, 500, 30, 90))
    pg.draw.rect(screen, black, (100, 500, 30, 90))

    pg.draw.polygon(screen, black, [(650, 500), (650, 600), (700, 550)], 15)
    pg.draw.polygon(screen, black, [(590, 500), (590, 600), (640, 550)], 15)

    text_surface = font.render(music_files[current_track][2], True, black)
    screen.blit(text_surface, (400 - text_surface.get_width() // 2, 50))

    if cover_img:
        cover_resized = pg.transform.scale(cover_img, (300, 300))
        screen.blit(cover_resized, (250, 100))

    pg.display.flip()
    clock.tick(60)

pg.quit()