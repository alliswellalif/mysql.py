import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:d
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error: '{err}'")

create_orders_table = """
create table orders(
  order_id int primary key,
  customer_name varchar(30) not null,
  product_name varchar(20) not null,
  date_ordered date,
  quantity int,
  unit_price float,
  phone_number varchar(20)
);
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
execute_query(connection, create_orders_table)

# %%
data_orders = """
INSERT INTO orders VALUES
(101, 'Steve', 'Laptop', '2018-06-12', 2, 800, '6293730802'),
(102, 'Jos', 'Books', '2019-02-10', 10, 12, '8367489124'),
(103, 'Stacy', 'Trousers', '2019-12-25', 5, 50, '8976123645'),
(104, 'Nancy', 'T-Shirts', '2018-07-14', 7, 30, '7368145099'),
(105, 'Maria', 'Headphones', '2019-05-30', 6, 48, '8865316698'),
(106, 'Danny', 'Smart TV', '2018-08-20', 10, 300, '7720130449');
"""

# %%
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
# %%
import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = "SELECT * FROM orders;"

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q1)

for result in results:
    print(result)
    
# %%
q2 = """
select customer_name, phone_number from orders;
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q2)

for result in results:
    print(result)

# %%
q3 = """
select year(date_ordered) from orders;
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q3)

for result in results:
    print(result)
# %%
q4 = """
select distinct year(date_ordered) from orders;
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q4)

for result in results:
    print(result)
# %%
q5 = """
select * from orders where date_ordered < '2018-12-31';
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q5)

for result in results:
    print(result)
# %%
q6 = """
select * from orders where date_ordered > '2018-12-31';
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q6)

for result in results:
    print(result)
# %%
q7 = """
select * from orders order by unit_price;
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q7)

for result in results:
    print(result)
# %%
execute_query(connection, data_orders)

q7 = """
select * from orders order by unit_price;
"""

results = read_query(connection, q7)

for result in results:
    print(result)







# %%
import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")

data_orders = """
INSERT INTO orders VALUES
(101, 'Steve', 'Laptop', '2018-06-12', 2, 800.0, '6293730802'),
(102, 'Jos', 'Books', '2019-02-10', 10, 12.0, '8367489124'),
(103, 'Stacy', 'Trousers', '2019-12-25', 5, 50.0, '8976123645'),
(104, 'Nancy', 'T-Shirts', '2018-07-14', 7, 30.0, '7368145099'),
(105, 'Maria', 'Headphones', '2019-05-30', 6, 48.0, '8865316698'),
(106, 'Danny', 'Smart TV', '2018-08-20', 10, 300.0, '7720130449');
"""
execute_query(connection, data_orders)

q7 = """
select * from orders order by unit_price;
"""

results = read_query(connection, q7)

if results:
    for result in results:
        print(result)
# %%
import pandas as pd

from_db = []

for result in results:
    result = list(result)
    from_db.append(result)

columns = ["order_id", "customer_name", "product_name", "date_ordered", "quantity", "unit_price", "phone_number"]

df = pd.DataFrame(from_db, columns=columns)

display(df)

# %%
# Update command for order_id 104
update = """
update orders
set unit_price = 45
where order_id = 104
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
execute_query(connection, update)

# %%
q8 = """
select * from orders where order_id = 103;
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q8)

for result in results:
    print(result) 
    # %%
    q9 = """
select * from orders;
"""

connection = create_db_connection("localhost", "root", "Alifthereal07!", "mysql_python")
results = read_query(connection, q9)

for result in results:
      print(result)