# https://github.com/Krefails/csd-310
# Justin Kreifels, 2-19-2022
# This program prints an INNER join SQL statement to the console

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

    cursor.execute('SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id')

    teamPlayers = cursor.fetchall()

    print('-- DISPLAYING PLAYER RECORDS --')
    
    for teamPlayer in teamPlayers:
        print(f'Player ID: {teamPlayer[0]}\nFirst Name: {teamPlayer[1]}\nLast Name: {teamPlayer[2]}\nTeam Name: {teamPlayer[3]}\n')
    
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