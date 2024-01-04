import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            # self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            print("Database connected.")
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

    def disconnect(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            print("Database disconnected.")

    def execute_query(self, query, params={}) -> list:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()


# class CustomRowFactory:
#     def __init__(self, cursor, row):
#         for idx, col in enumerate(cursor.description):
#             setattr(self, col[0], row[idx])

        
# def dict_factory(cursor, row):
#     """
#     Allows sqlite3 row data to be returned as a dictionary (per row)
#     (By default in sqlite3, rows are returned as tuples)
#     Usage:
#         conn.row_factory = dict_factory
#     """
#     fields = [column[0] for column in cursor.description]
#     return {key:value for key,value in zip(fields, row)}