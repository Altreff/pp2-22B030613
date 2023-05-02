import psycopg2
from config import config


def get_phonebooklimoff(limit, offset):
    """ get parts provided by a phonebook specified by the limit and offset """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
        # another way to call a function
        # cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(vendor_id,))
        cur.callproc('get_data_offset_limit', (limit, offset))
        # process the result set
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    limit = int(input("Write your limit:"))
    offset = int(input("Write your offset:"))
    get_phonebooklimoff(limit, offset)