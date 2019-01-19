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
        'number':'',
        'price':'',
        'color':[],
        'size':[],
        'stock':[]
    }

    return item
