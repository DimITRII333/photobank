import csv

from photobank.photo import Photo


def load_photos(path):
    photos = []
    with open(path, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['kind'] == 'illustration':
                p = Photo(int(row['id']), row['kind'], row['title'],
                          row['author'], row['tags'].split(';'), row['date'],
                          float(row['size_mb']), int(row['downloads']),
                          int(row['base_price']), fmt=row['format'])
            else:
                p = Photo(int(row['id']), row['kind'], row['title'],
                          row['author'], row['tags'].split(';'), row['date'],
                          float(row['size_mb']), int(row['downloads']),
                          int(row['base_price']), int(row['width']),
                          int(row['height']), row['license'])
            photos.append(p)
    return photos
