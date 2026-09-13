import pygame as pg
import constants as c


class Hud:
    def __init__(self):
        self.speed = 0
        self.font = pg.font.SysFont('arial', 40)
        self.hud_width = 300
        self.hud_height = 150
        self.rect_x = c.SCREEN_WIDTH - self.hud_width - 50
        self.rect_y = c.SCREEN_HEIGHT - self.hud_height - 50
        self.bg_rect = pg.Rect(self.rect_x, self.rect_y, self.hud_width, self.hud_height)

    def update(self, speed):
        self.speed = speed

    def draw(self, screen):
        pg.draw.rect(screen, c.GRAY, self.bg_rect)
        speed_text = f"{round(self.speed)} KPH"
        text_surface = self.font.render(speed_text, True, c.BLACK)

        text_rect = text_surface.get_rect(center=self.bg_rect.center)

        screen.blit(text_surface, text_rect)