import os
from .fonts import Font

title = Font.blue_background(Font.bold(f"Syntax manaul for Easyscript programming language"))
title = f"{title}\033[44m\033[5m{' ' * (os.get_terminal_size().columns - len(title) + 17)}\033[0m"
manaul_path = os.path.dirname(os.path.abspath(__file__)) + "/../Syntax_manaul/EN"
contents = {
    "EN": {
        "Special characters": manaul_path + "/Special_characters.txt", 
        "Single references": {
            "Single operators": manaul_path + "/Single_references/Single_operators.txt"
        }
    }
}
screen_columns = os.get_terminal_size().columns
screen_lines = os.get_terminal_size().lines
