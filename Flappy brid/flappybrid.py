import pygame as pg
import sys
import random

class Brid(object):
    imagelist = []
    state = 0
    pos = []
    speed = []
    def __init__(self):
        self.pos = [0,320]
        self.state = 0
        self.speed = [0,0]
        s0 = pg.image.load('D:/project/game/Flappy brid/assets/0.png')
        s1 = pg.image.load('D:/project/game/Flappy brid/assets/1.png')
        s2 = pg.image.load('D:/project/game/Flappy brid/assets/2.png')
        self.imagelist.append(s0)
        self.imagelist.append(s1)
        self.imagelist.append(s2)

    def bridUpdate(self):
        self.state = (self.state + 1) % 3
        #self.pos = self.pos + self.speed


class Pipe(object):
    def __init__(self):
        pass

if __name__ == "__main__":

    pg.init()
    size = length, width = 400,640
    screen = pg.display.set_mode(size)

    brid = Brid()
    
    background = pg.image.load('D:/project/game/Flappy brid/assets/background.png')
    color = (0,0,0)
    clock = pg.time.Clock()
    while True:
        clock.tick(6)
        for event in pg.event.get():  # envents 
            if event.type == pg.QUIT:  # quit
                pg.display.quit()
                sys.exit(0)
        screen.fill(color)
        screen.blit(background,(0,0))
        brid.bridUpdate()
        screen.blit(brid.imagelist[brid.state],brid.pos)
        pg.display.flip()


    
