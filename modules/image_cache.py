import os


def create_cache() -> None:
    """
    Funkcja tworzy katalog potrzebny do cache obrazów.

    :return: None
    """
    if not os.path.exists("image_cache"):
        os.makedirs("image_cache")
    return None




