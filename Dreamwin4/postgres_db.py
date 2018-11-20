import psycopg2
from logging_py import logger as log

# connect to database
conn = psycopg2.connect(database='student', host='localhost', user='postgres',
                       password='welcome', port=5432)
log.info('db connection established')

#with psycopg2.connect(database='student', host='localhost', user='postgres',
#                        password='welcome', port=5432) as conn:
# create cursor object
log.info('creating cursor object')
cursor = conn.cursor()


def create_table(cursor, conn):
    cursor.execute('create table stddetails (name varchar(30), age int, std int, \
               section varchar(5), school_name varchar(50))')

    conn.commit()

def get_data():
    pass

def insert_data(cursor, conn):
    data = get_data()
    cursor.execute("insert into stddetails values ('ashok', 12, 7, 'A', 'Oxford School')")
    conn.commit()


def fetch_data(cursor):
    log.info('fetching student data')
    cursor.execute("select * from stddetails where name='ashok'")
    data = cursor.fetchall()
    print(data)


if __name__ == '__main__':
    #create_table(cursor, conn)
    #insert_data(cursor, conn)
    fetch_data(cursor)




