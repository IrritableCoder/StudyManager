import mysql.connector
from datetime import date

# CONNECT TO MYSQL
mydatabase = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

# SET UP CURSOR
mycursor = mydatabase.cursor()

print('study analyst open\n')

while True:

    use_db = input("Use study analyst - use (u) or exit (e): ")

    # EXIT STUDY ANALYST
    if use_db.lower() == 'e':
        print('study analyst closed')
        print('bye')
        break

    # USE STUDY ANALYST

    # TABLE COMMANDS
    use_data = input(
        "Add data (ad)\nSee total lesson time (tlt)\nSee all table data (atd)\nCreate table (ct)\nDelete a table (dt)\nDelete table row (dtr)\nENTER: ")

    # ADD DATA TO TABLE
    if use_data.lower() == 'ad':
        print('add data open\n')
        lesson_date = date.today()
        student_name = input("Add name: ")
        lesson_title = input("Add lesson title: ")
        lesson_duration = float(input("Add lesson duration: "))
        table_name = input(
            "Add the name of the table you want to save your data to: ")
        sql = "INSERT INTO "+table_name + \
            " (date, student_name, lesson_title, lesson_duration) VALUES (%s, %s, %s, %s)"
        vals = (lesson_date, student_name, lesson_title, lesson_duration)
        mycursor.execute(sql, vals)
        mydatabase.commit()
        print(f"data saved to table: {table_name}")

    # SHOW SUMMED DATA
    elif use_data.lower() == 'tlt':
        print('show data open\n')
        imp_data__from = input(
            "Add the name of the table whose data you would like to see: ")
        imp_data_where = input(
            "Add which date's data you would like to see (2010-10-10): ")
        mycursor.execute(
            "SELECT SUM(lesson_duration) FROM "+imp_data__from+" WHERE date = '"+imp_data_where+"'")
        sum_data = mycursor.fetchall()

        print(f"total time spent of lessons today {imp_data_where}")
        for data in sum_data:
            print(data[0])

    # SHOW ALL DATA IN A TABLE
    elif use_data.lower() == 'atd':
        print('show all data open\n')
        all_data_from = input(
            "Add the name of the table you would like to open: ")
        mycursor.execute("SELECT * FROM "+all_data_from+"")
        table_data = mycursor.fetchall()

        for row in table_data:
            print(row)

    # CREATE TABLE
    elif use_data.lower() == 'ct':
        print('create table open\n')
        create_table_name = input("Add a name for your table: ")
        mycursor.execute(
            "CREATE TABLE "+create_table_name+" (date DATE NOT NULL, student_name VARCHAR(50) NOT NULL, lesson_title VARCHAR(100) NOT NULL, lesson_duration DECIMAL(4,2) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
        print(f"table {create_table_name} created")

    # DELETE TABLE
    elif use_data.lower() == 'dt':
        print('delete table open\n')
        delete_table_name = input("Which table would you like delete: ")
        table_to_delete = "DROP TABLE "+delete_table_name+""
        mycursor.execute(table_to_delete)
        print(f"table {delete_table_name} deleted")

    # DELETE A ROW IN THE TABLE
    elif use_data.lower() == 'dtr':
        print('delete table row open\n')

        delete_row_in_table = input(
            "Which table would you like to delete a row from: ")
        delete_row_name = input(
            "Which table row would you like delete - provide row id: ")
        row_to_delete = "DELETE FROM "+delete_row_in_table + \
            "WHERE id = '"+delete_row_name+"'"
        mycursor.execute(row_to_delete)
        mydatabase.commit()

        mycursor.execute("SELECT * FROM "+delete_row_in_table+"")
        changed_data = mycursor.fetchall()

        for row in changed_data:
            print(row)
