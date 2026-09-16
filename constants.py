import pygame as pg

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

TILE_SIZE = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (200, 200, 200)
GRAY = (128, 128, 128)
GREEN = (60, 208, 0)

name = "drove"

MINIMAP_SIZE = 180
MINIMAP_MARGIN = 16

#Paths

car1_path = "assets/car1.png"
car1_width = 75
car1_height = 150


#maps

TILES = {
    0: "assets/tiles/grass_tile.png",
    1: "assets/tiles/straight_vertical_left_tile.png",
    2: "assets/tiles/straight_vertical_right_tile.png",
    3: "assets/tiles/straight_horizontal_left_tile.png",
    4: "assets/tiles/straight_horizontal_right_tile.png",
    5: "assets/tiles/road_empty_tile.png",
    6: "assets/tiles/straight_vertical_left_empty.png",
    7: "assets/tiles/straight_vertical_right_empty.png",
    8: "assets/tiles/straight_horizontal_left_empty.png",
    9: "assets/tiles/straight_horizontal_right_empty.png",
    10: "assets/tiles/road_corner_top_left.png",
    11: "assets/tiles/road_corner_top_right.png",
    12: "assets/tiles/road_corner_bottom_left.png",
    13: "assets/tiles/road_corner_bottom_right.png",
}

map1 = "assets/drove-map-1.txt"

#fonts
font_regular_path = "assets/font_regular.otf"
font_bold_path = "assets/font_bold.otf"