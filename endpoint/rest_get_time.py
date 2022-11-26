import os
import logging
import tornado.web

from typing import Optional, Awaitable
from datetime import datetime

API_AUTH_USER = os.getenv('API_AUTH_USER')
API_AUTH_PASS = os.getenv('API_AUTH_PASS')


class RestGetTime(tornado.web.RequestHandler):
    """
    Klasa odpowiadająca za endpoint zwracający aktualną godzinę po zalogowaniu.
    """
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        """
        Obsługa zdarzenia przesłania danych do przeglądarki.

        :param chunk: wielkość przesłanej paczki danych
        :return: None
        """
        return None

    def get(self) -> None:
        """
        Zwrócenie aktualnej godziny zalogowanemu użytkownikowi.

        :return: None
        """
        logging.info("[HTTP GET] /time 200")
        self.write({"time": datetime.now().strftime("%H:%M:%S")})
        return None
