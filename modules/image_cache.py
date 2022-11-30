import os


def create_cache() -> None:
    """
    Funkcja tworzy katalog potrzebny do cache obrazów.

    :return: None
    """
    if not os.path.exists("image_cache"):
        os.makedirs("image_cache")
    return None


def check_image_in_cache(md5: str) -> bytes:
    """
    Funkcja sprawdza, czy posiadamy już taki przetworzony obraz.

    :param md5: str: identyfikator md5 obrazu do sprawdzenia w cache
    :return: bytes (0: brak w cache, zawartość obrazu do zwrócenia)
    """
    if os.path.exists("image_cache/" + md5):
        file = open("image_cache/" + md5, mode='rb')
        content: bytes = file.read()
        file.close()
        return content
    return bytes(0)


def save_image_in_cache(md5: str, result: bytes) -> None:
    """
    Zapisuje w cache wynik przetwarzania obrazu do późniejszego użycia.

    :param md5: str: identyfikator md5 oryginalnego obrazu do cache
    :param result: bytes: przetworzony obraz do zapisania w cache
    :return: None
    """
    file = open("image_cache/" + md5, mode='wb')
    file.write(result)
    file.close()
    return None
