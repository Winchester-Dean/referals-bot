import logging
import sqlite3

logging.basicConfig(level=logging.INFO)

class DataBase:
    def __init__(self):
        self.directory = "./database.db"
        self.connect = sqlite3.connect(self.directory)
        self.cursor = self.connect.cursor()

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    referer INTEGER,
                    balance INTEGER DEFAULT 0
                )
            """)
        
        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS channels(
                    id INTEGER PRIMARY KEY,
                    chid INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    link TEXT NOT NULL
                )
            """)
    
    def add_user(
        self,
        user_id: int,
        name: str,
        referer: int = None
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO users(user_id, name, referer) "
                "VALUES(?, ?, ?)",
                [user_id, name, referer]
            )
    
    def add_channel(
        self,
        chid: int,
        name: str,
        link: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO channels(chid, name, link) "
                "VALUES(?, ?, ?)",
                [chid, name, link]
            )

    def get_users(self):
        self.cursor.execute(
            "SELECT user_id, name, balance FROM users"
        )
        return self.cursor.fetchall()
    
    def get_users_id(self):
        self.cursor.execute(
            "SELECT user_id FROM users"
        )
        return self.cursor.fetchall()
    
    def get_balance(
        self,
        user_id: int
    ):
        self.cursor.execute(
            "SELECT balance FROM users "
            "WHERE user_id=?",
            [user_id]
        )
        return self.cursor.fetchone()
    
    def get_referals_count(
        self,
        user_id: int
    ):
        self.cursor.execute(
            "SELECT COUNT(*) FROM users "
            "WHERE referer=?",
            [user_id]
        )
        return self.cursor.fetchone()
    
    def get_channels(self):
        self.cursor.execute(
            "SELECT name, link FROM channels"
        )
        return self.cursor.fetchall()
    
    def get_channels_id(self):
        self.cursor.execute(
            "SELECT chid FROM channels"
        )
        return self.cursor.fetchall()
    
    def remove_channel(
        self,
        chid: int
    ):
        with self.connect:
            self.cursor.execute(
                "DELETE FROM channels "
                "WHERE chid=?",
                [chid]
            )
    
    def update_balance(
        self,
        user_id: int,
        balance: int
    ):
        with self.connect:
            self.cursor.execute(
                "UPDATE users SET balance=balance+? "
                "WHERE user_id=?",
                [balance, user_id]
            )

