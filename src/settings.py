import pandas as pd

def setConst():
    init = {
        'url': 'https://www.backcountry.com/womens-clothing-best-sellers',
        'single_url': 'https://www.backcountry.com/womens-clothing-best-sellers',
        # 'url': 'https://www.backcountry.com/mens-clothing-best-sellers'
        # 'url': 'https://www.backcountry.com/kids-best-sellers'
        'limit': 300,
        'folder': 'backcountry',
        'csv_name': 'backcountry.csv',
        'weight': 300,
        'highweight': 500,
        'image_path': 'http://kai8217.xsrv.jp/backcountry_img/',
        'limit_img_sub': 8
    }

    return init

def setStructure():
    item = {
        'name': '',
        'brand': '',
        'product': '',
        'upc': '',
        'img_name': '',
        'img_main': '',
        'img_sub': '',
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
        'product_id_type': '',
        'recommended_browse_nodes': '2131480051',
        'condition': 'new',
        'update_delete': 'Update',
        'url': '',
        'variation_theme': 'SizeColor',
        'relationship_type': '',
        'parent_sku': '',
        'fulfillment_latency': '14',
        'merchant_shipping_group_name': 'テスト',
        'condition_type': '新品',
        'bullet_point1': '',
        'bullet_point2': '当商品は、アメリカの正規店からの並行輸入品となっていますので到着まで2-3週間お時間いただいております。',
        'bullet_point3': '当店では完全正規品のみしか取り扱っておりませんのでご安心してご購入ください。',
        'bullet_point4': '万が一不良品や、返品を希望される場合は当社規定のポリシーがありますので当社ページのヘルプから事前にご確認下さい。',
        'bullet_point5': '在庫は常に変動しているため、ご注文が重なった時など在庫が確保できていない場合もございますので何卒ご了承ください。'
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
