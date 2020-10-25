import os, sys

from tools import contorl, reader

filepath = os.path.dirname(os.path.abspath(__file__)) + "/CN/"
keylayouts = {
    "q": contorl.quit,       # Quit the manaul
    "j": contorl.move_down,  # Go to down text
    "k": contorl.move_up,    # Go to up text
    "h": contorl.move_left,  # Go to pervious text
    "l": contorl.move_right  # Go to next text
}
keys = tuple(keylayouts.keys())

def main() -> int:
    print("""Welcome to the Syntax manaul for Easyscript programming language.
Press any key to read this manaul.
Keys:
q: quit this manaul
j: move the page down.
k: move the page up.
h: read pervious text.
l: read next text.""")
    while True:
        ch = reader.get_character().lower()
        if ch not in keys:
            continue
        contorl.execute("clear")
        try:
            keylayouts[ch]()
        except SystemExit: # Exit this manual
            break
        except:
            pass
        print("""Welcome to the Syntax manaul for Easyscript programming language.
Press any key to read this manaul.
Keys:
q: quit this manaul
j: move the page down.
k: move the page up.
h: read pervious text.
l: read next text.""")
    return 0

if __name__ == "__main__":
    main()
