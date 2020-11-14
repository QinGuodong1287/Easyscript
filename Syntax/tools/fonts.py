class Font():
    def bold(string: str) -> str:
        return f"\033[5m{string}\033[0m"

    def white_background(string: str) -> str:
        return f"\033[7m{string}\033[0m"

    def blue_background(string: str) -> str:
        return f"\033[44m{string}\033[0m"
