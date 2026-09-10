import pygame as pg

class Car:
    def __init__(self, x, y, image):
        pg.init()
        self.x = x
        self.y = y
        self.image