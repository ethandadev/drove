import os
import sys

if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.argv[0]))
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame as pg
import pygame_essentials as pe
import constants as c
from carController import Car
from mapManager import mapManager
from hud import Hud
from startMenu import StartMenu

pg.init()
print("[Pygame] Initialized")
print("[drove] Starting Game...")
icon_image = pg.image.load('assets/icon.png')
pg.display.set_icon(icon_image)
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pg.SCALED, vsync=1)
pg.display.set_caption(c.name)


car_img = pg.image.load(c.car1_path).convert_alpha()

player = Car(0, 0, car_img)
map_manager = mapManager()
map_manager.load_map()
hud = Hud(*map_manager.get_minimap())
startMenu = StartMenu()

clock = pg.time.Clock()

state = "start"

camera_follows_rotation = False

debug = pe.DebugOverlay(visible=False, position=(10, 10), font_size=22)
debug.watch("car pos", lambda: f"{player.x:.0f}, {player.y:.0f}")
debug.watch("current tile on", lambda: map_manager.get_tile_at(player.x, player.y))
debug.watch("camera mode", lambda: "camera follows rotation" if camera_follows_rotation else "camera dont follow rotation")
debug.watch("current state", lambda: state)
debug.watch("current true speed", lambda: f"{player.speed:.0f}")
debug.watch("car angle", lambda: f"{player.angle:.0f}")


running = True
while running:
    dt = clock.tick(c.FPS) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_c and state == "game":
            camera_follows_rotation = not camera_follows_rotation
        debug.handle_event(event)
        if state == "start":
            startMenu.handle_event(event)

    debug.update(dt)
    if state == "start":
        startMenu.draw(screen)
        if startMenu.play_button.was_clicked():
            state = "game"
        elif startMenu.quit_button.was_clicked():
            running = False
    else:
        keys = pg.key.get_pressed()
        player.update(keys, map_manager.get_tile_at(player.x, player.y))
        hud.update(player.get_speed(), *player.get_pos())

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

    debug.draw(screen)
    pg.display.flip()

print("[drove] Exiting...")
pg.quit()
print("[Pygame] Exiting...")
sys.exit()