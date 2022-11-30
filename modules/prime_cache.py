import os


def create_cache() -> None:
    """
    Funkcja tworzy katalog potrzebny do cache liczb pierwszych.

    :return: None
    """
    if not os.path.exists("prime_cache"):
        os.makedirs("prime_cache")
    return None


def check_prime_in_cache(number: int) -> int:
    """
    Funkcja sprawdza, czy odpowiedź na liczbę pierwszą znajduje się w cache aplikacji.

    :param number: int: liczba do sprawdzenia, czy jest pierwsza
    :return: int (-1: brak w cache, 0: nie jest pierwsza, 1: liczba jest pierwsza)
    """
    if os.path.exists("prime_cache/" + str(number)):
        file = open("prime_cache/" + str(number), mode='r')
        content = file.read()
        file.close()
        return int(content)
    return -1
