import logging

import tornado.web

from typing import Optional, Awaitable


class RestGetRoot(tornado.web.RequestHandler):
    """
    Główna klasa odpowiadająca za główny endpoint aplikacji z informacją powitalną.
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
        Wyświetlenie informacji powitalnej na endpoint GET /.

        :return: None
        """
        logging.info("[HTTP GET] / 200")

        self.write({
            "przedmiot": "Zaawansowane programowanie w języku Python",
            "kierunek": "Informatyka",
            "semestr": 3,
            "rok": "2022 / 2023",
            "tryb": "niestacjonarne",
            "autor": "Artur Leśnik"
        })

        return None
