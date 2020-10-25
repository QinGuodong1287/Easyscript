import sys
from subprocess import Popen

def quit() -> int:
    return sys.exit(0)

def execute(command: str) -> int:
    Popen(command, shell=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr).wait()
    return 0

def move(direction: str) -> int:
    if direction in ("up", "down", "left", "right"):
        return direction

def move_up():
    return move("up")

def move_down():
    return move("down")

def move_left():
    return move("left")

def move_right():
    return move("right")
