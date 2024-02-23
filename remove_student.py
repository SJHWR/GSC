
from db_connection import get_db_connection

def remove_student_info(sno):
    connection = get_db_connection()
    db_cursor = connection.cursor()
    try:   
        db_cursor.execute("SELECT * FROM sc WHERE sno = %s;", (sno,))
        enrollments = db_cursor.fetchall()
        if enrollments:
            db_cursor.execute("DELETE FROM sc WHERE sno = %s;", (sno,))
            connection.commit()
            print("Student's enrollment records successfully deleted.")
        db_cursor.execute("DELETE FROM student WHERE sno = %s;", (sno,))
        if db_cursor.rowcount > 0:
            connection.commit()
            print("Student information successfully deleted.")
        else:
            print("No student found to delete.")
    finally:
        db_cursor.close()
        connection.close()

if __name__ == "__main__":
    student_id = input("Enter sno to delete: ")
    remove_student_info(student_id)
