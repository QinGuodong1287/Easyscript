def clear() -> None:
    print("\033[2J")

def move_up(y: int) -> None:
    print(f"\033[{y}A")

def move_down(y: int) -> None:
    print(f"\033[{y}B")

def move_left(x: int) -> None:
    print(f"\033[{x}D")

def move_right(x: int) -> None:
    print(f"\033[{x}C")

def move_to(x: int, y: int) -> None:
    print(f"\033[{x};{y}H")

def reset_cursor() -> None:
    print("\033[H")

def hide_cursor() -> None:
    print("\033[?25l")

def show_cursor() -> None:
    print("\033[?25h")

def hight_light() -> None:
    print("\033[7m")

def un_hight_light() -> None:
    print("\033[27m")

