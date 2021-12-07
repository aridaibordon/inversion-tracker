import sqlite3

def create_database() -> None:
    con = sqlite3.connect("inversion.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE degiro (id integer PRIMARY KEY, balance float, orderDate date DEFAULT(date()))")
    cur.execute("CREATE TABLE crypto (id integer PRIMARY KEY, coin text, crp_balance float, eur_balance float, orderDate date DEFAULT(date()))")
    cur.execute("CREATE TABLE operations (id integer PRIMARY KEY, active text, number float, cost float, orderDate date DEFAULT(date()))")


def update_degiro(balance: float) -> None:
    con     = sqlite3.connect("inversion.db")
    cur     = con.cursor()

    cur     = cur.execute("INSERT INTO degiro (balance) VALUES (?)", (balance,))
    
    con.commit()
    cur.close()