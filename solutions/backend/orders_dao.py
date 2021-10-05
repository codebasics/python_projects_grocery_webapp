from datetime import datetime
from sql_connection import get_sql_connection


def get_order_details(connection, order_id):
    cursor = connection.cursor()
    query = ("select orders.customer_name as customer, products.name as product, quantity, total_price "
             "from order_details "
             "inner join orders on order_details.order_id = orders.order_id "
             "inner join products on order_details.product_id = products.product_id "
             "where order_details.order_id = " + str(order_id))

    cursor.execute(query)

    response = []

    for (customer, product, quantity, total_price) in cursor:
        response.append({
            'customer': customer,
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        }

        )
    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_order_details(connection, 27))
