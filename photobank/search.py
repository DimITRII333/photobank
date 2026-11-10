def search(photos, text=None, author=None, kind=None, min_price=None,
           max_price=None):
    result = []
    for p in photos:
        if text:
            t = text.lower()
            if t not in p.title.lower() and t not in [x.lower() for x in p.tags]:
                continue
        if author and p.author != author:
            continue
        if kind and p.kind != kind:
            continue
        if min_price is not None and p.get_price() < min_price:
            continue
        if max_price is not None and p.get_price() > max_price:
            continue
        result.append(p)
    return result


def statistics(photos):
    if len(photos) == 0:
        return {'count': 0, 'avg_price': 0, 'max_price': 0, 'downloads': 0}
    s = 0
    m = 0
    d = 0
    for p in photos:
        s += p.get_price()
        if p.get_price() > m:
            m = p.get_price()
        d += p.downloads
    return {'count': len(photos), 'avg_price': s / len(photos),
            'max_price': m, 'downloads': d}
