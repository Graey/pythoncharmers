from threading import Thread
from Background import Background
from PIL.Image import open as openImage
from PIL.ImageTk import PhotoImage


class Bird(Thread):
    __tag = "Bird"
    __isAlive = None
    __going_up = False
    __going_down = 0
    __times_skipped = 0
    __running = False
    decends = 0.00390625
    climbsUp = 0.0911458333

    def __init__(self, background, gameover_function, *screen_geometry, fp="bird.png", event="<Up>", descend_speed=5):
        if not isinstance(background, Background):
            raise TypeError(
                "The background argument must be an instance of Background.")
        if not callable(gameover_function):
            raise TypeError(
                "The gameover_method argument must be a callable object.")
        self.__canvas = background
        self.image_path = fp
        self.__descend_speed = descend_speed
        self.gameover_method = gameover_function
        self.__width = screen_geometry[0]
        self.__height = screen_geometry[1]
        self.decends *= self.__height
        self.decends = int(self.decends + 0.5)
        self.climbsUp *= self.__height
        self.climbsUp = int(self.climbsUp + 0.5)
        Thread.__init__(self)
        self.width = (self.__width // 100) * 6
        self.height = (self.__height // 100) * 11
        self.__canvas.bird_image = \
            self.getPhotoImage(image_path=self.image_path,
                               width=self.width, height=self.height, closeAfter=True)[0]
        self.__birdID = self.__canvas.create_image(self.__width // 2, self.__height // 2,
                                                   image=self.__canvas.bird_image, tag=self.__tag)
        self.__canvas.focus_force()
        self.__canvas.bind(event, self.jumps)
        self.__isAlive = True

    def birdIsAlive(self):
        return self.__isAlive

    def checkCollision(self):
        position = list(self.__canvas.bbox(self.__tag))
        if position[3] >= self.__height + 20:
            self.__isAlive = False
        if position[1] <= -20:
            self.__isAlive = False
        position[0] += int(25 / 78 * self.width)
        position[1] += int(25 / 77 * self.height)
        position[2] -= int(20 / 78 * self.width)
        position[3] -= int(10 / 77 * self.width)
        ignored_collisions = self.__canvas.getBackgroundID()
        ignored_collisions.append(self.__birdID)
        possible_collisions = list(self.__canvas.find_overlapping(*position))
        for _id in ignored_collisions:
            try:
                possible_collisions.remove(_id)
            except:
                continue
        if len(possible_collisions) >= 1:
            self.__isAlive = False
        return not self.__isAlive

    def getTag(self):
        return self.__tag

    @staticmethod
    def getPhotoImage(image=None, image_path=None, width=None, height=None, closeAfter=False):
        if not image:
            if not image_path:
                return
            image = openImage(image_path)
        if not width:
            width = image.width
        if not height:
            height = image.height
        newImage = image.resize([width, height])
        photoImage = PhotoImage(newImage)
        if closeAfter:
            newImage.close()
            newImage = None
            image.close()
            image = None
        return photoImage, newImage, image

    def jumps(self, event=None):
        self.checkCollision()
        if not self.__isAlive or not self.__running:
            self.__going_up = False
            return
        self.__going_up = True
        self.__going_down = 0
        if self.__times_skipped < self.climbsUp:
            self.__canvas.move(self.__tag, 0, -1)
            self.__times_skipped += 1
            self.__canvas.after(3, self.jumps)
        else:
            self.__going_up = False
            self.__times_skipped = 0

    def kill(self):
        self.__isAlive = False

    def run(self):
        self.__running = True
        self.checkCollision()
        if self.__going_down < self.decends:
            self.__going_down += 0.05
        if self.__isAlive:
            if not self.__going_up:
                self.__canvas.move(self.__tag, 0, self.__going_down)
            self.__canvas.after(self.__descend_speed, self.run)
        else:
            self.__running = False
            self.gameover_method()