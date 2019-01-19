import pandas as pd

def setConst():
    init = {
        'url': 'https://www.backcountry.com/womens-clothing-best-sellers',
        # 'url': 'https://www.backcountry.com/mens-clothing-best-sellers'
        # 'url': 'https://www.backcountry.com/kids-best-sellers'
        'limit': 3
    }

    return init

def setStructure():
    item = {
        'name': '',
        'product':'',
        'price': '',
        'color': '',
        'size': '',
        'stock': ''
    }

    return item

def setPandas():
    col = [
        'name',
        'product',
        'price',
        'color',
        'size',
        'stock'
    ]

    return pd.DataFrame(index=[], columns=col)
