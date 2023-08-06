import cowsay

from mitch_dm_mypkg.shusayer.shusayer import Shu


class AgroShu(Shu):

    def say(self, message):
        getattr(cowsay, self.style)(message.upper())
