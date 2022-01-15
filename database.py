import os
import psycopg2


def connect_dataset():
    con = psycopg2.connect(
        host=os.environ["SERVER"],
        dbname=os.environ["DATABASE"],
        user=os.environ["USERSQL"],
        password=os.environ["PASSSQL"]
        )
    return con, con.cursor()


def close_session(connection, cursor):
    cursor.close()
    connection.close()


def return_balance() -> list:
    con, cur    = connect_dataset()
    balance     = cur.execute("SELECT balance FROM degiro ORDER BY id DESC LIMIT 2").fetchall()
    close_session(con, cur)
    return balance
    

def create_database() -> None:
    con, cur = connect_dataset()

    cur.execute("CREATE TABLE degiro (id integer BIGSERIAL NOT NULL PRIMARY KEY, balance float NOT NULL, orderDate date NOT NULL DEFAULT CURRENT_DATE)")
    cur.execute("CREATE TABLE operations (id integer BIGSERIAL NOT NULL PRIMARY KEY, active text NOT NULL, number float NOT NULL, cost float NOT NULL, orderDate date NOT NULL DEFAULT CURRENT_DATE, crypto bool NOT NULL)")
    cur.execute("CREATE TABLE portfolio (id integer BIGSERIAL NOT NULL PRIMARY KEY, active text NOT NULL, number float NOT NULL, orderDate date NOT NULL DEFAULT CURRENT_DATE, crypto bool NOT NULL)")
    con.commit()
    close_session(con, cur)


def update_degiro_db(balance: float) -> None:
    con, cur = connect_dataset()

    cur.execute("INSERT INTO degiro (balance) VALUES (?)", (balance,))
    con.commit()
    close_session(con, cur)


def add_operation(active, number, cpu, crypto) -> None:
    con, cur = connect_dataset()

    cur.execute("INSERT INTO operations (active, number, cpu, crypto) VALUES (?, ?, ?, ?)", (active, number, cpu, crypto))
    con.commit()
    close_session(con, cur)


def get_portfolio() -> None:
    con, cur = connect_dataset()

    cur.execute("SELECT active, SUM(number), crypto FROM operations GROUP BY active")
    for active, number, crypto in cur.fetchall():
        cur.execute("INSERT INTO portfolio (active, number, crypto) VALUES (?, ?, ?)", (active, number, crypto))

    con.commit()
    close_session(con, cur)
