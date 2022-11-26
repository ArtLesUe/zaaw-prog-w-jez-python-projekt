import os
import logging
import tornado.web
import base64

from typing import Optional, Awaitable
from datetime import datetime


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

        auth_data: str = self.request.headers.get("Authorization")

        if auth_data is None or (auth_data is not None and "Basic " not in auth_data):
            self.set_status(401)
            self.set_header("WWW-Authenticate", "Basic realm=\"Restricted\"")
            self.finish()
            return None

        api_auth_user = os.getenv('API_AUTH_USER')
        api_auth_pass = os.getenv('API_AUTH_PASS')

        auth_string: str = api_auth_user + ":" + api_auth_pass
        auth_bytes: bytes = auth_string.encode("ascii")
        base64_bytes: bytes = base64.b64encode(auth_bytes)
        base64_string: str = base64_bytes.decode("ascii")
        auth_data: str = auth_data.split(" ")[1]

        if auth_data != base64_string:
            self.set_status(401)
            self.set_header("WWW-Authenticate", "Basic realm=\"Restricted\"")
            self.finish()
            return None

        self.write({"time": datetime.now().strftime("%H:%M:%S")})
        return None
