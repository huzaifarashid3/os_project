import pygame
from network import Network
from player import Player
from ball import Ball
from canvas import Canvas
from helper_functions import *

pygame.init()


class Game():
    def __init__(self, w, h):
        # self.n = Network()
        # self.startPos = read_pos(self.n.getPos())
        self.player = Player(10, 20, yellow, 15, 80)
        self.ball = Ball(w/2, h/2, 30, 10, 10, red)
        self.canvas = Canvas(w, h, bg_color, "testing")
        self.run = True

    def start(self):
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(60)
            self.input_handling()
            self.modify()
            self.render()
        pygame.quit()

    def input_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player.vel = 10
                if event.key == pygame.K_UP:
                    self.player.vel = -10
            if event.type == pygame.KEYUP:
                self.player.vel = 0

    def render(self):
        self.canvas.draw_background()
        self.player.draw(self.canvas.get_canvas())
        self.ball.draw(self.canvas.get_canvas())
        self.canvas.update()

    def modify(self):
        self.player.move()
        self.ball.move()
        self.ball.collision(self.player.p)