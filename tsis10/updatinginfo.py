import psycopg2
from config import config


def update_phonebook(id, username, phone, chphone, chname):
    """ update vendor name based on the vendor id """
    chnames = """ UPDATE phonebook
                SET username = %s
                WHERE id = %s"""
    chphones = """ UPDATE phonebook
                SET phone = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        if chname == True:
            cur.execute(chnames, (username, id))
        if chphone == True:
            cur.execute(chphones, (phone, id))
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    chname = bool(int(input("Change name?[0/1]:")))
    if chname == True:
        name = str(input("Write new name:"))
    else:
        name = "Null"
    chphone = bool(int(input("Change phone?[0/1]:")))
    if chphone == True:
        phone = int(input("Write new phone:"))
    else:
        phone = int(0)
    id = int(input("Write id:"))
    update_phonebook(id, name, phone, chphone, chname)