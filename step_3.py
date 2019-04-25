from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint


def group_products_by_customer_and_invoice(products_string):
    products = transform_products_to_list(products_string)
    customer_dict = {}
    for product in products:
        invoice_id = product[0] #key
        customer_id = product[-2]
        customer_dict.setdefault(customer_id, {}) #if customer id x exists, create empty list
        customer_dict[customer_id].setdefault(invoice_id, [])
        customer_dict[customer_id][invoice_id].append(product)
    return customer_dict

#pprint (group_products_by_customer_and_invoice(products_string))
"""
{
    customer_id: {
        invoice_id:[
            []
        ]
    }

}


"""
