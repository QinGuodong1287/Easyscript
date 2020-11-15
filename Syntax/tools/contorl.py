import os, sys
from subprocess import Popen, PIPE
from time import sleep

program_path = os.path.dirname(os.path.abspath(__file__))

from . import cursor_contorl, settings, fonts, reader

cursor_contorl.hide_cursor()

def execute(command: str, output: bool=True) -> int:
    Popen(command, shell=True, stdin=sys.stdin, stdout=(sys.stdout if output else PIPE), stderr=sys.stderr).wait()
    return 0

execute("clear")
filepath = program_path + "/../Syntax_manaul/EN/Special_characters.txt"

def quit() -> int:
    choice = ''
    while choice not in ('y', 'n'):
        execute("clear")
        print(settings.title)
        choice = reader.get_character("Quit any way? (y/n)")
        if choice == 'y':
            cursor_contorl.show_cursor()
            return sys.exit(0)
        elif choice == 'n':
            print_text()
            return 0
        else:
            for sec in range(3, -1, -1):
                execute("clear")
                print(settings.title)
                print("\rYour choice is wrong. Please choose again after {} {}.".format(sec, "seconds" if sec != 1 else "second"), end='', flush=True)
                sleep(1)
                
def print_text() -> None:
    execute("clear")
    print(settings.title)
    with open(filepath) as fp:
        text_list = [line.rstrip() for line in fp.readlines()]
    text_list[0] = fonts.Font.bold(text_list[0])
    print('\n'.join(text_list))

def fill_screen(lines: list or tuple) -> str:
    if isinstance(lines, dict):
        raise ValueError("The lines list's type can't be a dict!")
    text_list = lines[:]
    if text_list[0] != settings.title:
        text_list.insert(0, settings.title)
    text_list = [text_list[0]] + [fonts.Font.white_background(line + ' ' * (settings.screen_columns - len(line))) for line in text_list[1:settings.screen_lines]]
    text_list += [fonts.Font.white_background(' ' * settings.screen_columns) for _ in range(len(text_list), settings.screen_lines - 1)]
    return '\n'.join(text_list)

def move(direction: str) -> int:
    if direction not in ("up", "down", "left", "right"):
        return 1
    print_text()
    return 0

def move_up():
    return move("up")

def move_down():
    return move("down")

def move_left():
    return move("left")

def move_right():
    return move("right")
