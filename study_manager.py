import mysql.connector
from datetime import date
from findnshow import fns

# CONNECT TO MYSQL
mydatabase = mysql.connector.connect(
    host="LOCALHOST",
    user="USERNAME",
    password="PASSWORD",
    database="DATABASE"
)

# SET UP CURSOR
mycursor = mydatabase.cursor()

print('\nstudy manager working\n')

# CHOOSE WHICH TABLE YOU WOULD LIKE TO WORK IN
t_list = fns()

work_table = str(input(
    "Which table would you like to work in?\nEnter a name: ") or t_list[0]).strip()

# MAIN MENU
while True:

    # STUDY MANAGER COMMANDS
    use_data = input(
        "\nAdd data (ad)\nSee total lesson time (tlt)\nSee all table data (atd)\nCreate table (ct)\nDelete a table (dt)\nDelete table row (dtr)\nMove to new table (mnt)\nExit (e)\nENTER: ")

    # EXIT STUDY MANAGER
    if use_data.lower().strip() == 'e':
        print("\nstudy manager closed\n")
        break

    # ADD DATA TO A TABLE
    if use_data.lower().strip() == 'ad':
        print('\nadd data open\n')

        while True:

            # DATA INTAKE
            lesson_date = date.today()
            student_name = input("Add student name: ").strip()
            lesson_title = input("Add lesson title: ").strip()
            lesson_duration = float(input("Add lesson duration: "))

            # ADD DATA TO TABLE
            values_to_table = "INSERT INTO "+work_table + \
                " (date, student_name, lesson_title, lesson_duration) VALUES (%s, %s, %s, %s)"
            values = (lesson_date, student_name, lesson_title, lesson_duration)
            mycursor.execute(values_to_table, values)
            mydatabase.commit()

            print(f"data saved to table: {work_table}")

            # BACK
            back = input(
                "\nBack to main menu (b) or continue (c):\n")
            if back.lower().strip() == 'b':
                print("\nadd data closed\n")
                break

    # CALCULATE TIME SPENT ON STUDIES FOR A CERTAIN DATA
    elif use_data.lower().strip() == 'tlt':
        print('\nsun total study time open\n')

        while True:

            # FIND AND SHOW DATA
            calculate_data_where = str(input(
                "Add which date's (YYYY-MM-DD) data you would like to see: ") or date.today()).strip()

            # SUM LESSON LENGTH
            mycursor.execute(
                "SELECT SUM(lesson_duration) FROM "+work_table+" WHERE date = '"+calculate_data_where+"'")
            sumed_data = mycursor.fetchall()

            print(f"Total time spent on lessons on {calculate_data_where}:")
            for lesson in sumed_data:
                print(lesson[0])

            # BACK
            back = input(
                "\nBack to main menu (b) or continue (c):\n")
            if back.lower().strip() == 'b':
                print("\ntotal study time closed\n")
                break

    # SHOW ALL DATA IN A TABLE
    elif use_data.lower().strip() == 'atd':
        print('\nshow all data open\n')

        # SHOW All DATA
        mycursor.execute("SELECT * FROM "+work_table+"")
        table_data = mycursor.fetchall()

        print(f"Now displaying all rows in {work_table}: ")
        for row in table_data:
            print("\nshow all data closed\n")
            print(row)

    # CREATE TABLE IN DATABASE
    elif use_data.lower() == 'ct':
        print('\ncreate table open\n')

        while True:

            # INPUT DATA TO CREATE A TABLE
            create_table_name = input("Add a name for your table: ").strip()

            # CREATE TABLE
            mycursor.execute(
                "CREATE TABLE "+create_table_name+" (date DATE NOT NULL, student_name VARCHAR(50) NOT NULL, lesson_title VARCHAR(100) NOT NULL, lesson_duration DECIMAL(4,2) NOT NULL, id INT PRIMARY KEY NOT NULL AUTO_INCREMENT)")

            print(f"table {create_table_name} created")

            # BACK
            back = input("\nBack to main menu (b) or continue (c):\n")
            if back.lower().strip() == 'b':
                print("\ncreate table closed\n")
                break

   # DELETE TABLE IN DATABASE
    elif use_data.lower().strip() == 'dt':
        print('\ndelete table open\n')

        while True:

            # SHOW TABLES
            fns()

            # INPUT DATA TO DELETE A TABLE
            delete_table_name = input(
                "Which table would you like delete: ").strip()

            # DELETE TABLE
            table_to_delete = "DROP TABLE "+delete_table_name+""
            mycursor.execute(table_to_delete)

            print(f"table {delete_table_name} deleted")

            # BACK
            back = input("\nBack to main menu (b) or continue (c):\n")
            if back.lower().strip() == 'b':
                print("\ndelete table closed\n")
                break

    # DELETE ROW IN TABLE
    elif use_data.lower().strip() == 'dtr':
        print('\ndelete table row open\n')

        while True:

            # SHOW TABLE ROWS (ORIGINAL)
            mycursor.execute("SELECT * FROM "+work_table+"")
            changed_data = mycursor.fetchall()

            for row in changed_data:
                print(row)

            # INPUT DATA TO DELETE ROWS IN A TABLE
            delete_row_name = input(
                "Which table row would you like delete, provide a row id: ").strip()

            # DELETE ROW
            row_to_delete = "DELETE FROM "+work_table+" WHERE id = '"+delete_row_name+"'"
            mycursor.execute(row_to_delete)
            mydatabase.commit()

            print("\nRow(s) successfully deleted\n")

            # SHOW TABLE ROWS (MODIFIED)
            mycursor.execute("SELECT * FROM "+work_table+"")
            changed_data = mycursor.fetchall()

            for row in changed_data:
                print(row)

            # BACK
            back = input(
                "\nBack to main menu (b) or continue (c):\n")
            if back.lower().strip() == 'b':
                print("\ndelete table rows closed\n")
                break

    # CHANGE WHICH TABLE YOU ARE WORKING IN
    elif use_data.lower().strip() == 'mnt':
        print('\nmove to new table table open\n')

        while True:

            # SHOW TABLES
            fns()

            # INPUT DATA TO DELETE A TABLE
            work_table = input(
                "Which table would you like work in: ").strip()

            # REPORT SUCCESS
            print(f"you are now working in {work_table}")

            # BACK
            back = input("\nBack to main menu (b) or continue (c):\n")
            if back.lower().strip() == 'b':
                print("\nmove to new table table closed\n")
                break
