
from db_connection import get_db_connection

def modify_student_info(sno, new_name, new_age, new_gender, new_dept):
    connection = get_db_connection()
    db_cursor = connection.cursor()
    try:
        db_cursor.execute("SELECT * FROM student WHERE sno = %s;", (sno,))
        if db_cursor.fetchone():
            db_cursor.execute("UPDATE student SET sname=%s, sage=%s, sgender=%s, sdept=%s WHERE sno = %s;",
                              (new_name, new_age, new_gender, new_dept, sno))
            connection.commit()
            print("Student information successfully updated.")
        else:
            print("No student found with the given sno.")
    finally:
        db_cursor.close()
        connection.close()

if __name__ == "__main__":
    student_id = input("Enter sno: ")
    new_info = input("Enter new student info (sname, sage, sgender, sdept) separated by comma: ").split(',')
    modify_student_info(student_id, *new_info)
