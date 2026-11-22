from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = """
        SELECT products.product_id, products.name, products.uom_id,
               products.price_per_unit, uom.uom_name
        FROM products
        INNER JOIN uom ON products.uom_id = uom.uom_id
    """
    cursor.execute(query)

    response = []
    for product_id, name, uom_id, price_per_unit, uom_name in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit,
            "uom_name": uom_name,
        })
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = """
        INSERT INTO products (name, uom_id, price_per_unit)
        VALUES (%s, %s, %s)
    """
    data = (product["product_name"], product["uom_id"], product["price_per_unit"])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def update_product(connection, product):
    query = """
        UPDATE products
        SET name = %s, uom_id = %s, price_per_unit = %s
        WHERE product_id = %s
    """
    values = (
        product["product_name"],
        product["uom_id"],
        product["price_per_unit"],
        product["product_id"],
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
        connection.commit()
    except Exception:
        connection.rollback()
        raise


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()

    return cursor.lastrowid


if __name__ == "__main__":
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        "product_name": "potatoes",
        "uom_id": "1",
        "price_per_unit": 10,
    }))