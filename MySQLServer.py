import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL Server (adjust user and password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # Replace with your MySQL root password
    )

    cursor = connection.cursor()

    # Attempt to create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():

import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL Server (adjust user and password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bidoh100%"  
    )

    cursor = connection.cursor()

    # Attempt to create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
