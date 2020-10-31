import random
import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)


class Ball(object):
    def __init__(self, screen, radius, x, y):
        self.__screen = screen
        self._radius = radius
        self._xLoc = x
        self._yLoc = y
        self.__xVel = 7
        self.__yVel = 2
        w, h = pygame.display.get_surface().get_size()
        self.__width = w
        self.__height = h

    def getXVel(self):
        return self.__xVel

    def getYVel(self):
        return self.__yVel

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0),
                           (self._xLoc, self._yLoc), self._radius)

    def update(self, paddle, brickwall):
        self._xLoc += self.__xVel
        self._yLoc += self.__yVel
        if self._xLoc <= self._radius:
            self.__xVel *= -1
        elif self._xLoc >= self.__width - self._radius:
            self.__xVel *= -1
        if self._yLoc <= self._radius:
            self.__yVel *= -1
        elif self._yLoc >= self.__width - self._radius:
            return True
        if brickwall.collide(self):
            self.__yVel *= -1
        paddleY = paddle._yLoc
        paddleW = paddle._width
        paddleH = paddle._height
        paddleX = paddle._xLoc
        ballX = self._xLoc
        ballY = self._yLoc
        if ((ballX + self._radius) >= paddleX and ballX <= (paddleX + paddleW)) \
                and ((ballY + self._radius) >= paddleY and ballY <= (paddleY + paddleH)):
            self.__yVel *= -1
        return False



class Paddle(object):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self._xLoc,
                                             self._yLoc, self._width, self._height), 0)

    def update(self):
        x, y = pygame.mouse.get_pos()
        if x >= 0 and x <= (self.__W - self._width):
            self._xLoc = x


class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h
        self.__isInGroup = False

    def draw(self):
        pygame.draw.rect(screen, (255 ,177, 237), (self._xLoc,
                                                  self._yLoc, self._width, self._height), 0)

    def add(self, group):
        group.add(self)
        self.__isInGroup = True

    def remove(self, group):
        group.remove(self)
        self.__isInGroup = False

    def alive(self):
        return self.__isInGroup

    def collide(self, ball):
        brickX = self._xLoc
        brickY = self._yLoc
        brickW = self._width
        brickH = self._height
        ballX = ball._xLoc
        ballY = ball._yLoc
        ballXVel = ball.getXVel()
        ballYVel = ball.getYVel()
        if ((ballX + ball._radius) >= brickX and (ballX + ball._radius) <= (brickX + brickW)) \
                and ((ballY - ball._radius) >= brickY and (ballY - ball._radius)
                     <= (brickY + brickH)):
            return True
        else:
            return False




class BrickWall(pygame.sprite.Group):
    def __init__(self, screen, x, y, width, height):
        self.__screen = screen
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._bricks = []
        X = x
        Y = y
        for i in range(3):
            for j in range(4):
                self._bricks.append(Brick(screen, width, height, X, Y))
                X += width + (width / 7.0)
            Y += height + (height / 7.0)
            X = x

    def add(self, brick):
        self._bricks.append(brick)

    def remove(self, brick):
        self._bricks.remove(brick)

    def draw(self):
        for brick in self._bricks:
            if brick != None:
                brick.draw()

    def update(self, ball):
        for i in range(len(self._bricks)):
            if ((self._bricks[i] != None) and self._bricks[i].collide(ball)):
                self._bricks[i] = None
        for brick in self._bricks:
            if brick == None:
                self._bricks.remove(brick)

    def hasWin(self):
        return len(self._bricks) == 0

    def collide(self, ball):
        for brick in self._bricks:
            if brick.collide(ball):
                return True
        return False


ball = Ball(screen, 25, random.randint(1, 700), 250)
paddle = Paddle(screen, 100, 20, 250, 450)
brickWall = BrickWall(screen, 25, 25, 150, 50)
isGameOver = False
gameStatus = True
score = 0
pygame.display.set_caption("Brickout-game")
done = False
clock = pygame.time.Clock()
pygame.font.init()
mgGameOver = pygame.font.SysFont('courier', 32)
mgWin = pygame.font.SysFont('courier', 32)
mgScore = pygame.font.SysFont('courier', 32)
textsurfaceGameOver = mgGameOver.render('Game Over!', False, WHITE)
textsurfaceWin = mgWin.render("You win!", False, WHITE)
textsurfaceScore = mgScore.render("score: " + str(score), False, WHITE)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)
    if gameStatus:
        brickWall.draw()
        if brickWall.collide(ball):
            score += 10
        textsurfaceScore = mgScore.render(
            "score: " + str(score), False, WHITE)
        screen.blit(textsurfaceScore, (300, 0))
        brickWall.update(ball)
        paddle.draw()
        paddle.update()
        if ball.update(paddle, brickWall):
            isGameOver = True
            gameStatus = False
        if brickWall.hasWin():
            gameStatus = False
        ball.draw()
    else:
        if isGameOver:
            screen.blit(textsurfaceGameOver, (0, 0))
            textsurfaceScore = mgScore.render(
                "score: " + str(score), False, WHITE)
            screen.blit(textsurfaceScore, (300, 0))
        elif brickWall.hasWin():
            screen.blit(textsurfaceWin, (0, 0))
            textsurfaceScore = mgScore.render(
                "score: " + str(score), False, WHITE)
            screen.blit(textsurfaceScore, (300, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
