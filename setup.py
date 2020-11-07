import os, sys

def show_cursor() -> None:
    print("\033[?25h")

file_path = os.path.dirname(os.path.abspath(__file__))
from tools import reader, contorl
build_ext_path = file_path + "/tools"
try:
    from tools import cursor_contorl # Import the extension
except ImportError: # If import is failed
    # Install the Cython extension
    pwd = os.getcwd()
    os.chdir(build_ext_path)
    print("\033[70mBuilding extension...\033[0m")
    contorl.execute("python install_setup.py build_ext --inplace")
    print("\033[70mInstalling extension...\033[0m")
    contorl.execute("python install_setup.py install")
    os.chdir(pwd)
    # Just import it
    try:
        import cursor_contorl
    except ImportError: # If import is failed
        print("Can't inport the extension, exitting this program...")
        del pwd
        show_cursor()
        sys.exit(0)
    del pwd
contorl.execute("clear")

text_path = file_path + "/Syntax_manaul/CN"
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
    contorl.execute("clear")
