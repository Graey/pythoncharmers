from tkinter import Tk
from tkinter import Canvas
from PIL.Image import open as openImage
from PIL.ImageTk import PhotoImage


class Background(Canvas):

    __background = []
    __stop = False

    def __init__(self, tk_instance, *geometry, fp="background.png", animation_speed=50):
        if not isinstance(tk_instance, Tk):
            raise TypeError(
                "The tk_instance argument must be an instance of Tk.")
        self.image_path = fp
        self.animation_speed = animation_speed
        self.__width = geometry[0]
        self.__height = geometry[1]
        Canvas.__init__(self, master=tk_instance,
                        width=self.__width, height=self.__height)
        self.__bg_image = \
            self.getPhotoImage(image_path=self.image_path, width=self.__width,
                               height=self.__height, closeAfter=True)[0]
        self.__background_default = self.create_image(
            self.__width // 2, self.__height // 2, image=self.__bg_image)
        self.__background.append(self.create_image(
            self.__width // 2, self.__height // 2, image=self.__bg_image))
        self.__background.append(
            self.create_image(self.__width + (self.__width // 2), self.__height // 2, image=self.__bg_image))

    def getBackgroundID(self):

        return [self.__background_default, *self.__background]

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

    def reset(self):

        self.delete("all")
        self.__stop = False
        self.__background.clear()
        self.__background_default = self.create_image(
            self.__width // 2, self.__height // 2, image=self.__bg_image)
        self.__background.append(self.create_image(
            self.__width // 2, self.__height // 2, image=self.__bg_image))
        self.__background.append(
            self.create_image(self.__width + (self.__width // 2), self.__height // 2, image=self.__bg_image))

    def run(self):

        if not self.__stop:
            self.move(self.__background[0], -10, 0)
            self.move(self.__background[1], -10, 0)
            self.tag_lower(self.__background[0])
            self.tag_lower(self.__background[1])
            self.tag_lower(self.__background_default)
            if self.bbox(self.__background[0])[2] <= 0:
                self.delete(self.__background[0])
                self.__background.remove(self.__background[0])
                width = self.bbox(self.__background[0])[2] + self.__width // 2
                self.__background.append(self.create_image(
                    width, self.__height // 2, image=self.__bg_image))
            self.after(self.animation_speed, self.run)

    def stop(self):

        self.__stop = True