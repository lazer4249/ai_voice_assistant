import sqlite3
from datetime import datetime

def save_habit(action):
    conn = sqlite3.connect("data/habits.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS habits (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 action TEXT,
                 date TEXT)""")
    
    # Avoid duplicate entries within 5 minutes
    recent_time = datetime.now().timestamp() - 300
    c.execute("SELECT date FROM habits WHERE action = ? ORDER BY date DESC LIMIT 1", (action,))
    last = c.fetchone()
    
    if last is None or datetime.strptime(last[0], "%Y-%m-%d %H:%M:%S.%f").timestamp() < recent_time:
        c.execute("INSERT INTO habits (action, date) VALUES (?, ?)", (action, datetime.now()))
    
    conn.commit()
    conn.close()


def get_daily_summary():
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect("data/habits.db")
    c = conn.cursor()

    # Ensure the table exists before querying
    c.execute("""CREATE TABLE IF NOT EXISTS habits (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 action TEXT,
                 date TEXT)""")

    c.execute("SELECT action FROM habits WHERE date LIKE ?", (f"{today}%",))
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]

