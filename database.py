import sqlite3


def connect_dataset():
    con = sqlite3.connect("inversion.db")
    return con, con.cursor()


def return_balance() -> list:
    con, cur = connect_dataset()
    return cur.execute("SELECT balance FROM degiro ORDER BY id DESC LIMIT 2").fetchall()
    

def create_database() -> None:
    con, cur = connect_dataset()

    cur.execute("CREATE TABLE IF NOT EXISTS degiro (id integer PRIMARY KEY, balance float, orderDate date DEFAULT(datetime()))")
    cur.execute("CREATE TABLE IF NOT EXISTS operations (id integer PRIMARY KEY, active text, number float, cost float, orderDate date DEFAULT(datetime()), crypto bool)")
    cur.execute("CREATE TABLE IF NOT EXISTS portfolio (id integer PRIMARY KEY, active text, number float, orderDate date DEFAULT(datetime()), crypto bool)")
    con.commit()


def update_degiro_db(balance: float) -> None:
    con, cur = connect_dataset()

    cur.execute("INSERT INTO degiro (balance) VALUES (?)", (balance,))
    con.commit()
    cur.close()


def add_operation(active, number, cpu, crypto) -> None:
    con, cur = connect_dataset()

    cur.execute("INSERT INTO operations (active, number, cpu, crypto) VALUES (?, ?, ?, ?)", (active, number, cpu, crypto))
    con.commit()
    cur.close()


def get_portfolio() -> None:
    con, cur = connect_dataset()

    cur.execute("SELECT active, SUM(number), crypto FROM operations GROUP BY active")
    for active, number, crypto in cur.fetchall():
        cur.execute("INSERT INTO portfolio (active, number, crypto) VALUES (?, ?, ?)", (active, number, crypto))

    con.commit()
    cur.close()
