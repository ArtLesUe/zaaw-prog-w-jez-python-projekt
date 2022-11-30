import os


def create_cache():
    if not os.path.exists("prime_cache"):
        os.makedirs("prime_cache")
