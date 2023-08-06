import cowsay


class Shu:

    def __init__(self, style):
        self.style = style

    def say(self, message):
        getattr(cowsay, self.style)(message)
