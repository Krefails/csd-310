# https://github.com/Krefails/csd-310
# Justin Kreifels, 2-20-2022
# This program prints an INNER join SQL statement to the console after inserting, updating, and deleting

import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "pysports_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True
}

def show_players(cursor, title):

    cursor.execute('SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id')

    teamPlayers = cursor.fetchall()

    print(f'-- DISPLAYING {title} --')
    
    for teamPlayer in teamPlayers:
        print(f'Player ID: {teamPlayer[0]}\nFirst Name: {teamPlayer[1]}\nLast Name: {teamPlayer[2]}\nTeam Name: {teamPlayer[3]}\n')

def update_player(cursor, table, teamID, oldFirstName, firstName, lastName):
    cursor.execute(f"UPDATE {table} SET team_id = {int(teamID)}, first_name = '{firstName}', last_name = '{lastName}' WHERE first_name = '{oldFirstName}'")

def insert_player(cursor, table, firstName, lastName, teamID):
    cursor.execute(f"INSERT INTO player (first_name, last_name, team_id) VALUES('{firstName}', '{lastName}', {int(teamID)})")

def delete_player(cursor, table, firstName):
    cursor.execute(f"DELETE FROM {table} WHERE first_name = '{firstName}'")

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    insert_player(cursor, "player", "Smeagol", "Shire Folk", 1)

    show_players(cursor, "PLAYERS AFTER INSERT")

    update_player(cursor, "player", 2, "Smeagol", "Gollum", "Ring Stealer")

    show_players(cursor, "PLAYERS AFTER UPDATE")

    delete_player(cursor, "player", "Gollum")

    show_players(cursor, "PLAYERS AFTER DELETE")

    db.commit() 

    input('\nPress any key to continue... ')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('  The supplied username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('  The specified database does not exist')

    else:
        print(err)

finally:
    db.close()