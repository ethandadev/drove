import pygame as pg
import pygame_essentials as pe
import constants as c


class StartMenu:
    def __init__(self):
        self.bg_color = c.LIGHT_GRAY
        self.title = pe.Label((30, c.SCREEN_HEIGHT // 2 - 80), "drove", font_size=110, color=c.BLACK, anchor="midleft", font=c.font_bold_path)
        self.subtitle = pe.Label((30, c.SCREEN_HEIGHT // 2 + 0), "The perfect driving game :)", font_size=50, color=c.BLACK, anchor="midleft", font=c.font_regular_path)
        self.credit_text = pe.Label((10, c.SCREEN_HEIGHT-10), "Made by ethandadev", font_size=25, color=c.BLACK, anchor="bottomleft", font=c.font_regular_path)
        self.image = pg.image.load("assets/car_display.png").convert_alpha()
        self.play_button = pe.Button((30, c.SCREEN_HEIGHT // 2 + 80), size=(300, 70), text="Play", font=c.font_bold_path, font_size=40, anchor="midleft", border_radius=8)
        self.quit_button = pe.Button((30, c.SCREEN_HEIGHT // 2 + 160), size=(300, 70), text="Quit", font=c.font_bold_path, font_size=40, anchor="midleft", border_radius=8)

    def handle_event(self, event):
        self.play_button.handle_event(event)
        self.quit_button.handle_event(event)

    def draw(self, screen):
        screen.fill(self.bg_color)
        self.title.draw(screen)
        self.subtitle.draw(screen)
        screen.blit(self.image, (c.SCREEN_WIDTH // 2 - 20, 80))
        self.credit_text.draw(screen)
        self.play_button.draw(screen)
        self.quit_button.draw(screen)


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    menu = StartMenu()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            menu.handle_event(event)

        if menu.play_button.was_clicked():
            print("Play clicked!")

        menu.draw(screen)
        pg.display.flip()

    pg.quit()