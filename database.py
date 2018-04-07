#Databse code for quotebot

#impoerts sqlite3
import sqlite3
from datetime import datetime, date


def database():
#creates connection, database and table (if needed):
        # connect to sqlite and creates a db file
        connect = sqlite3.connect("quotes.db")
        # create a cursos (Just like the cursor in an editor, its role is to keep track of where we are in the database.)
        cursor = connect.cursor()
        #created cursor executes a requested query - Create a table in this case
        cursor.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, quote text NOT NULL UNIQUE, author text NOT NULL, created date)")
        # if we performed any operation on the database other than sending queries, we need to commit those changes
        connect.commit()

        connect.close()


def check_quote(quote):
    # connect to sqlite and creates a db file
    connect = sqlite3.connect("quotes.db")
    # create a cursos (Just like the cursor in an editor, its role is to keep track of where we are in the database.)
    cursor = connect.cursor()
    cursor.execute("SELECT quote FROM quotes WHERE quote = ?", (quote,))
    quote_exist = cursor.fetchall()
    # check if quote already in database
    if quote_exist == []:
        return True
    else:
        return False

    connect.close()


def add_quote(quote, author):
    connect = sqlite3.connect("quotes.db")
    # create a cursos (Just like the cursor in an editor, its role is to keep track of where we are in the database.)
    cursor = connect.cursor()
    # add quote to the database
    cursor.execute("INSERT INTO quotes VALUES (NULL, ?, ?, ?)", (quote, author, datetime.now()))
    connect.commit()
    connect.close()
