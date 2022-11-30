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


def save_prime_in_cache(number: int, result: bool) -> None:
    """
    Zapisuje w cache wynik przetwarzania liczby pierwszej do późniejszego użycia.

    :param number: int: liczba pierwsza, która była sprawdzana
    :param result: bool: wynik sprawdzania, czy liczba jest pierwszą
    :return: None
    """
    result_int: int = 1 if result else 0
    file = open("prime_cache/" + str(number), mode='w')
    file.write(str(result_int))
    file.close()
    return None
