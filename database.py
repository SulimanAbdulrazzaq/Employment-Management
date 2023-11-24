import sqlite3



def create_table():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    
    
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    role TEXT,
                    gender TEXT,
                    status TEXT)""")
    conn.commit()
    conn.close()
    
def fetch():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    empss = cursor.fetchall()
    conn.close()
    return empss


def insert(id,name,role,gender,status):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO employees (id,name,role,gender,status) VALUES(?,?,?,?,?)",
                                                                            (id,name,role,gender,status))
    conn.commit()
    conn.close()
def delete(id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    
    
def update(nname,nrole,ngender,nstatus,id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE employees SET name= ?,role = ?,gender=?,status=? WHERE id=?",
                (nname,nrole,ngender,nstatus,id))
    conn.commit()
    conn.close()
    
    
    
def id_exist(id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT (*) FROM employees WHERE id=?",(id,))
    result = cursor.fetchone()
    conn.close()
    return result[0]>0


create_table()