import sqlite3


class Student:
    def __init__(self, id, name, gender, birthday, student_id, grade, clas):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.student_id = student_id
        self.grade = grade
        self.clas = clas

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_birthday(self):
        return self.birthday

    def get_student_id(self):
        return self.student_id

    def get_grade(self):
        return self.grade

    def get_clas(self):
        return self.clas

class Monitor:
    def __init__(self, id, addr, physical_location, type):
        self.id = id
        self.addr = addr
        self.physical_location = physical_location
        self.type = type

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()

    def create_monitorsDB(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS monitors 
                            (
                                id integer PRIMARY KEY AUTOINCREMENT, 
                                addr text, 
                                physical_location text,
                                type text
                            )
                        """)
        self.conn.commit()

    def monitor_entry(self, monitor):
        self.cur.execute("""INSERT INTO monitors VALUES (?,?,?,?)""", (
        monitor.id, monitor.addr, monitor.physical_location, monitor.type))
        self.conn.commit()

    def monitor_read_byID(self, id):
        self.cur.execute('SELECT * FROM monitors WHERE id = ?', (id,))
        for row in self.cur.fetchall():
            print(row)
        self.conn.commit()

    def monitor_readAll(self):
        self.cur.execute('SELECT * FROM monitors')
        monitors = self.cur.fetchall()
        self.conn.commit()
        return monitors

    def monitor_remove_byID(self, id):
        self.cur.execute('DELETE FROM monitors WHERE id = ?', (id,))
        self.conn.commit()

    def monitor_clearAll(self):
        self.cur.execute('DELETE FROM monitors')
        self.conn.commit()

    def create_studentsDB(self):
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS Students
                (
                    id integer PRIMARY KEY AUTOINCREMENT, 
                    name varchar(20),
                    gender varchar(2),
                    birthday date,
                    student_id varchar(20),
                    grade varchar(10),
                    class varchar(10)
                )
            """)
        self.conn.commit()

    '''
    def execute(self, sql):
        result = self.cur.execute(*sql)
        self.conn.commit()
        return result

    def query(self, sql):
        return self.cur.execute(*sql)
    '''

    def clean(self):
        self.cur.close()
        self.conn.close()

    def student_entry(self, student):
        self.cur.execute("""INSERT INTO Students VALUES (?,?,?,?,?,?,?)""", (
        student.id, student.name, student.gender, student.birthday, student.student_id, student.grade, student.clas))
        self.conn.commit()

    def student_read_byID(self, id):
        self.cur.execute('SELECT * FROM Students WHERE id = ?', (id,))
        for row in self.cur.fetchall():
            print(row)
        self.conn.commit()

    def student_readAll(self):
        self.cur.execute('SELECT * FROM Students')
        for row in self.cur.fetchall():
            print(row)
        self.conn.commit()

    def student_remove_byID(self, id):
        self.cur.execute('DELETE FROM Students WHERE id = ?', (id,))
        self.conn.commit()

    def student_clearAll(self):
        self.cur.execute('DELETE FROM Students')
        self.conn.commit()


root = Database()
'''
if __name__ == '__main__':
    root.execute((
        r"""
            CREATE TABLE IF NOT EXISTS students
            (
                id integer, 
                name varchar(20),
                gender varchar(2),
                birthday date,
                student_id varchar(20),
                grade varchar(10),
                class varchar(10)
            );
        """,))

    root.execute((
        r"""
            CREATE UNIQUE INDEX students_id_uindex ON `students` (id);
        """,))

root.create_studentsDB()
root.student_remove_byID(1)
root.student_clearAll()
student1 = Student(None, 'b', 'aa', 2018, 1, 1, 1)
root.student_entry(student1)
root.student_read_byID(2)
root.student_readAll()

root.create_monitorsDB()
monitor1 = Monitor(None, 'abc', 'abc', 'abc')
root.monitor_readAll()
'''
print(root.monitor_readAll())
root.clean()