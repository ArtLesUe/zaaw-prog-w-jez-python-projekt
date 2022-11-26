import asyncio
import logging

import tornado.web

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


async def main():
    app = make_app()
    app.listen(8888)
    logging.Logger.setLevel(logging.getLogger(), logging.INFO)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
