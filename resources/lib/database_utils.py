import sqlite3


class User:
    def __init__(self, username, reason, game, date):
        self.username = username
        self.reason = reason
        self.game = game
        self.date = date


def ReadUsers(prompt):
    con = sqlite3.connect('lib/the_list.db')
    cur = con.cursor()

    matches = []

    for row in cur.execute(f"SELECT * FROM user_table;"):
        if prompt['username-field'].lower() == row[0].lower() and row[0] != '':
            matches.append(row)
            continue
        elif prompt['reason-field'].lower() == row[1].lower() and row[1] != '':
            matches.append(row)
            continue
        elif prompt['game-field'].lower() == row[2].lower() and row[2] != '':
            matches.append(row)
            continue
        elif prompt['date-field'].lower() == row[3].lower() and row[3] != '':
            matches.append(row)
            continue


    con.close()

    message = ''

    for x in matches:
        message = message + f"""
        Username: {x[0]}
        Reason: {x[1]}
        Game: {x[2]}
        Date: {x[3]}\n
        """
    
    return message


def AddUser(username, reason, game, date):
    con = sqlite3.connect('lib/the_list.db')
    cur = con.cursor()

    cur.execute(f"INSERT INTO user_table(username, reason, game, date) VALUES('{username}', '{reason}', '{game}', '{date}');")

    con.commit()
    con.close()
