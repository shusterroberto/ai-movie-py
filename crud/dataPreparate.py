import sqlite3

def data_preparate_learning_english():
    conn = sqlite3.connect('learning_english.db')

    conn.execute('''
                    CREATE TABLE IF NOT EXISTS lessons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    id_module INTEGER FOREN KEY,
                    creat_at DATETIME NOT NULL,
                    update_at DATETIME,
                    path VARCHAR(500))
                 ''')

    return True