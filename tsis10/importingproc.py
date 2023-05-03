import psycopg2
from config import config
def add_part(name, phone_num):
    conn = None    
    try:
        params = config()      
        conn = psycopg2.connect(**params)      
        cur = conn.cursor()
        cur.execute('CALL inserting_data(%s, %s)', (name, phone_num))   
        conn.commit()
        cur.close()    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        if conn is not None:            
            conn.close()

if __name__ == '__main__':
    name = str(input("Write name:"))
    phone_num = int(input("Write number:"))
    add_part(name, phone_num)