import sqlite3


def ReadUsers(prompt):
    con = sqlite3.connect('lib/the_list.db')
    cur = con.cursor()

    for row in cur.execute(f'SELECT * FROM user_table;'):
        for value in row:
            if prompt.lower() in value.lower():
                return row

    con.close()


def AddUser(username, reason, game, date):
    con = sqlite3.connect('lib/the_list.db')
    cur = con.cursor()

    cur.execute(f"INSERT INTO user_table(username, reason, game, date) VALUES('{username}', '{reason}', '{game}', '{date}');")

    con.commit()
    con.close()
