class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__temp_volume = 0

    def power(self):
        self.__status = not self.__status
        self.__muted = False

    def mute(self):
        if self.__status:
            if self.__muted is False:
                self.__temp_volume = self.__volume
                self.__volume = 0
                self.__muted = True
            elif self.__muted:
                self.__volume = self.__temp_volume
                self.__muted = False

    def channel_up(self):
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status is True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status:
            if self.__muted is True:
                self.mute()
                if self.__volume == self.MAX_VOLUME:
                    pass
                else:
                    self.__volume += 1
            elif self.__muted is False:
                if self.__volume == self.MAX_VOLUME:
                    pass
                else:
                    self.__volume += 1

    def volume_down(self):
        if self.__status is True:
            if self.__muted is True:
                self.mute()
                if self.__volume == self.MIN_VOLUME:
                    pass
                else:
                    self.__volume -= 1
            elif self.__muted is False:
                if self.__volume == self.MIN_VOLUME:
                    pass
                else:
                    self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'