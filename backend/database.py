import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("finance.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            is_income INTEGER,
            category TEXT,
            date TEXT
        )
        """)
        self.conn.commit()

    def add_transaction(self, amount, is_income, category, date):
        self.conn.execute("""
            INSERT INTO transactions (amount, is_income, category, date)
            VALUES (?, ?, ?, ?)
        """, (amount, int(is_income), category, date))
        self.conn.commit()

    def get_transactions(self):
        cursor = self.conn.execute("""
            SELECT id, amount, is_income, category, date
            FROM transactions
            ORDER BY id DESC
        """)

        return [
            {
                "id": row[0],
                "amount": row[1],
                "is_income": bool(row[2]),
                "category": row[3],
                "date": row[4]
            }
            for row in cursor
        ]

    def delete_transaction(self, tx_id):
        self.conn.execute("DELETE FROM transactions WHERE id=?", (tx_id,))
        self.conn.commit()