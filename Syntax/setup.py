import os, sys

program_path = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(program_path + "/error.txt"):
    os.remove(program_path + "/error.txt")

def show_cursor() -> None:
    print("\033[?25h")

from tools import reader, contorl, settings, fonts
build_ext_path = program_path + "/tools"
error_file_path = program_path + "/error.txt"
try:
    from tools import cursor_contorl # Import the extension
except ImportError: # If import is failed
    # Install the Cython extension
    cwd = os.getcwd()
    os.chdir(build_ext_path)
    print("\033[5mBuilding extension...\033[0m")
    contorl.execute("python install_setup.py build_ext --inplace")
    print("\033[5mInstalling extension...\033[0m")
    contorl.execute("python install_setup.py install")
    os.chdir(cwd)
    del cwd
    # Just import it
    try:
        from tools import cursor_contorl
    except ImportError: # If import is failed
        print("Can't inport the extension, exitting this program...")
        show_cursor()
        sys.exit(0)
contorl.execute("clear")

keylayouts = {
    "q": contorl.quit,       # Quit the manaul
    "j": contorl.move_down,  # Go to down text
    "k": contorl.move_up,    # Go to up text
    "h": contorl.move_left,  # Go to pervious text
    "l": contorl.move_right  # Go to next text
}
keys = tuple(keylayouts.keys())
welcome_text = f"""{settings.title}
Welcome to the Syntax manaul for Easyscript programming language.
Press any key to read this manaul.
Keys:
q: quit this manaul
j: move the page down.
k: move the page up.
h: read pervious text.
l: read next text."""
text_list = [line.rstrip() for line in welcome_text.splitlines()]
welcome_text = '\n'.join(text_list)
del text_list

def main() -> int:
    print(welcome_text)
    while True:
        ch = reader.get_character().lower()
        if ch not in keys:
            continue
        contorl.execute("clear")
        try:
            keylayouts[ch]()
        except SystemExit: # Exit this manual
            break
        except Exception as e:
            if os.path.exists(error_file_path):
                with open(error_file_path, 'a') as fp:
                    fp.write(str(e) + '\n')
            else:
                with open(error_file_path, 'w') as fp:
                    fp.write(str(e) + '\n')
    return 0

if __name__ == "__main__":
    main()
    contorl.execute("clear")
