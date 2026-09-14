import pygame as pg
import constants as c


class Hud:
    def __init__(self):
        self.speed = 0
        self.font = pg.font.SysFont('arial', 40)
        self.font2 = pg.font.SysFont('arial', 20)
        self.hud_width = 300
        self.hud_height = 150
        self.rect_x = c.SCREEN_WIDTH - self.hud_width - 50
        self.rect_y = c.SCREEN_HEIGHT - self.hud_height - 50
        self.bg_rect = pg.Rect(self.rect_x, self.rect_y, self.hud_width, self.hud_height)
        self.fps_hud_width = 100
        self.fps_hud_height = 50
        self.rect_x2 = 30
        self.rect_y2 = 30
        self.bg_rect2 = pg.Rect(self.rect_x2, self.rect_y2, self.fps_hud_width, self.fps_hud_height)
        self.fps = 0
        print("[Hud] Initialized")

    def update(self, speed, fps):
        self.speed = speed
        self.fps = fps

    def draw(self, screen):
        pg.draw.rect(screen, c.GRAY, self.bg_rect)
        speed_text = f"{round(self.speed)} KPH"
        text_surface = self.font.render(speed_text, True, c.BLACK)

        text_rect = text_surface.get_rect(center=self.bg_rect.center)

        screen.blit(text_surface, text_rect)

        if c.show_fps:
            pg.draw.rect(screen, c.WHITE, self.bg_rect2)
            fps_text = self.font2.render(f"FPS: {round(self.fps)}", True, c.BLACK)
            fps_text_rect = fps_text.get_rect(center=self.bg_rect2.center)

            screen.blit(fps_text, fps_text_rect)