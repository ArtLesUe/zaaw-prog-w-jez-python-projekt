import logging
import tornado.web
import time

from typing import Optional, Awaitable

from modules.prime_cache import check_prime_in_cache
from modules.prime_cache import save_prime_in_cache


class RestGetPrime(tornado.web.RequestHandler):
    """
    Klasa odpowiadająca za sprawdzanie, czy podana liczba jest liczbą pierwszą.
    """
    @staticmethod
    def fpf(n: int) -> bool:
        """
        Funkcja sprawdza z wysokim prawdopodobieństwem czy liczba jest pierwsza.

        :param n:int: liczba pierwsza do sprawdzenia
        :return: bool
        """
        if n & 1 == 0:
            return False
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d = d + 2
        return True

    @staticmethod
    def aks(num: int) -> bool:
        """
        Funkcja sprawdza z wysokim prawdopodobieństwem czy liczba jest pierwsza.

        :param num:int: liczba pierwsza do sprawdzenia
        :return: bool
        """
        if num == 2:
            return True
        if num == 3:
            return True
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= num:
            if num % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        """
        Obsługa zdarzenia przesłania danych do przeglądarki.

        :param chunk: wielkość przesłanej paczki danych
        :return: None
        """
        return None

    def get(self, slug) -> None:
        """
        Endpoint sprawdzający, czy podana liczba jest liczbą pierwszą.

        :param slug: liczba, która będzie sprawdzana pod kątem bycia liczbą pierwszą
        :return: None
        """
        logging.info("[HTTP GET] /prime/" + str(slug) + " 200")
        exec_time: float = time.time()

        number: int = int(slug)

        if number <= 1:
            self.send_error(422)
            return None

        if number > 9223372036854775807:
            self.send_error(422)
            return None

        cache_result: int = check_prime_in_cache(number)

        if cache_result != -1:
            if cache_result == 0:
                self.write({"result": "nie jest liczbą pierwszą", "number": str(number),
                            "exec": str((-exec_time + time.time()))})
                return None

            self.write({"result": "jest liczbą pierwszą", "number": str(number),
                        "exec": str((-exec_time + time.time()))})
            return None

        if len(str(abs(number))) <= 8 and not self.fpf(number):
            self.write({"result": "nie jest liczbą pierwszą", "number": str(number),
                        "exec": str((-exec_time + time.time()))})
            save_prime_in_cache(number, False)
            return None

        if len(str(abs(number))) > 8 and not self.aks(number):
            self.write({"result": "nie jest liczbą pierwszą", "number": str(number),
                        "exec": str((-exec_time + time.time()))})
            save_prime_in_cache(number, False)
            return None

        self.write({"result": "jest liczbą pierwszą", "number": str(number),
                    "exec": str((-exec_time + time.time()))})
        save_prime_in_cache(number, True)
        return None
