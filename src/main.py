from admin import AuthBot
from logger import run_logger


def main() -> None:
    AuthBot().start()
    run_logger()


if __name__ == "__main__":
    main()
