import sqlite3
import os

#
# Mission Database
#
MIS_TABLE_NAME = "mission_table"
MIS_Headers    = ["id", "type", "parameter", "status", "create_time"]
MIS_FILENAME   = os.path.join(os.path.dirname(__file__), "missionDB.sdb")


class SqliteModule:

    def __init__(self, file_name, table_name, headers):

        self.file_name  = file_name
        self.table_name = table_name
        self.headers    = headers
        self.db         = self.connect()

    def connect(self):

        exist = os.path.exists(self.file_name)
        db = sqlite3.connect(self.file_name)
        if not exist:
            cursor = db.cursor()
            temp_headers = self.headers.copy()  # copy headers because it will be change initial headers
            cursor.execute('''CREATE TABLE {} ( {} TEXT )'''.format(self.table_name, temp_headers.pop(0)))
            if temp_headers:
                for temp in temp_headers:
                    cursor.execute('''ALTER TABLE {} ADD COLUMN {} TEXT'''.format(self.table_name, temp))
            db.commit()
        return db

    def add_content(self, content, status, time):

        content_headers = MIS_Headers[:3]
        content_values = tuple([content[h] for h in content_headers] + [status, time])
        cursor = self.db.cursor()
        cursor.execute('''INSERT INTO {} {} VALUES {}'''.format(self.table_name, tuple(self.headers), content_values))
        self.db.commit()

    def update_content(self, cur_field, cur_status, cur_id, cur_time):

        cursor = self.db.cursor()
        cursor.execute('''UPDATE {} SET "{}" = "{}" WHERE id = "{}" AND create_time = "{}"'''
                       .format(self.table_name, cur_field, cur_status, cur_id, cur_time))
        self.db.commit()

    def get_headers(self):

        cursor = self.db.cursor()
        cmd = cursor.execute("select * from {}".format(self.table_name))
        headers = [description[0] for description in cmd.description]
        return headers

    def select_u_want(self, want_item, need_key, need_value):  # mis_db.select_u_want('parameter', 'id', '1')

        cursor = self.db.cursor()
        if type(want_item) == str:
            temp = cursor.execute(
                "select {} from {} where {} = '{}'".format(want_item, self.table_name, need_key, need_value))
            value = [i[0] for i in temp]
            return value[0]  # return one content
        elif type(want_item) == list:
            temp_array = dict()
            for item in want_item:
                temp = cursor.execute(
                    "select {} from {} where {} = '{}'".format(item, self.table_name, need_key, need_value))
                value = [i[0] for i in temp]
                temp_array[item] = value[0]
            return temp_array  # return dict content
        else:
            print('Input args error')

    def truncate(self):
        cursor = self.db.cursor()
        cursor.execute("delete from {}".format(self.table_name))
        self.db.commit()

    def quit(self):
        if self.db:
            self.db.close()
