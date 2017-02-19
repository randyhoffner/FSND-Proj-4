#!/usr/bin/env python

# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2




def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE FROM matches;"
    db_cursor.execute(query)
    db.commit()
    db.close();


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE FROM players;"
    db_cursor.execute(query)
    db.commit()
    db.close();


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT COUNT(id) AS num FROM players;"
    db_cursor.execute(query)
    results = db_cursor.fetchone()
    db.close()
    if results:
        return results[0]
    else:
        return '0'


def registerPlayer(name):

    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).

    Query command execute() includes "(name,)" to protect database from
    sql injection attack.
"""

    db = connect()
    db_cursor = db.cursor()
    db_cursor.execute("INSERT INTO players (name) VALUES (%s);", (name,));
    db.commit()
    db.close()



def playerStandings():

    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played

    Query execute() commands set up to prevent sql injection attack.
"""

    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM standings;"
    db_cursor.execute(query)
    matches = db_cursor.fetchall()
    db.commit()
    db.close()
    return matches


def reportMatch(winner, loser):

    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
"""


    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    db_cursor.execute(query, (winner, loser))
    db.commit()
    db.close()

def swissPairings():

    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2) --
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
"""

    pair = []
    db = connect()
    db_cursor = db.cursor()
    db_cursor.execute("SELECT id,name,total_wins FROM Standings ORDER BY total_wins DESC;")
    win_pair_list = db_cursor.fetchall()

    # If the total number of players divided by 2 leaves a
    # remainder of 0, there is an even number of players.
    # Otherwise, print "else:" statement.
    if len(win_pair_list) % 2 == 0:
        # "for" loops over the length of the win_pair_list, ordered
        # from top (most total wins) to bottom (fewest tota wins),
        # returning id1 ([i][0]), name1 ([i][1]); and id2 ([i+1][0]),
        # name2 ([i+1][1]) for each pair, then appends the pair.
        for i in range(0, len(win_pair_list), 2):
            collect_players = win_pair_list[i][0], win_pair_list[i][1], \
                              win_pair_list[i+1][0], win_pair_list[i+1][1]
            pair.append(collect_players)
        return pair
    else:
        print "An uneven number of players is registered"

    db.commit()
    db.close()
