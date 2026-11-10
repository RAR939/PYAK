from colorama import Fore, Style, just_fix_windows_console

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


def main():
    n = 20

    just_fix_windows_console()
    print(Fore.BLUE + repr(Rectangle(n, n, "синий")) + Style.RESET_ALL)
    print(Fore.GREEN + repr(Circle(n, "зелёный")) + Style.RESET_ALL)
    print(Fore.RED + repr(Square(n, "красный")) + Style.RESET_ALL)


if __name__ == "__main__":
    main()
