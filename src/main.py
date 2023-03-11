from admin import AuthBot
from tg.language import LANGUAGE


def main() -> None:
    AuthBot().start()
    print(LANGUAGE)


if __name__ == "__main__":
    main()
