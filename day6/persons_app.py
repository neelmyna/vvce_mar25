import pymysql

def connect_db():
    connection = pymysql.Connect(host='localhost', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
    print('DB connected')
    return connection

def disconnect_db(connection):
    connection.close()
    print('DB dis-connected')

def run_query(query, object=None, operation=None):
    connection = connect_db()
    cursor = connection.cursor()
    count = cursor.execute(query, object)
    if count == 0:
        print(f'Row {operation} did not happen')
    else:
        print(f'Row {operation} successful')
    if operation == 'search':
        result_set = cursor.fetchone()
    connection.commit()
    cursor.close()
    disconnect_db(connection)
    return result_set

def create_db():
    query = 'create database IF NOT EXISTS nithin_db'
    run_query(query)

def create_table():
    query = 'create table employees(id int primary key auto_increment, name varchar(40) not null, designation varchar(30), phone_number bigint unique, salary float, commission float default(0))'
    run_query(query, operation = 'table creation')

def read_person_details():
    name = input('Enter the person name: ')
    gender = input('Enter the person gender: ')
    location = input('Enter the person location: ')
    return (name, gender, location)

def insert_person():
    person = read_person_details()
    query = 'insert into persons(name, gender, location) values(%s, %s, %s);'
    run_query(query, person, operation = 'insertion')

def delete_person():
    id = int(input('Enter id of the person to delete the row: '))
    query = f'delete from persons where id = {id}'
    run_query(query, operation = 'deletion')

def update_person():
    id = int(input('Enter id of the person to update the row: '))
    location = input('Enter new location of the person: ')
    query = f'update persons set location = %s where id = %s'
    connection = connect_db()
    cursor = connection.cursor()
    count = cursor.execute(query, (location, id))
    if count == 0:
        print(f'Row update did not happen')
    else:
        print(f'Row update successful')
    connection.commit()
    cursor.close()
    disconnect_db(connection)

def search_row():
    id = int(input('Enter id of the person to search: '))
    query = f'select * from persons where id = {id}'
    person = run_query(query, operation='search')
    if person is None:
        print(f'Person with id {id} not found')
    else:
        print('Row details are \n ', str(person))

search_row()