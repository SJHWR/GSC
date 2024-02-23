
from db_connection import get_db_connection

def add_student_info(sno, student_name, student_age, student_gender, dept_name):
    connection = get_db_connection()
    db_cursor = connection.cursor()
    try:
        db_cursor.execute("SELECT * FROM student WHERE sno = %s;", (sno,))
        if db_cursor.fetchone():
            print("This sno already exists. Please use a different sno.")
        else:
            db_cursor.execute("INSERT INTO student (sno, sname, sage, sgender, sdept) VALUES (%s, %s, %s, %s, %s);",
                              (sno, student_name, student_age, student_gender, dept_name))
            connection.commit()
            print("Student information successfully added.")
    finally:
        db_cursor.close()
        connection.close()

if __name__ == "__main__":
    student_info = input("Enter student info (sno, sname, sage, sgender, sdept) separated by comma: ").split(',')
    add_student_info(*student_info)
