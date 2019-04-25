from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint


def calculate_total_per_invoices(products_string):
    products = transform_products_to_list(products_string)
    customer_dict = {}
    for product in products:
        invoice_id = product[0] #key
        customer_id = product[-2] #main key
        price = float(product [-3])
        quantity = float(product [3])
        total_price = round(price * quantity, 3)
        
        customer_dict.setdefault(customer_id, {}) #if customer id x exists, create empty list
        customer_dict[customer_id].setdefault(invoice_id, 0)
        customer_dict[customer_id][invoice_id] += total_price
    return customer_dict
    #pprint (products)
pprint (calculate_total_per_invoices(products_string))

"""
{
    customer_id: {
        invoice_id:total_price
        
    }

}
"""
