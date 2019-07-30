import poefixer as p
import sqlite3

VOLUME_PATH_PREFIX = "data/"


def connect_to_db():
    return sqlite3.connect(VOLUME_PATH_PREFIX + "bear.db")


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Items (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        account_name NVARCHAR(64),\
        category NVARCHAR(64),\
        name NVARCHAR(64),\
        type_line NVARCHAR(64),\
        stash NVARCHAR(128),\
        note NVARCHAR(64)\
    )")
    conn.commit()


def insert_item(cursor, item):
    cursor.execute(
        "INSERT INTO Items(account_name, category, name, type_line, stash, note) VALUES(?, ?, ?, ?, ?, ?)", item)


conn = connect_to_db()
create_table(conn)
cursor = conn.cursor()
api = p.PoeApi(next_id="457655933-474459305-447398401-512121627-486185425")
i = 0

while(i < 10):
    for stash in api.get_next():
        if(stash.public == True):
            for item in stash.items:
                if "~price" in str(str(item.note).encode('utf-8')):
                    insert_item(cursor, (
                        str(stash.accountName).encode('utf-8').decode('utf-8'),
                        str(item.category).encode('utf-8').decode('utf-8'),
                        str(item.name).encode('utf-8').decode('utf-8'),
                        str(item.typeLine).encode('utf-8').decode('utf-8'),
                        str(stash.stash).encode('utf-8').decode('utf-8'),
                        str(item.note).encode('utf-8').decode('utf-8')
                    ))

    print(api.next_id)
    api = p.PoeApi(next_id=api.next_id)
    i = i+1

conn.commit()
conn.close()
