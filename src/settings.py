import pandas as pd

def setConst():
    init = {
        'url': 'https://www.backcountry.com/womens-clothing-best-sellers',
        # 'url': 'https://www.backcountry.com/mens-clothing-best-sellers'
        # 'url': 'https://www.backcountry.com/kids-best-sellers'
        'limit': 1,
        'folder': 'backcountry',
        'csv_name': 'backcountry.csv'
    }

    return init

def setStructure():
    item = {
        'name': '',
        'product': '',
        'upc': '',
        'img_name': '',
        'price': '',
        'color': '',
        'size': '',
        'stock': '',
        'description':'',
        'Material':''
    }

    return item

def setPandas():
    col = [
        'name',
        'product',
        'upc',
        'img_name',
        'price',
        'color',
        'size',
        'stock',
        'description',
        'Material'
    ]

    return pd.DataFrame(index=[], columns=col)
