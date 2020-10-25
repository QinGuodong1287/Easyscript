import sys
import tty, termios

fd = sys.stdin.fileno()
settings = termios.tcgetattr(fd)

def get_character() -> str:
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    return ch
