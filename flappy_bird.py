import pygame as pg 
import sys
pg.init()

class Game:
    def __init__(self):
        self.width = 600
        self.height= 768
        self.win=pg.display.set_mode((self.width,self.height))
        self.bg_img=pg.image.load
        self.gameLoop()
    
    def gameLoop(self):
        while True:
            for events in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

game=Game()