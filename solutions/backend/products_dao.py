from sql_connection import get_sql_connection


def edit_product(connection, product):
    cursor = connection.cursor()
    query = ("UPDATE products "
             "set name=%s, uom_id=%s, price_per_unit=%s"
             " WHERE product_id=%s;")
    data = (product['name'], product['uom_id'], product['price_per_unit'], product['product_id'])

    cursor.execute(query, data)
    connection.commit()

    return product['product_id']


if __name__ == '__main__':
    connection = get_sql_connection()
    
    print(edit_product(connection, {
        'product_id': 1,
        'name': 'potatoes',
        'uom_id': 1,
        'price_per_unit': 10
    }))
