from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@1234",
    database="database_connective"
)

def insert(name, age, city):
    res = con.cursor()
    sql = "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)"
    user = (name, age, city)
    res.execute(sql, user)
    con.commit()
    print("Data inserted successfully!")

def update(name, age, city, id):
    res = con.cursor()
    sql = "UPDATE users SET name=%s, age=%s, city=%s WHERE id=%s"
    user = (name, age, city, id)
    res.execute(sql, user)
    con.commit()
    print("Data updated successfully!")

def select():
    res = con.cursor()
    sql = "SELECT * FROM users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))

def delete(id):
    res = con.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data deleted successfully!")

def quit():
    con.close()
    print("Connection closed. Exiting...")
    exit()

while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Exit")
    choice = int(input("Enter Your choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        city = input("Enter the city: ")
        insert(name, age, city)
    elif choice == 2:
        id = input("Enter the id: ")
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        city = input("Enter the city: ")
        update(name, age, city, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter the id to delete: ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid choice, please try again!")
