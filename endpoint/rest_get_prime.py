import logging
import tornado.web
import time

from typing import Optional, Awaitable


class RestGetPrime(tornado.web.RequestHandler):
    """
    Klasa odpowiadająca za sprawdzanie, czy podana liczba jest liczbą pierwszą.
    """
    def aks(self, num: int) -> bool:
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
        logging.info("[HTTP GET] /prime/<number> 200")
        exec_time: float = time.time()

        number: int = int(slug)

        if number <= 1:
            self.send_error(422)
            return None

        if number > 9223372036854775807:
            self.send_error(422)
            return None

        if not self.aks(number):
            self.write({"result": "nie jest liczbą pierwszą", "number": str(number),
                        "exec": str((-exec_time + time.time()))})
            return None

        self.write({"result": "jest liczbą pierwszą", "number": str(number),
                    "exec": str((-exec_time + time.time()))})
        return None
