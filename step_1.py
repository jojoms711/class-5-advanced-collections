from data import products_string
def transform_products_to_list(products_string):
    splitted =  (products_string.split('\n'))
    product_list = []
    for item in splitted:
        if item:
            clean_item = item.split(',')
            product_list.append(clean_item)
    return product_list
transform_products_to_list(products_string)


