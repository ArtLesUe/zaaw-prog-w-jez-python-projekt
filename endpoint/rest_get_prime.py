import logging
import tornado.web

from typing import Optional, Awaitable


class RestGetPrime(tornado.web.RequestHandler):
    """
    Klasa odpowiadająca za sprawdzanie, czy podana liczba jest liczbą pierwszą.
    """
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

        self.write(slug);
