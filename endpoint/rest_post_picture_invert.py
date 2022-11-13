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

    def get(self) -> None:
        """
        Zwrócenie prostego formularza do przesyłania obrazów do endpoint.

        :return: None
        """
        logging.info("[HTTP GET] / 200")
        self.write("<html>" +
                   "<form method='post' enctype='multipart/form-data'>" +
                   "<input name='obraz' type='file' accept='*.jpg' />" +
                   "<br/>" +
                   "<br/>" +
                   "<input type='submit' />" +
                   "</form>" +
                   "</html>")
        return None

    def post(self) -> None:
        """
        Zwrócenie przesłanego obrazu po wykonaniu na nim polecenia inwersji kolorów.

        :return: None
        """
        logging.info("[HTTP POST] / 200")
        self.set_header("Content-type", self.request.files['obraz'][0]['content_type'])
        self.write(self.request.files['obraz'][0]['body'])
        return None
