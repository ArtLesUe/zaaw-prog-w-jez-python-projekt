import logging
import tornado.web

from typing import Optional, Awaitable


class RestPostPictureInvert(tornado.web.RequestHandler):
    """
    Klasa odpowiadająca za endpoint zwracający inwersję przesłanego obrazka.
    """
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        """
        Obsługa zdarzenia przesłania danych do przeglądarki.

        :param chunk: wielkość przesłanej paczki danych
        :return: None
        """
        return None

    def post(self) -> None:
        """
        Zwrócenie przesłanego obrazu po wykonaniu na nim polecenia inwersji kolorów.

        :return: None
        """
        logging.info("[HTTP GET] / 200")
        self.write({})
        return None
