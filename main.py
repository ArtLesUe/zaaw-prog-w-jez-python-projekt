import asyncio
import logging

import tornado.web

from endpoint.rest_get_root import RestGetRoot


def make_app():
    return tornado.web.Application(
        [
            (r"/", RestGetRoot),
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
