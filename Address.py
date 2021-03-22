import sqlite3

conn = sqlite3.connect('company.db')


def create_data_model():
    conn.execute('''CREATE TABLE if not exists COMPANY
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME           VARCHAR(200)   NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(500),
         SALARY         REAL)''');
    print("Table created successfully")
    print("Welcome to Garima DATABASE")
    print("")


def insert_new_emp():
    id = input(" ID-Input a valid ID: ")
    name = input("Name - Input a valid Name: ")
    age = input("AGE - Input a valid AGE: ")
    address = input("ADDRESS - Input a valid ADDRESS: ")
    salary = input("SALARY - Input a valid SALARY: ")

    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES (?, ?, ?, ?)", (name, age, address, salary))
    conn.commit()
    print("Records created successfully")
    my_menu()


def print_all_emp():
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    my_menu()


def print_search_by_name():
    the_name = input("Please enter the name of the employee that you want to search for?")
    statement = "SELECT * from COMPANY where NAME=?"
    cursor = conn.execute(statement, (the_name))
    # print(cursor)
    for row in cursor.fetchall():
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    my_menu()

def print_specific_partial():
    the_name = input("Please enter the name of the employee that you want to search for?")
    statement = "SELECT * from COMPANY where NAME like ?"
    cursor = conn.execute(statement, ('%'+the_name+'%',))
    # print(cursor)
    for row in cursor.fetchall():
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    my_menu()

def my_menu():
    print("Hello!, Press the number as per your need")
    print("Press 1 : For adding new employee")
    print("Press 2 : For searching employee from your database")
    print("Press 3 : For printing the details of all employees")
    print("Press 4 : For searching employee from your database like")
    print("Press 5 : Exiting")


    menu_select = input(" Input a valid choice: ")
    # print("************* "+ menu_select)
    if menu_select == "1":
        insert_new_emp()
    elif menu_select == "2":
        print_specific()
    elif menu_select == "3":
        print_all_emp()
    elif menu_select=="4":
        print_specific_partial()
    elif menu_select == "5":
        exit()
    else:
        print("Please select a valid choice")
        # conn.close()
        my_menu()


# create_data_model()
# insert_new_emp()

def main():
    # print("Initializing the setup..")
    print("")
    create_data_model()
    my_menu()

main()
