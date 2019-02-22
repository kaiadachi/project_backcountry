import pandas as pd

def setConst():
    init = {
        'url': 'https://www.backcountry.com/womens-clothing-best-sellers',
        # 'url': 'https://www.backcountry.com/mens-clothing-best-sellers'
        # 'url': 'https://www.backcountry.com/kids-best-sellers'
        'limit': 2,
        'folder': 'backcountry',
        'csv_name': 'backcountry.csv',
        'weight': 275
    }

    return init

def setStructure():
    item = {
        'name': '',
        'brand': '',
        'product': '',
        'upc': '',
        'img_name': '',
        'price': '',
        'color': '',
        'size': '',
        'stock': '',
        'department_name': 'レディーズ',
        'en_description': '',
        'description': '',
        'Material':'',
        'parent_child': '',
        'distribution': 'JP Parallel Import',
        'feed_product_type': 'outerwear',
        'product_id_type': 'UPC',
        'recommended_browse_nodes': '2131480051',
        'condition': 'new',
        'update_delete': 'Update',
        'url': '',
        'variation_theme': 'SizeColor',
        'relationship_type': '',
        'parent_sku': '',
        'fulfillment_latency': '14',
        'merchant_shipping_group_name': 'テスト'
    }

    return item

# def setPandas():
    # col = [
    #     'name',
    #     'brand',
    #     'product',
    #     'upc',
    #     'img_name',
    #     'price',
    #     'color',
    #     'size',
    #     'stock',
    #     'department_name',
    #     'description',
    #     'Material',
    #     'parent_child',
    #     'distribution',
    #     'feed_product_type',
    #     'product_id_type',
    #     'recommended_browse_nodes',
    #     'condition',
    #     'update_delete',
    #     'url'
    # ]
