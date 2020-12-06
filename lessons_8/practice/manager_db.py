import sqlite3 as sql
from sqlite3 import ProgrammingError, OperationalError


class ContextManager:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sql.connect(self.db_name)
        self.conn.row_factory = sql.Row
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


class ManagerDb(ContextManager):

    def __init__(self, db_name):
        super().__init__(db_name)

    def create_category(self):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""CREATE TABLE category(id integer primary key AUTOINCREMENT, name text, parent_id INTEGER NULL,
                        FOREIGN KEY (parent_id) REFERENCES category(id) )""")
                conn.commit()
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def create_product(self):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""CREATE TABLE products(id integer primary key AUTOINCREMENT, name text,
                            price REAL, count integer null,
                            discription text,
                            category_id INTEGER not NULL,
                            FOREIGN KEY (category_id) REFERENCES category(id) )""")
                conn.commit()
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def select_category(self):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM category ORDER BY CASE WHEN parent_id IS NULL "
                               "THEN id ELSE parent_id END, COALESCE(parent_id, '') DESC")
                rows = cursor.fetchall()
                data = list()
                for i in rows:
                    res = dict()
                    res['id'] = i['id']
                    res['name'] = i['name']
                    if i['parent_id']:
                        res['parent'] = self.get_parent(i['parent_id'])
                    else:
                        res['parent'] = None
                    data.append(res)

                return data
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def select_category_products(self, id):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM products  where category_id = {id}")
                rows = cursor.fetchall()
                return rows, self.get_parent(id)
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def select_detail_product(self, id):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM products  where id = {id}")
                rows = cursor.fetchall()
                return rows
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def get_category(self):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM category")
                rows = cursor.fetchall()
                return rows
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def get_parent(self, id):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM category where id={id}")
                rows = cursor.fetchall()
                return rows[0][1]
            except OperationalError as ex:
                print(ex)
            except ProgrammingError as ex:
                print(ex)

    def add_category(self, name, parent_id):
        if name:
            with ContextManager(self.db_name) as conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("""insert into category(name, parent_id) VALUES(?, ?)""", (name, parent_id))
                    conn.commit()
                except ProgrammingError as ex:
                    print(ex)
                except OperationalError as ex:
                    print(ex)

    def add_product(self, *args):
        with ContextManager(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""insert into products(name, price, count, discription, category_id) VALUES(?,?,?, ?,
                                ?)""", args)
                conn.commit()
            except ProgrammingError as ex:
                print(ex)
            except OperationalError as ex:
                print(ex)