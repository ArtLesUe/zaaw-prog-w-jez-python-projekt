import logging
import tornado.web
import tornado.process
import tornado.ioloop

from dotenv import load_dotenv
from tornado.httpserver import TCPServer

from modules.prime_cache import create_cache
from modules.image_cache import create_cache as create_cache_img

from endpoint.rest_get_root import RestGetRoot
from endpoint.rest_get_prime import RestGetPrime
from endpoint.rest_post_picture_invert import RestPostPictureInvert
from endpoint.rest_get_time import RestGetTime


def make_app():
    return tornado.web.Application(
        [
            (r"/", RestGetRoot),
            (r"/prime/([0-9]+)", RestGetPrime),
            (r"/picture/invert", RestPostPictureInvert),
            (r"/time", RestGetTime)
        ],
        debug=False
    )


def main():
    server = tornado.httpserver.HTTPServer(make_app())
    server.bind(8888)
    server.start(0)
    logging.Logger.setLevel(logging.getLogger(), logging.INFO)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    load_dotenv()
    create_cache()
    create_cache_img()
    main()
