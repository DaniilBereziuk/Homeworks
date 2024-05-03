class COMPUTER:

    def __init__(self, monitor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = '2TB'
        self.monitor = monitor


class Motherboard:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.processor = 'intel core i9'
        self.operative_memory = '64GB'

    def brain(self):
        print('I the brain of computer..')

class Videocard:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.videocard = 'RTX Geforce 4090'

    def video(self):
        print('I make a photo on screen..')


class PC(COMPUTER, Videocard, Motherboard):

    def print_info(self):
        print(self.monitor)
        print(self.memory)
        print(self.processor)
        print(self.operative_memory)
        print(self.videocard)

pc = PC(monitor='Samsung')
pc.print_info()