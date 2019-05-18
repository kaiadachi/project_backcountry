import pandas as pd
from src.settings import *
from src.utility import *

# from settings import *
# from utility import *

def convertAmazon():
    init = setConst()

    main_df = pd.read_csv('{0}/{1}'.format(init['folder'] + '_csv', 'replaced_' + init['csv_name']), encoding="Shift_jis", dtype = 'object')
    main_df = main_df.fillna(' ')

    header_df = pd.read_csv('template/temple.csv', encoding='Shift_jis', header=2)
    skip_df = pd.read_csv('template/temple.csv', encoding='Shift_jis', names=header_df.columns)

    header_df['feed_product_type'] = main_df['feed_product_type']
    header_df['item_sku'] = main_df['product']
    header_df['brand_name'] = main_df['brand']
    header_df['item_name'] = main_df['name'] + ' ' + main_df['color'] + ' ' + main_df['size']
    header_df['external_product_id'] = main_df['upc']
    header_df['external_product_id_type'] = main_df['product_id_type']
    header_df['outer_material_type'] = main_df['Material']
    header_df['recommended_browse_nodes'] = main_df['recommended_browse_nodes']
    header_df['size_name'] = main_df['size']
    header_df['department_name'] = main_df['department_name']
    header_df['size_map'] = main_df['size']
    header_df['color_name'] = main_df['color']
    header_df['color_map'] = main_df['color']
    header_df['quantity'] = main_df['stock']
    header_df['standard_price'] = main_df['price']
    header_df['parent_child'] = main_df['parent_child']
    header_df['update_delete'] = main_df['update_delete']
    header_df['relationship_type'] = main_df['relationship_type']
    header_df['variation_theme'] = main_df['variation_theme']
    header_df['parent_sku'] = main_df['parent_sku']
    header_df['fulfillment_latency'] = main_df['fulfillment_latency']
    header_df['bullet_point2'] = main_df['bullet_point2']
    header_df['bullet_point3'] = main_df['bullet_point3']
    header_df['bullet_point4'] = main_df['bullet_point4']
    header_df['bullet_point5'] = main_df['bullet_point5']

    header_df['condition_type'] = main_df['condition_type']
    header_df['distribution_designation'] = main_df['distribution']
    header_df['merchant_shipping_group_name'] = main_df['merchant_shipping_group_name']
    header_df['main_image_url'] = init['image_path'] + main_df['img_name']

    try:
        for i in range(1, init['limit_img_sub']):
            header_df['other_image_url{0}'.format(i)] = main_df['img_sub_{0}'.format(i)]
    except:
        pass

    result_df = pd.concat([skip_df, header_df])
    createCsv(result_df, '{0}_csv'.format(init['folder']), '{0}_amazon.txt'.format(init['folder']), False, '\t')
    createCsv(result_df, '{0}_csv'.format(init['folder']), '{0}_amazon.csv'.format(init['folder']), False, ',')

if __name__ == '__main__':
    convertAmazon()
