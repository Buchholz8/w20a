import dbcreds
import mariadb

def all_posts():
    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    cursor.execute('select_post')
    results = cursor.fetchall()
    cursor.close()
    conn.close()

all_posts()
