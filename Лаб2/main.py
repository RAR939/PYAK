from colorama import Fore, Style, just_fix_windows_console

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


def build_figures(n):
    return (
        Rectangle(n, n, "синий"),
        Circle(n, "зелёный"),
        Square(n, "красный"),
    )


def main():
    just_fix_windows_console()
    for figure, color in zip(build_figures(20), (Fore.BLUE, Fore.GREEN, Fore.RED)):
        print(color + repr(figure) + Style.RESET_ALL)


if __name__ == "__main__":
    main()
