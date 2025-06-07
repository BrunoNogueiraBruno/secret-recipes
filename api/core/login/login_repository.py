import sqlite3
from core.user.user import User  

class LoginRepository:
    def __init__(self, db_path='dbReceitas.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def search_user_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            return User(row["name"], row["email"], row["password"])
        return None