from emp_db import (
    connect_db, create_employee_table, insert_employee,
    fetch_employees, update_employee, delete_employee, close_db, setup_logger
)

def main():
    setup_logger('applog.txt')  # logs go to applog.txt
    conn = connect_db()
    if conn:
        create_employee_table(conn)
        insert_employee(conn, 'Ram', 27, 'IT')
        fetch_employees(conn)
        update_employee(conn, 1, age=30)
        fetch_employees(conn)
        delete_employee(conn, 1)
        fetch_employees(conn)
        close_db(conn)

if __name__ == "__main__":
    main()
