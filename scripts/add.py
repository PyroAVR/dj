#!/usr/bin/env python3
import sqlite3
import cgi
form = cgi.FieldStorage()

db = sqlite3.connect('../data/songs.db')
c = db.cursor()

if form.getvalue('link') == None:
     print('401')
     exit()
else:
    data = (form.getvalue('link'),)
    # print(form.getvalue('link'))
    c.execute("insert into \"songs\" values (?)", data)
    db.commit()
    print('200')
db.close()
