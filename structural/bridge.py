class Remote(object):

    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        if self.device.is_turn_on():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)


class AdvancedRemote(Remote):

    def __init__(self, device):
        super(AdvancedRemote, self).__init__(device)

    def mute(self):
        self.device.set_volume(0)


class Device(object):

    def is_turn_on(self):
        raise NotImplementedError()

    def enable(self):
        raise NotImplementedError()

    def disable(self):
        raise NotImplementedError()

    def set_channel(self, channel):
        raise NotImplementedError()

    def get_channel(self):
        raise NotImplementedError()

    def set_volume(self, percent):
        raise NotImplementedError()

    def get_volume(self):
        raise NotImplementedError()


class TV(Device):

    def __init__(self, name):
        self.name = name
        self.is_enable = False
        self.volume = 0
        self.channel = 0

    def is_turn_on(self):
        return self.is_enable

    def enable(self):
        self.is_enable = True

    def disable(self):
        self.is_enable = False

    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel

    def set_volume(self, percent):
        self.volume = percent

    def get_volume(self):
        return self.volume


if __name__ == '__main__':

    sony_tv = TV('Sony')
    remote_sony = AdvancedRemote(sony_tv)
    remote_sony.toggle_power()
    print(sony_tv.is_turn_on())
    remote_sony.channel_up()
    print(sony_tv.name, 'channel is', sony_tv.channel)
    print(sony_tv.name, 'volume is', sony_tv.volume)
    remote_sony.volume_up()
    print("VOLUME UP...")
    print(sony_tv.name, 'volume is', sony_tv.volume)



