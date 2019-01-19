import pandas as pd

def setConst():
    init = {
        'url': 'https://www.backcountry.com/womens-clothing-best-sellers',
        # 'url': 'https://www.backcountry.com/mens-clothing-best-sellers'
        # 'url': 'https://www.backcountry.com/kids-best-sellers'
        'limit': 3,
        'img_folder': 'backcountry_img'
    }

    return init

def setStructure():
    item = {
        'name': '',
        'product':'',
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
        'img_name',
        'price',
        'color',
        'size',
        'stock',
        'description',
        'Material'
    ]

    return pd.DataFrame(index=[], columns=col)
