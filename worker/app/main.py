from pixelize import pixelize


def main() -> None:
    """Entrypoint"""

    def inner(image: None):
        pixelize(image=image)


if __name__ == "__main__":
    main()
