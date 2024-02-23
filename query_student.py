# query_student.py
from db_connection import get_db_connection

def query_student_info(sno):
    connection = get_db_connection()
    db_cursor = connection.cursor()
    try:
        db_cursor.execute("SELECT * FROM student WHERE sno = %s;", (sno,))
        student_info = db_cursor.fetchone()
        if student_info:
            print(student_info)
        else:
            print("Student not found with the given sno.")
    finally:
        db_cursor.close()
        connection.close()

if __name__ == "__main__":
    student_id = input("Enter sno: ")
    query_student_info(student_id)
