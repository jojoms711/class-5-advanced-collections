from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint

def group_products_by_customer(products_string):
    products = transform_products_to_list(products_string)
    customer_dict = {}
    for product in products:
        customer_id = product[-2] #key
        customer_dict.setdefault(customer_id, []) #if customerid x exists, create empty list
        customer_dict[customer_id].append(product)
    return customer_dict

pprint(group_products_by_customer(products_string))
