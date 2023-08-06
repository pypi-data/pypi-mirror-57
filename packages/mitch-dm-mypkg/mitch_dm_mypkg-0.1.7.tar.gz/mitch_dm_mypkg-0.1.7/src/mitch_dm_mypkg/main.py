import sys

from src.mitch_dm_mypkg.shusayer.shusayer import Shu


def run(style, message):
    Shu(style).say(message)


def cli():
    try:
        run(sys.argv[1], sys.argv[2])
    except IndexError:
        run(
            style='turkey',
            message='Too chicken to make me say something?',
        )


if __name__ == '__main__':
    cli()
