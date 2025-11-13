import sqlite3
import logging

def setup_logger(log_filename='applog.txt'):
    logging.basicConfig(
        filename=log_filename,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def connect_db(db_name='employee.db'):
    try:
        conn = sqlite3.connect(db_name)
        logging.info("Database connected successfully.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect database: {e}")

def create_employee_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                department TEXT
            )
        ''')
        conn.commit()
        logging.info("Employee table created successfully.")
    except Exception as e:
        logging.error(f"Failed to create table: {e}")

def insert_employee(conn, name, age, department):
    try:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO employees (name, age, department) VALUES (?, ?, ?)',
            (name, age, department)
        )
        conn.commit()
        logging.info(f"Inserted employee: {name}, {age}, {department}")
    except Exception as e:
        logging.error(f"Failed to insert employee ({name}): {e}")

def fetch_employees(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employees')
        rows = cursor.fetchall()
        logging.info("Fetched employees list.")
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        logging.error(f"Failed to fetch employees: {e}")

def update_employee(conn, emp_id, name=None, age=None, department=None):
    try:
        cursor = conn.cursor()
        fields = []
        values = []
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if age is not None:
            fields.append("age = ?")
            values.append(age)
        if department is not None:
            fields.append("department = ?")
            values.append(department)
        if not fields:
            logging.warning("No fields to update, skipping update.")
            return
        values.append(emp_id)
        sql = f"UPDATE employees SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(sql, values)
        conn.commit()
        logging.info(f"Updated employee id={emp_id}, fields: {fields}")
    except Exception as e:
        logging.error(f"Failed to update employee ID {emp_id}: {e}")

def delete_employee(conn, emp_id):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
        conn.commit()
        logging.info(f"Deleted employee with id={emp_id}")
    except Exception as e:
        logging.error(f"Failed to delete employee {emp_id}: {e}")

def close_db(conn):
    try:
        conn.close()
        logging.info("Database connection closed.")
    except Exception as e:
        logging.error(f"Failed to close database: {e}")
