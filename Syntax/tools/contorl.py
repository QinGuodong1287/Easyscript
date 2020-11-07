import sys
from subprocess import Popen
from atexit import register

import cursor_contorl

cursor_contorl.hide_cursor()

def execute(command: str) -> int:
    Popen(command, shell=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr).wait()
    return 0

execute("clear")

def quit() -> int:
    execute("clear")
    cursor_contorl.show_cursor()
    return sys.exit(0)

def move(direction: str) -> int:
    if direction in ("up", "down", "left", "right"):
        return 0
    else:
        return 1

def move_up():
    return move("up")

def move_down():
    return move("down")

def move_left():
    return move("left")

def move_right():
    return move("right")
