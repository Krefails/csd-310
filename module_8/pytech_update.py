# https://github.com/Krefails/csd-310
# Justin Kreifels, 2-15-2022

import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "pysports_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True
}

try:
    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()

    cursor.execute('SELECT team_id, team_name, mascot FROM team')

    teams = cursor.fetchall()

    print('\n  -- DISPLAYING TEAM RECORDS --')

    for team in teams:
        print(f'Team ID: {team[0]}\nTeam Name: {team[1]}\nMascot: {team[2]}\n')

    cursor.execute('SELECT player_id, first_name, last_name, team_id FROM player')

    players = cursor.fetchall()

    print('\n  -- DISPLAYING PLAYER RECORDS --')

    for player in players:
        print(f'Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam ID: {player[3]}\n')

    input('\n\n  Press any key to continue... ')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('  The supplied username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('  The specified database does not exist')

    else:
        print(err)

finally:
    db.close()
