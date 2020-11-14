import sys
import tty, termios

fd = sys.stdin.fileno()
settings = termios.tcgetattr(fd)

def get_character(prompt: str="") -> str:
    try:
        if prompt:
            print(prompt, end='', flush=True)
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    return ch
