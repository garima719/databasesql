import sqlite3

conn = sqlite3.connect('company.db')

def create_data_model():
    conn.execute('''CREATE TABLE if not exists COMPANY
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME           VARCHAR(200)   NOT NULL,
         AGE            INT     NOT NULL,
         CITY        CHAR(150) NOT NULL,    
         ADDRESS        CHAR(500),
         SALARY         REAL,
         FOREIGN KEY (CITY) REFERENCES SPECIFIC_ADDRESS (CITY))''')

def create_specific_address_table():
    conn.execute('''CREATE TABLE if not exists SPECIFIC_ADDRESS
         (
         CITY       VARCHAR(200) NOT NULL PRIMARY KEY,
         STATE      VARCHAR(200))''')

    print("Table created successfully")
    print("Welcome to Garima DATABASE")
    print("")


def insert_new_emp():
    # id = input(" ID-Input a valid ID: ")
    name = input("Name - Input a valid Name: ")
    age = input("AGE - Input a valid AGE: ")
    city = input("City - Input a valid CITY: ")
    address = input("ADDRESS - Input a valid address: ")
    salary = input("SALARY - Input a valid SALARY: ")

    conn.execute("INSERT INTO COMPANY (NAME,AGE,CITY,SALARY,ADDRESS) \
      VALUES (?, ?, ?, ?,?)", (name, age, city, salary, address))

    conn.commit()
    print("Records created successfully")
    my_menu()


def insert_specific_address():
    # house_number = int(input("HOUSE_NUMBER - Enter House_number: "))
    # street = input("STREET - Enter Street: ")
    city = input("CITY - Enter City: ")
    state = input("STATE - Enter State: ")

    conn.execute("INSERT INTO SPECIFIC_ADDRESS ( CITY, STATE) \
    VALUES (?, ?)", ( city, state))
    conn.commit()

    my_menu()

def print_all_emp():
    # cursor = conn.execute("SELECT id, name, address,city, salary from COMPANY")
    cursor = conn.execute("SELECT COMPANY.id, COMPANY.name, "
                          "COMPANY.address, COMPANY.city, COMPANY.salary, SPECIFIC_ADDRESS.state "
                          "from COMPANY INNER JOIN SPECIFIC_ADDRESS ON COMPANY.CITY=SPECIFIC_ADDRESS.CITY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("City = ", row[3])
        print("State = ", row[5])
        print("Salary = ", row[4], "\n")

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
    print("Press 5 :  To Enter A New City And It's  Details")
    print("Press 6 : Exiting")


    menu_select = input(" Input a valid choice: ")
    # print("************* "+ menu_select)
    if menu_select == "1":
        insert_new_emp()
    elif menu_select == "2":
        print_search_by_name()
    elif menu_select == "3":
        print_all_emp()
    elif menu_select=="4":
        print_specific_partial()
    elif menu_select == "5":
        insert_specific_address()
    elif menu_select == "6":
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
    create_specific_address_table()
    my_menu()


main()
