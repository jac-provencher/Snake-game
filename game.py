import pygame
from random import randint

pygame.init()

class Cube:

    def __init__(self, startingPoint, direction=(1, 0)):
        pass

    def move(self, direction):
        pass

    def draw(self, surface, eyes=False):
        pass

class Snake:

    bodyparts = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)
        self.bodyparts.append(self.head)
        self.x, self.y = position
        self.snakeDirection = (1, 0)
        self.speed = 15
        self.vector = {'right': (1, 0), 'left': (-1, 0), 'up': (0, -1), 'down': (0, 1), 'statique': (0, 0)}

    def move(self, direction):

        self.snakeDirection = i, j = self.vector[direction]
        self.x += self.speed*i
        self.y += self.speed*j

        self.turns[(self.x, self. y)] = self.snakeDirection

    def addcube(self):
        pass

class Window:

    def __init__(self):

        pygame.display.set_caption("Snake")
        self.screenHeight, self.screenWidth = 450, 450
        self.screen = pygame.display.set_mode((self.screenHeight, self.screenWidth))
        self.snake = Snake((0, 255, 0), (90, 240))
        self.running = True

    def redrawSnake(self):

        snakeDimension = self.screenHeight//15
        pygame.draw.rect(self.screen, self.snake.color, (self.snake.x, self.snake.y, snakeDimension, snakeDimension))

    def redrawLines(self):

        rowWidth = self.screenHeight//15
        for n in range(0, self.screenHeight, rowWidth):
            pygame.draw.line(self.screen, (105, 105, 105), (n, 0), (n, self.screenHeight))
            pygame.draw.line(self.screen, (105, 105, 105), (0, n), (self.screenWidth, n))

    def mainloop(self):

        direction = 'statique'

        while self.running:

            pygame.time.delay(75)
            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            if keys[pygame.K_LEFT]:
                direction = 'left'
            elif keys[pygame.K_RIGHT]:
                direction = 'right'
            elif keys[pygame.K_UP]:
                direction = 'up'
            elif keys[pygame.K_DOWN]:
                direction = 'down'

            self.snake.move(direction)

            self.screen.fill((0, 0, 0))

            self.redrawSnake()
            self.redrawLines()

            pygame.display.update()

game = Window()
game.mainloop()

pygame.quit()
