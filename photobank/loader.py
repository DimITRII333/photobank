import csv

from photobank.factory import PhotoFactory


def load_photos(path):
    factory = PhotoFactory()
    with open(path, encoding='utf-8') as f:
        return [factory.create(row) for row in csv.DictReader(f)]
