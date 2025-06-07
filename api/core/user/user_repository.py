import sqlite3
from core.user.user import User

class UserRepository:
    def __init__(self, db_path='dbReceitas.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()
    
    def save(self, user: User):
        # Se usuário já existe (email), atualiza; senão insere
        cursor = self.conn.cursor()
        existent = self.search_by_email(user.email)
        if existent:
            sql = """
            UPDATE users SET name=?, password=? WHERE email=?
            """
            cursor.execute(sql, (user.name, user.password, user.email))
        else:
            sql = """
            INSERT INTO users (name, email, password) VALUES (?, ?, ?)
            """
            cursor.execute(sql, (user.name, user.email, user.password))
        self.conn.commit()
        return user

    def search_by_email(self, email):
        query = 'SELECT * FROM users WHERE email = ?'
        cursor = self.conn.execute(query, (email,))
        row = cursor.fetchone()
        return User(**row) if row else None

    def list_all(self):
        query = 'SELECT * FROM users'
        cursor = self.conn.execute(query)
        return [User(**row) for row in cursor.fetchall()]

    def remove_by_email(self, email):
        query = 'DELETE FROM users WHERE email = ?'
        self.conn.execute(query, (email,))
        self.conn.commit()

    def remove_by_id(self, id):
        query = 'DELETE FROM users WHERE id = ?'
        self.conn.execute(query, (id,))
        self.conn.commit()

    def get_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return Usuarios(
                name=row["name"],
                email=row["email"],
                password=row["password"]
            )
        else:
            return None