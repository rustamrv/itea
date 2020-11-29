from manager_db import ManagerDb


if __name__ == "__main__":
    mn = ManagerDb()
    # mn.create_table('faculty', 'id integer primary key, name text')
    # mn.create_table('grooup', 'id integer primary key, name text, faculty_id INTEGER NOT NULL, FOREIGN KEY ('
    #                           'faculty_id) REFERENCES grooup(id)')
    # mn.create_table('student',
    #                 'id integer primary key, first_name text, last_name text, number_card text, '
    #                 'group_id INTEGER NOT NULL, '
    #                 'FOREIGN KEY (group_id) REFERENCES student(id)')
    #
    # mn.create_table('subject',
    #                 'id integer primary key, name text, group_id INTEGER NOT NULL, '
    #                 'FOREIGN KEY (group_id) REFERENCES subject(id)')
    # mn.create_table('rate_list',
    #                 'id integer primary key, raite text, rating integer, student_id INTEGER NOT NULL, '
    #                 'subject_id INTEGER NOT NULL, '
    #                 'FOREIGN KEY (student_id) REFERENCES student_card(id)'
    #                 'FOREIGN KEY (subject_id) REFERENCES student_card(id)')
    print("ok")