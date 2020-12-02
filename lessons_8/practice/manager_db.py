import sqlite3 as sql


class ManagerDb:

    def __init__(self):
        self.conn = sql.connect('shop_db')
        self.conn.row_factory = sql.Row

    def select_category(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM category")
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
        except Exception as ex:
            print(ex)

    def get_parent(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM category where id={id}")
            rows = cursor.fetchall() 
            return rows[0][1]
        except Exception as ex:
            print(ex) 