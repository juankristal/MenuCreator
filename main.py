import sys

from Exceptions.TooManyParametersException import TooManyParametersException
from MenuJSONLoader import MenuJSONLoader
from models.Menu import Menu


def main():
    if len(sys.argv) > 2:
        raise TooManyParametersException("Expected to run with a single parameter or none. Run with `python3 "
                                         "menu.json` as the only parameter to load menu from JSON")
    menu = Menu()

    if sys.argv:
        menu = MenuJSONLoader().parse(sys.argv[1])

    while True:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("owo")
