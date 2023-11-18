class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        This initialises the status and muted values to a base value of false, and this
        sets the volume and channel to the min values.
        The temp_volume is for muting and unmuting to save the volume so it can be accessed
        later when unmuted.
        :return None:
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__temp_volume = 0

    def power(self) -> None:
        '''
        Switches status of television class between true and false
        :return None:
        '''
        self.__status = not self.__status
        self.__muted = False

    def mute(self) -> None:
        '''
        Switches muted status between true and false.
        If the status is set to true it saves the volume in
        temp_volume for later use when the status is switched back
        :return None:
        '''
        if self.__status:
            if self.__muted is False:
                self.__temp_volume = self.__volume
                self.__volume = 0
                self.__muted = True
            elif self.__muted:
                self.__volume = self.__temp_volume
                self.__muted = False

    def channel_up(self) -> None:
        '''
        Ticks the channel num up 1 and sets it to the minimum
        channel num if it goes past the max.
        :return None:
        '''
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Ticks the channel num down 1 and sets it to the maximum
        channel num if it goes past the min.
        :return None:
        '''
        if self.__status is True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        ticks volume up and unmutes if muted.
        When volume reaches max it will stay there
        :return None:
        '''
        if self.__status:
            if self.__muted is True:
                self.mute()
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        ticks volume down and unmutes if muted.
        When volume reaches min it will stay there
        :return None:
        '''
        if self.__status is True:
            if self.__muted is True:
                self.mute()
            if self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1


    def __str__(self) -> str:
        '''
        displays television status, channel, and volume
        :return str:
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'