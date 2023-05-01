import psycopg2
from config import config


def insert_data(username, phone):
    """ insert a new data into the phonebook table """
    insertdata = "INSERT INTO phonebook(username,phone) VALUES(%s,%s)"
    conn = None
 
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(insertdata, (username,phone))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    name = str(input("Write the name:"))
    phone = int(input("Write phone number(without +7)"))
    insert_data(name,phone)