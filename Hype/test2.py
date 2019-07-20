import psycopg2
import sys

def select_all(table_name, order_id):
    try:
        connection = psycopg2.connect("dbname='bama_prj' user='postgres' password='51136616' host='localhost' port='5433'")
        cursor = connection.cursor()
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')

    sql = ''' 
    SELECT *
    FROM %s ORDER BY %s
    ''' %(table_name, order_id)
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    print(rows)

select_all('main_carinfo', 'car_id')