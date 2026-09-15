import math
import pygame as pg


class Car:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.angle = 0
        self.speed = 0
        self.max_speed = 36
        self.acceleration = 0.2
        self.friction = 0.05
        self.turn_speed = 4
        print("[Car Controller] Initialized")

    def update(self, keys_pressed, tile_on):
        if tile_on == 0:
            self.speed /= 1.5 if self.speed > 4 else 1
            grass_penalty = 0.5
        else:
            grass_penalty = 1
        abs_speed = abs(self.speed)
        turn_modifier = self.get_turn_modifier(abs_speed)

        steering_dir = -1 if self.speed < 0 else 1

        if keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]:
            self.angle += self.turn_speed * turn_modifier * steering_dir * grass_penalty
        if keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]:
            self.angle -= self.turn_speed * turn_modifier * steering_dir * grass_penalty

        if keys_pressed[pg.K_UP] or keys_pressed[pg.K_w]:
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys_pressed[pg.K_DOWN] or keys_pressed[pg.K_s]:
            self.speed = max(self.speed - self.acceleration, -self.max_speed / 2)
        else:
            if self.speed > 0:
                self.speed = max(0, self.speed - self.friction)
            elif self.speed < 0:
                self.speed = min(0, self.speed + self.friction)

        rad = math.radians(self.angle)
        dx = -math.sin(rad) * self.speed
        dy = -math.cos(rad) * self.speed

        self.x += dx
        self.y += dy

    def draw(self, surface, x=None, y=None):
        draw_x = x if x is not None else self.x
        draw_y = y if y is not None else self.y
        rotated_image = pg.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=(draw_x, draw_y))
        surface.blit(rotated_image, new_rect.topleft)
        #surface.blit(self.image, (draw_x, draw_y))

    def get_speed(self):
        return self.speed*3.2

    def get_turn_modifier(self, abs_speed: float) -> float:
        if abs_speed <= 0:
            return 0.01

        ramp_up = 1.0 - math.exp(-3.5 * abs_speed)

        speed_past_peak = max(0.0, abs_speed - 3.5)
        decay = math.exp(-0.15 * speed_past_peak)

        min_turn_ratio = 0.45

        return max(min_turn_ratio, ramp_up * decay)