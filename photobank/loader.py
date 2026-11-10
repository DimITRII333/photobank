import csv

from photobank.photo import Illustration, PremiumPhoto, StockPhoto


def load_photos(path):
    photos = []
    with open(path, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            common = (int(row['id']), row['title'], row['author'],
                      row['tags'].split(';'), row['date'],
                      float(row['size_mb']), int(row['downloads']),
                      int(row['base_price']))
            if row['kind'] == 'illustration':
                p = Illustration(*common, row['format'])
            elif row['kind'] == 'premium':
                p = PremiumPhoto(*common, int(row['width']),
                                 int(row['height']), row['license'])
            else:
                p = StockPhoto(*common, int(row['width']),
                               int(row['height']))
            photos.append(p)
    return photos
