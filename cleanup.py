import sqlite3
from settings import *

def isSchemaThere(conn):
	cur = conn.cursor()
	cur.execute("SELECT name FROM sqlite_master WHERE name='links'")
	if len(cur.fetchall()) > 0:
		return True
	return False

conn = sqlite3.connect(LOCAL_LINK_DB)
if isSchemaThere(conn) == True:
    cur = conn.cursor()
    cur.execute("DELETE FROM links WHERE first_seen < datetime('now', '-7 day')")
    cur.execute("VACUUM")
    conn.commit()
    conn.close()

