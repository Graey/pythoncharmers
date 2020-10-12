import os.path
from datetime import timedelta
from time import time
from tkinter import Tk, Button
from Background import Background
from Bird import Bird
from Settings import Settings
from Tubes import Tubes


class App(Tk, Settings):
    __background_animation_speed = 720
    __bestScore = 0
    __bird_descend_speed = 35
    __buttons = []
    __playing = False
    __score = 0
    __time = "%H:%M:%S"

    def __init__(self):
        Tk.__init__(self)
        self.setOptions()
        if all([self.window_width, self.window_height]):
            self.__width = self.window_width
            self.__height = self.window_height
        else:
            self.__width = self.winfo_screenwidth()
            self.__height = self.winfo_screenheight()
        self.title(self.window_name)
        self.geometry("{}x{}".format(self.__width, self.__height))
        self.resizable(*self.window_rz)
        self.attributes("-fullscreen", self.window_fullscreen)
        self["bg"] = "black"
        for file in self.images_fp:
            if not os.path.exists(file):
                raise FileNotFoundError(
                    "The following file was not found:\n{}".format(file))
        self.__startButton_image = Background.getPhotoImage(
            image_path=self.startButton_fp,
            width=(self.__width // 100) * self.button_width,
            height=(self.__height // 100) * self.button_height,
            closeAfter=True
        )[0]
        self.__exitButton_image = Background.getPhotoImage(
            image_path=self.exitButton_fp,
            width=(self.__width // 100) * self.button_width,
            height=(self.__height // 100) * self.button_height,
            closeAfter=True
        )[0]
        self.__title_image = Background.getPhotoImage(
            image_path=self.title_fp,
            width=(self.__width // 100) * self.title_width,
            height=(self.__height // 100) * self.title_height,
            closeAfter=True
        )[0]
        self.__scoreboard_image = Background.getPhotoImage(
            image_path=self.scoreboard_fp,
            width=(self.__width // 100) * self.scoreboard_width,
            height=(self.__height // 100) * self.scoreboard_height,
            closeAfter=True
        )[0]
        self.__background_animation_speed //= self.__width / 100
        self.__background_animation_speed = int(
            self.__background_animation_speed)
        self.__bird_descend_speed //= self.__height / 100
        self.__bird_descend_speed = int(self.__bird_descend_speed)

    def changeFullscreenOption(self, event=None):

        self.window_fullscreen = not self.window_fullscreen
        self.attributes("-fullscreen", self.window_fullscreen)

    def close(self, event=None):

        self.saveScore()
        try:
            self.__background.stop()
            self.__bird.kill()
            self.__tubes.stop()
        finally:
            quit()

    def createMenuButtons(self):

        width = (self.__width // 100) * self.button_width
        height = (self.__height // 100) * self.button_height
        startButton = Button(
            self, image=self.__startButton_image, bd=0, command=self.start, cursor=self.button_cursor,
            bg=self.button_bg, activebackground=self.button_activebackground
        )
        self.__buttons.append(
            self.__background.create_window((self.__width // 2) - width // 1.5,
                                            int(self.__height / 100 *
                                                self.button_position_y),
                                            window=startButton))
        exitButton = Button(
            self, image=self.__exitButton_image, bd=0, command=self.close, cursor=self.button_cursor,
            bg=self.button_bg, activebackground=self.button_activebackground
        )
        self.__buttons.append(
            self.__background.create_window((self.__width // 2) + width // 1.5,
                                            int(self.__height / 100 *
                                                self.button_position_y),
                                            window=exitButton))

    def createScoreBoard(self):

        x = self.__width // 2
        y = (self.__height // 100) * self.scoreboard_position_y
        scoreboard_w = (self.__width // 100) * self.scoreboard_width
        scoreboard_h = (self.__width // 100) * self.scoreboard_height
        score_x = x - scoreboard_w / 100 * 60 / 2
        score_y = y + scoreboard_h / 100 * 10 / 2
        bestScore_x = x + scoreboard_w / 100 * 35 / 2
        bestScore_y = y + scoreboard_h / 100 * 10 / 2
        time_x = x
        time_y = y + scoreboard_h / 100 * 35 / 2
        font = (self.text_font, int(0.02196 * self.__width + 0.5))
        self.__background.create_image(x, y, image=self.__scoreboard_image)
        self.__background.create_text(
            score_x, score_y, text="Score: %s" % self.__score,
            fill=self.text_fill, font=font
        )
        self.__background.create_text(
            bestScore_x, bestScore_y, text="Best Score: %s" % self.__bestScore,
            fill=self.text_fill, font=font
        )
        self.__background.create_text(
            time_x, time_y, text="Time: %s" % self.__time,
            fill=self.text_fill, font=font
        )

    def createTitleImage(self):

        self.__background.create_image(self.__width // 2, (self.__height // 100) * self.title_position_y,
                                       image=self.__title_image)

    def deleteMenuButtons(self):

        for item in self.__buttons:
            self.__background.delete(item)
        self.__buttons.clear()

    def gameOver(self):

        self.__time = int(time() - float(self.__time))
        self.__time = str(timedelta(seconds=self.__time))
        self.__background.stop()
        self.__tubes.stop()
        self.__playing = False
        self.createMenuButtons()
        self.createTitleImage()
        self.createScoreBoard()

    def increaseScore(self):

        self.__score += 1
        if self.__score > self.__bestScore:
            self.__bestScore = self.__score

    def init(self):

        self.loadScore()
        self.__background = Background(
            self, self.__width, self.__height, fp=self.background_fp, animation_speed=self.__background_animation_speed
        )
        self.__background.focus_force()
        self.__background.bind(self.window_fullscreen_event,
                               self.changeFullscreenOption)
        self.__background.bind(self.window_start_event, self.start)
        self.__background.bind(self.window_exit_event, self.close)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.__background.pack()
        self.createMenuButtons()
        self.createTitleImage()
        self.__bird = Bird(
            self.__background, self.gameOver, self.__width, self.__height,
            fp=self.bird_fp, event=self.bird_event, descend_speed=self.__bird_descend_speed
        )

    def loadScore(self):

        try:
            file = open(self.score_fp)
            self.__bestScore = int(file.read(), 2)
            file.close()
        except:
            file = open(self.score_fp, 'w')
            file.write(bin(self.__bestScore))
            file.close()

    def saveScore(self):

        with open(self.score_fp, 'w') as file:
            file.write(bin(self.__bestScore))

    def start(self, event=None):

        if self.__playing:
            return
        self.__score = 0
        self.__time = time()
        self.deleteMenuButtons()
        self.__background.reset()
        if self.background_animation:
            self.__background.run()
        self.__bird = Bird(
            self.__background, self.gameOver, self.__width, self.__height,
            fp=self.bird_fp, event=self.bird_event, descend_speed=self.__bird_descend_speed
        )
        self.__tubes = Tubes(
            self.__background, self.__bird, self.increaseScore, self.__width, self.__height,
            fp=self.tube_fp, animation_speed=self.__background_animation_speed
        )
        self.__bird.start()
        self.__tubes.start()


if __name__ == "__main__":
    try:
        app = App()
        app.init()
        app.mainloop()
    except FileNotFoundError as error:
        print(error)