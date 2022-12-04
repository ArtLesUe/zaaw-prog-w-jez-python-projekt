import os
import random

from locust import HttpUser, task, between
from dotenv import load_dotenv


load_dotenv()


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def http_get_root(self):
        self.client.get("/", name="GET /")

    @task
    def http_get_time(self):
        self.client.get("/time", auth=(os.getenv('API_AUTH_USER'), os.getenv('API_AUTH_PASS')), name="GET /time")

    @task
    def http_post_image_invert(self):
        attach = open('tests/test-image.jpg', 'rb')
        self.client.post("/picture/invert", data={}, files={'obraz': attach.read()}, name="GET /picture/invert")
        attach.close()

    @task
    def http_get_prime(self):
        self.client.get("/prime/" + str(random.randint(0, 9223372036854775807)), name="GET /prime/[number]")
