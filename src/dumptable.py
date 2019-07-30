import sqlite3
import sys

if len(sys.argv) < 3:
    print("Needs 2 args: the DB path and max number of rows (0 for all rows)")
    exit()

conn = sqlite3.connect(sys.argv[1])
cursor = conn.cursor()
cursor.execute("SELECT * FROM Items")
rows = cursor.fetchall()

num_rows = int(sys.argv[2])

for row in rows:
    num_rows -= 1
    if num_rows == 0:
        break
    print(row)

conn.close()
