import io
import logging
import tornado.web
import PIL.Image as Image
import PIL.ImageChops as ImageChops

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
        logging.info("[HTTP POST] /picture/invert 200")
        self.set_header("Content-type", "image/jpeg")
        image = Image.open(io.BytesIO(self.request.files['obraz'][0]['body']))
        image.convert("RGB")
        image_inv = ImageChops.invert(image)
        image_data = io.BytesIO()
        image_inv.save(image_data, format='jpeg')
        self.write(image_data.getvalue())
        return None
