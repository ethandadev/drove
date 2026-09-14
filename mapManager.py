import math

import pygame as pg
import constants as c


class mapManager:
    def __init__(self):
        self.map = None
        self.map_data = []
        self.tiles = []
        self.map_width = 0
        self.map_height = 0
        print("[Map Manager] Initialized")

    def load_level_data(self, filepath):
        grid = []
        with open(filepath, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                row = [int(char.strip()) for char in cleaned_line.split(',') if char.strip()]
                if row:
                    grid.append(row)
        self.map_data = grid

    def load_tiles(self):
        self.tiles = {}
        for tile_id, path in c.TILES.items():
            image = pg.image.load(path).convert_alpha()
            image = pg.transform.scale(image, (c.TILE_SIZE, c.TILE_SIZE))
            self.tiles[tile_id] = image

    def load_map(self):
        print("[Map Manager] Starting to Load Map")
        try:
            self.load_level_data(c.map1)
            self.load_tiles()

            rows = len(self.map_data)
            cols = len(self.map_data[0]) if rows else 0

            self.map_width = cols * c.TILE_SIZE
            self.map_height = rows * c.TILE_SIZE
            self.map = pg.Surface((self.map_width, self.map_height)).convert_alpha()

            for row_index, row in enumerate(self.map_data):
                for col_index, tile_id in enumerate(row):
                    tile_image = self.tiles.get(tile_id)
                    if tile_image is None:
                        continue
                    self.map.blit(tile_image, (col_index * c.TILE_SIZE, row_index * c.TILE_SIZE))
            print("[Map Manager] Loaded Map")
        except Exception as e:
            print(f"[Map Manager] Error: {e}")

    def clamp_camera(self, camera_x, camera_y):
        max_x = max(0, self.map_width - c.SCREEN_WIDTH)
        max_y = max(0, self.map_height - c.SCREEN_HEIGHT)
        camera_x = max(0, min(camera_x, max_x))
        camera_y = max(0, min(camera_y, max_y))
        return camera_x, camera_y

    def draw(self, surface, camera_x, camera_y):
        surface.blit(self.map, (-camera_x, -camera_y))

    def draw_rotated(self, surface, world_x, world_y, angle):
        chunk_size = int(math.hypot(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)) + c.TILE_SIZE * 2
        chunk = pg.Surface((chunk_size, chunk_size)).convert_alpha()
        chunk.fill(c.GREEN)

        src_x = int(world_x - chunk_size / 2)
        src_y = int(world_y - chunk_size / 2)

        clip_left = max(src_x, 0)
        clip_top = max(src_y, 0)
        clip_right = min(src_x + chunk_size, self.map_width)
        clip_bottom = min(src_y + chunk_size, self.map_height)

        if clip_right > clip_left and clip_bottom > clip_top:
            area = pg.Rect(clip_left, clip_top, clip_right - clip_left, clip_bottom - clip_top)
            dest = (clip_left - src_x, clip_top - src_y)
            chunk.blit(self.map, dest, area)

        rotated = pg.transform.rotate(chunk, -angle)
        dest_rect = rotated.get_rect(center=(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2))
        surface.blit(rotated, dest_rect.topleft)

    def get_tile_at(self, x, y):
        col = int(x // c.TILE_SIZE)
        row = int(y // c.TILE_SIZE)
        try:
            return self.map_data[row][col]
        except IndexError as e:
            print(f"[Map Manager] Error: {e}")



