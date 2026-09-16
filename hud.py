import pygame as pg
import pygame_essentials as pe
import constants as c


class Hud:
    def __init__(self, minimap, minimap_scale_x, minimap_scale_y):
        self.speed = 0
        self.hud_width = 300
        self.hud_height = 150
        self.rect_x = c.SCREEN_WIDTH - self.hud_width - 50
        self.rect_y = c.SCREEN_HEIGHT - self.hud_height - 50
        self.bg_rect = pg.Rect(self.rect_x, self.rect_y, self.hud_width, self.hud_height)
        self.speed_text = pe.Label((400, 360), "- KPH", color=(40, 40, 40), anchor="center", font=c.font_regular_path, font_size=40)
        self.speed_text.rect.center = self.bg_rect.center
        self.minimap = minimap
        self.minimap_scale_x = minimap_scale_x
        self.minimap_scale_y = minimap_scale_y
        print("[Hud] Initialized")

    def update(self, speed):
        self.speed = speed

    def draw(self, screen):
        pg.draw.rect(screen, c.GRAY, self.bg_rect)
        speed_text = f"{round(self.speed)} KPH"
        self.speed_text.text = speed_text

        self.speed_text.draw(screen)
