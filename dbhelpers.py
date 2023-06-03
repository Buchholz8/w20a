#i imported mariadb and my dbcreds.py
import mariadb
import dbcreds
#i used your function here but i added a few more excepts one for programming to check for sql related error
#and one for opertaion to test for errors in the data base
def run_procedures(sql, args):
    results = None
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.IntegrityError:
        print("Sorry, what you entered doesn't exist")
    except mariadb.OperationalError:
        print('there is an error in the data base')
    except mariadb.ProgrammingError:
        print('Error in the sql syntax or query execution')
    except Exception as error:
        print('Error:', error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return results