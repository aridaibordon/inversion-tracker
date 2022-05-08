import os
import psycopg2


def connect_database():
    # Create connection and cursor to PosgreSQL database.
    con = psycopg2.connect(
        host=os.environ["SERVER"],
        dbname=os.environ["DATABASE"],
        user=os.environ["USERSQL"],
        password=os.environ["PASSSQL"]
    )
    return con, con.cursor()


def close_session(connection, cursor):
    # Close current cursor and connection.
    cursor.close()
    connection.close()


def create_tables() -> None:
    # Create tables in current db.
    con, cur = connect_database()

    cur.execute('CREATE TABLE IF NOT EXISTS balance (id bigserial NOT NULL PRIMARY KEY, degiro float, coinbase float, personal float, order date DEFAULT CURRENT_DATE)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS address (id bigserial NOT NULL PRIMARY KEY, address text NOT NULL)')

    con.commit()
    close_session(con, cur)


def add_address(address: str) -> None:
    # Add BTC address to database.
    con, cur = connect_database()

    cur.execute('INSERT INTO address (address) VALUES (%s)', (address,))

    con.commit()
    close_session(con, cur)


def update_balance(degiro: float, coinbase: float, personal: float) -> None:
    # Insert new balance to database.
    con, cur = connect_database()

    cur.execute('INSERT INTO balance (degiro, coinbase, personal) VALUES (%s, %s, %s)',
                (degiro, coinbase, personal))

    con.commit()
    close_session(con, cur)


def return_degiro_balance(count: int) -> list:
    # Return last {count} balances.
    con, cur = connect_database()

    cur.execute(
        "SELECT degiro FROM balance ORDER BY id DESC LIMIT %s", (str(count),))

    balance = [item[0] for item in cur.fetchall()]
    close_session(con, cur)

    return balance


def return_degiro_balance_old(count: int) -> list:
    # Return last {count} balances. -> Old table on database
    con, cur = connect_database()

    cur.execute(
        "SELECT balance, date FROM degiro ORDER BY id DESC LIMIT %s", (str(count),))

    data = cur.fetchall()

    balance = [item[0] for item in data]
    date = [item[1].strftime("%d/%m/%Y") for item in data]

    close_session(con, cur)

    return balance, date


def get_addresses() -> tuple:
    # Return all addresses in database.
    con, cur = connect_database()

    cur.execute('SELECT address FROM address')

    addresses = [address[0] for address in cur.fetchall()]
    close_session(con, cur)

    return addresses
