from admin import AdminAuth


def main() -> None:
    AdminAuth().ensure_server_has_admin()


if __name__ == "__main__":
    main()
