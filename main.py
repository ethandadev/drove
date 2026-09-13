import sys
import pygame as pg
import constants as c
from carController import Car
from mapManager import mapManager
from hud import Hud

pg.init()
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption(c.name)

car_img = pg.image.load(c.car1_path).convert_alpha()

player = Car(0, 0, car_img)
hud = Hud()
map_manager = mapManager()
map_manager.load_map()
clock = pg.time.Clock()

camera_follows_rotation = False

running = True
while running:
    clock.tick(c.FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_c:
            camera_follows_rotation = not camera_follows_rotation

    keys = pg.key.get_pressed()
    player.update(keys)
    hud.update(player.get_speed())

    margin = max(c.car1_width, c.car1_height) / 2
    player.x = max(margin, min(player.x, map_manager.map_width - margin))
    player.y = max(margin, min(player.y, map_manager.map_height - margin))

    #draw stuff
    screen.fill(c.GREEN)

    if camera_follows_rotation:
        map_manager.draw_rotated(screen, player.x, player.y, player.angle)

        actual_angle = player.angle
        player.angle = 0
        player.draw(screen, c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
        player.angle = actual_angle
        hud.draw(screen)
    else:
        camera_x = player.x - (c.SCREEN_WIDTH / 2)
        camera_y = player.y - (c.SCREEN_HEIGHT / 2)
        camera_x, camera_y = map_manager.clamp_camera(camera_x, camera_y)

        map_manager.draw(screen, camera_x, camera_y)
        player.draw(screen, player.x - camera_x, player.y - camera_y)
        hud.draw(screen)

    pg.display.flip()

pg.quit()
sys.exit()