"""
    Justin Kreifels
    03-08-2022
    This program builds on the what_a_book database
    It allows the user to traverse the database tables and view results
    It also allows the user add books to the wishlist table for certain users
    It checks for bad input
    It checks for SQL errors
"""

import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def show_menu():
    """ This function prints a menu to the console
        and asks the user for input

    Returns:
        int: the users input parsed to an int
    """

    print('\n-- NOW DISPLAYING MAIN MENU --\n')

    try:
        print('\t1. View Books\t2. View Locations\t3. My Account\t4. Leave Store\n')

        userInput = int(
            input('\tPlease input a number (example 1 for books) >> '))

        if userInput <= 0 or userInput > 4:
            print('\t\tError -- Please Enter Valid Menu Option Only!\n')
            return show_menu()

        return userInput

    except ValueError:
        print('\t\tError -- Please Enter A Number Only!\n')
        return show_menu()


def show_books(cursor):
    """ This function prints a SQL SELECT statement from 
        whatabook.book table to the console

    Args:
        cursor (object): Database cursor to execute statements
    """

    cursor.execute(
        'SELECT book_id, book_name, author, details FROM book ORDER BY book_id ASC')

    books = cursor.fetchall()

    print('\n\t-- NOW DISPLAYING ALL BOOKS --\n')

    for book in books:
        print(
            f'\tBook Name: {book[0]}\n\tAuthor: {book[2]}\n\tBook Details: {book[1]}\n')


def show_locations(cursor):
    """ This function prints a SQL SELECT statement 
        from whatabook.store to the console

    Args:
        cursor (object): Database cursor to execute statements
    """

    cursor.execute('SELECT store_id, locale FROM store ORDER BY store_id')

    locales = cursor.fetchall()

    print('\n\t-- NOW DISPLAYING ALL LOCATIONS --\n')

    for locale in locales:
        print(f'\n\tLocale: {locale[1]}\n')


def validate_user():
    """ This function asks the user from input to 
        select which user they will update in the whatabook database

    Returns:
        int: The users input parsed to an int
    """

    try:
        userID = int(
            input('\n\tPlease enter a valid customer id (1, 2, or 3) >> '))

        if userID < 0 or userID > 3:
            print('\t\tError -- Please Enter A Valid User ID Only!\n')
            return validate_user()

        return userID

    except ValueError:
        print('\t\tError -- Please Enter A Number Only!\n')
        return validate_user()


def show_account_menu():
    """ This function prints a menu to the console, 
        and asks the user for input

    Returns:
        int: The users input parsed to an int
    """

    print('\n\t-- NOW DISPLAYING ACCOUNT MENU --\n')

    try:
        print('\t1. Wishlist\t2. Add Book\t3. Main Menu\n')

        userInput = int(
            input('\tPlease input a number (example 1 for wishlist) >> '))

        if userInput <= 0 or userInput > 3:
            print('\t\tError -- Please Enter Valid Book ID Only!\n')
            return show_account_menu()

        return userInput

    except ValueError:
        print('\t\tError -- Please Enter A Number Only!\n')
        return show_account_menu()


def show_wishlist(cursor, user_id):
    """ This function prints a SQL joined SELECT statement 
        from whatabook.wishlist, whatabook.book, whatabook.user,
        and prints it to the console

    Args:
        cursor (object): Database cursor to execute statements
        user_id (int): The users input from show_account_menu()
    """

    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author "
                   + "FROM wishlist "
                   + "INNER JOIN user ON wishlist.user_id = user.user_id "
                   + "INNER JOIN book ON wishlist.book_id = book.book_id "
                   + "WHERE user.user_id = {}".format(user_id))

    wishlist = cursor.fetchall()

    print('\n\t-- NOW DISPLAYING WISHLIST --\n')

    for book in wishlist:
        print(f"\tBook Name: {book[4]}\n\tAuthor: {book[5]}\n")


def show_books_to_add(cursor, user_id):
    """ This function prints a SQL SELECT statement 
        from whatabook.book to the console

    Args:
        cursor (object): Database cursor to execute statements
        user_id (int): The users input from validate_user()
    """

    query = ("SELECT book_id, book_name, author, details "
             + "FROM book "
             + "WHERE book_id NOT IN "
             + "(SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    cursor.execute(query)

    booksToAdd = cursor.fetchall()

    print('\n\t-- NOW DISPLAYING BOOKS LEFT TO ADD --\n')

    for book in booksToAdd:
        print(f"\tBook Id: {book[0]}\n\tBook Name: {book[1]}\n")


def add_book_to_wishlist(cursor, user_id, book_id):
    """ This function inserts a new book into whatabook.wishlist

    Args:
        cursor (object): Database cursor to execute statements
        user_id (int): The users input from validate_user()
        book_id (int): Users input for what book to be added
    """

    cursor.execute(
        f'INSERT INTO wishlist(user_id, book_id) VALUES({user_id}, {book_id})')

    print(f'\t\nSUCCESS: {book_id} was added to your wishlist\t')


try:
    """ try/catch for handling SQL database errors """

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = show_menu()

    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                    book_id = int(
                        input("\n\tEnter the id of the book you want to add: "))

                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()

                    print(
                        f"\n\tBook id: {book_id} was added to your wishlist!")

                if account_option < 0 or account_option > 3:
                    print("\n\tInvalid option, please retry...")

                account_option = show_account_menu()

        user_selection = show_menu()

    print("\n\n  Thank you for using the application! See you again!")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
