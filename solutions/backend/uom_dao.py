from sql_connection import get_sql_connection
connection = get_sql_connection()


def insert_new_uom(connection, uom):
    cursor = connection.cursor()
    query = f"INSERT INTO uom (uom_name) VALUES ('{uom['name']}');"
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
       
    print(insert_new_uom(connection, {
        'name': 'cubic meter'
    }))
