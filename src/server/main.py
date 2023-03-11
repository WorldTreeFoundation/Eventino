import uvicorn

# from admin import AuthBot


def main() -> None:
    # AuthBot().start()
    uvicorn.run(
        "app.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
