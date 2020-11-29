import sqlite3 as sql


class ManagerDb:

    def __init__(self):
        self.conn = sql.connect('mydb.db')

    def create_faculty(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE faculty(id integer primary key, name text)""")
            self.conn.commit()
        except Exception as ex:
            print(ex)

    def create_group(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE grooup(id integer primary key, name text, faculty_id INTEGER NOT NULL, 
                            FOREIGN KEY (faculty_id) REFERENCES faculty(id))""")
            self.conn.commit()
        except Exception as ex:
            print(ex)

    def create_student(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE student(id integer primary key, first_name text, last_name text, 
            number_card text, group_id INTEGER NOT NULL, FOREIGN KEY(group_id) REFERENCES grooup(id))""")
            self.conn.commit()
        except Exception as ex:
            print(ex)

    def create_subject(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE subject(id integer primary key, name text, group_id INTEGER NOT NULL,
                    FOREIGN KEY (group_id) REFERENCES grooup(id) )""")
            self.conn.commit()
        except Exception as ex:
            print(ex)

    def create_rate_list(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE rate_list(id integer primary key, rate integer, student_id INTEGER NOT NULL, subject_id INTEGER NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES student(id)
                    FOREIGN KEY (subject_id) REFERENCES subject(id) )""")
            self.conn.commit()
        except Exception as ex:
            print(ex)


class User(ManagerDb):

    def __init__(self, name, is_admin):
        super().__init__()
        self.name = name
        self.is_admin = is_admin

    def create_tables(self):
        if self.is_admin:
            self.create_faculty()
            self.create_group()
            self.create_student()
            self.create_subject()
            self.create_rate_list()
        else:
            print(f'user {self.name} not admin')

    def add_faculties(self, faculties):
        if self.is_admin:
            cursor = self.conn.cursor()
            for i in faculties:
                cursor.execute(f"""insert into faculty(name) VALUES ('{i}')""")
                self.conn.commit()
            print("successful add faculties")
        else:
            print(f'user {self.name} not admin')

    def add_group(self, groups):
        if self.is_admin:
            cursor = self.conn.cursor()
            cursor.executemany("""insert into grooup(name, faculty_id) VALUES (?, ?)""", groups)
            self.conn.commit()
            print("successful add group")
        else:
            print(f'user {self.name} not admin')

    def add_student(self, students):
        if self.is_admin:
            cursor = self.conn.cursor()
            cursor.executemany("""insert into student(first_name, last_name, number_card, group_id) 
                                VALUES (?, ?, ?, ?)""", students)
            self.conn.commit()
            print("successful add students")
        else:
            print(f'user {self.name} not admin')

    def add_subject(self, subjects):
        if self.is_admin:
            cursor = self.conn.cursor()
            cursor.executemany("""insert into subject(name, group_id) 
                                VALUES (?, ?)""", subjects)
            self.conn.commit()
            print("successful add subjects")
        else:
            print(f'user {self.name} not admin')

    def add_rate_list(self, rate_lists):
        if self.is_admin:
            cursor = self.conn.cursor()
            cursor.executemany("""insert into rate_list(rate, student_id, subject_id) 
                                VALUES (?, ?, ?)""", rate_lists)
            self.conn.commit()
            print("successful add rate list")
        else:
            print(f'user {self.name} not admin')

    def get_excellent(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT student.first_name, student.last_name FROM rate_list "
                           "INNER JOIN student "
                           " ON student.id = rate_list.student_id "
                           "where rate_list.rate =5")
            rows = cursor.fetchall()
            for row in rows:
                print(*row)
        except Exception as ex:
            print(ex)

    def update_student(self, number, first_name, last_name):
        if self.is_admin:
            try:
                cursor = self.conn.cursor()
                if first_name:
                    cursor.execute("UPDATE student"
                                   f" SET first_name = '{first_name}'" 
                                   f" WHERE number_card = '{number}'")
                    self.conn.commit()
                if last_name:
                    cursor.execute("UPDATE student"
                                   f" SET last_name = '{last_name}'"
                                   f" WHERE number_card = '{number}'")
                    self.conn.commit()
                print('update')
            except Exception as ex:
                print(ex, 'ff')

    def get_students(self, number):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT student.first_name, student.last_name, student.number_card, "
                           "grooup.name, faculty.name FROM student "
                           "INNER JOIN grooup "
                           "ON grooup.id = student.group_id "
                           "INNER JOIN faculty ON faculty.id = grooup.faculty_id"
                           f" where student.number_card='{number}'")
            rows = cursor.fetchall()
            for row in rows:
                print(*row)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    mn = User('tolya', False)
    faculties = ['FIOT', 'Mathematical', 'Physics']

    mn.add_faculties(faculties)
    mn = User('tolya', True)
    mn.create_tables()

    # mn.add_faculties(faculties)
    # groups = [('G1', '1'), ('G2', '1'), ('G3', '2'), ('G4', '2'), ('G5', '3')]
    # mn.add_group(groups)
    # students = [('Николай', "Петровыч", "1-programing", "1"),
    #             ('Василий', "Иванов", "2-mathematics", "2"),
    #             ('Иван', "Петров", "3-mathematics", "3")]
    # mn.add_student(students)
    # subjects = [('python language', '1'), ('c++ language', '1'),
    #             ('higher mathematics', '2'),
    #             ('chemistry', '3'),
    #             ('physics', '3')]
    # mn.add_subject(subjects)
    #
    # rate_list = [('4', '1', '1'), ('4', '1', '2'), ('4', '1', '3'),
    #              ('5', '2', '1'), ('4', '2', '2'), ('5', '2', '3'),
    #              ('5', '3', '1'), ('3', '3', '2'),  ('5', '3', '3')]
    # mn.add_rate_list(rate_list)

    mn.get_excellent()
    mn.update_student('3-mathematics', 'John', 'Doe')
    mn.get_students('3-mathematics')
