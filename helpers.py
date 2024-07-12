"""
Вспомогательные функции для тестов
"""
import random
import string


def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def get_pages_list():
    return ['', 'en-gb/catalog/mp3-players', 'en-gb/catalog/cameras',
            'en-gb/catalog/smartphone', 'en-gb/catalog/software',
            'en-gb/catalog/tablet', 'en-gb/catalog/component',
            'en-gb/catalog/laptop-notebook', 'en-gb/catalog/desktops']


def random_email():
    return (random_string() + "@" + random_string(3)
            + "." + random.choice(["com", "pro", "org", "ru"]))
