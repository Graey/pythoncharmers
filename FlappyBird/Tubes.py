from random import randint
from threading import Thread
from Background import Background
from Bird import Bird
from PIL.Image import open as openImage
from PIL.ImageTk import PhotoImage


class Tubes(Thread):
    __distance = 0
    __move = 10
    __pastTubes = []

    def __init__(self, background, bird, score_function=None, *screen_geometry, fp=("tube.png", "tube_mourth"),
                 animation_speed=50):
        if not isinstance(background, Background):
            raise TypeError(
                "The background argument must be an instance of Background.")
        if not len(fp) == 2:
            raise TypeError(
                "The parameter fp should be a sequence containing the path of the images of the tube body and the tube mouth.")
        if not isinstance(bird, Bird):
            raise TypeError("The birdargument must be an instance of Bird.")
        if not callable(score_function):
            raise TypeError(
                "The score_function argument must be a callable object.")
        Thread.__init__(self)
        self.__background = background
        self.image_path = fp
        self.__animation_speed = animation_speed
        self.__score_method = score_function
        self.__width = screen_geometry[0]
        self.__height = screen_geometry[1]
        self.__bird_w = bird.width
        self.__bird_h = bird.height
        self.__imageWidth = (self.__width // 100) * 10
        self.__imageHeight = (self.__height // 100) * 5
        try:
            self.deleteAll()
        except:
            self.__background.tubeImages = []
        self.__background.tubeImages.append([])
        self.__background.tubeImages.append(
            self.getPhotoImage(
                image_path=self.image_path[1],
                width=self.__imageWidth,
                height=self.__imageHeight,
                closeAfter=True)[0]
        )
        self.__background.tubeImages.append(
            self.getPhotoImage(
                image_path=self.image_path[0],
                width=self.__imageWidth,
                height=self.__imageHeight)[1]
        )
        self.__minDistance = int(self.__imageWidth * 4.5)
        self.__stop = False
        self.__tubes = []

    def createNewTubes(self):

        tube1 = []
        width = self.__width + (self.__imageWidth)
        height = randint(self.__imageHeight // 2, self.__height -
                         (self.__bird_h * 2) - self.__imageHeight)
        tube1.append(self.__background.create_image(
            width, height, image=self.__background.tubeImages[1]))
        self.__background.tubeImages[0].append(
            [self.getPhotoImage(image=self.__background.tubeImages[2],
                                width=self.__imageWidth, height=height)[0], ]
        )
        y = (height // 2) + 1 - (self.__imageHeight // 2)
        tube1.append(self.__background.create_image(
            width, y, image=self.__background.tubeImages[0][-1][0]))
        tube2 = []
        height = height + (self.__bird_h * 2) + self.__imageHeight - 1
        tube2.append(self.__background.create_image(
            width, height, image=self.__background.tubeImages[1]))
        height = self.__height - height
        self.__background.tubeImages[0][-1].append(
            self.getPhotoImage(
                image=self.__background.tubeImages[2], width=self.__imageWidth, height=height)[0]
        )
        y = (self.__height - (height // 2)) + self.__imageHeight // 2
        tube2.append(self.__background.create_image(
            width, y, image=self.__background.tubeImages[0][-1][1]))
        self.__tubes.append([tube1, tube2])
        self.__distance = 0

    def deleteAll(self):

        for tubes in self.__tubes:
            for tube in tubes:
                for body in tube:
                    self.__background.delete(body)
        self.__background.clear()
        self.__background.tubeImages.clear()

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

    def move(self):

        scored = False
        for tubes in self.__tubes:
            for tube in tubes:
                if not scored:
                    x2 = self.__background.bbox(tube[0])[2]
                    if (self.__width / 2) - (self.__bird_w / 2) - self.__move < x2:
                        if x2 <= (self.__width / 2) - (self.__bird_w / 2):
                            if not tube[0] in self.__pastTubes:
                                self.__score_method()
                                self.__pastTubes.append(tube[0])
                                scored = True
                for body in tube:
                    self.__background.move(body, -self.__move, 0)

    def run(self):

        if self.__stop:
            return
        if len(self.__tubes) >= 1 and self.__background.bbox(self.__tubes[0][0][0])[2] <= 0:
            for tube in self.__tubes[0]:
                for body in tube:
                    self.__background.delete(body)
            self.__background.tubeImages[0].remove(
                self.__background.tubeImages[0][0])
            self.__tubes.remove(self.__tubes[0])
            self.__pastTubes.remove(self.__pastTubes[0])
        if self.__distance >= self.__minDistance:
            self.createNewTubes()
        else:
            self.__distance += self.__move
        self.move()
        self.__background.after(self.__animation_speed, self.run)

    def stop(self):
        self.__stop = True