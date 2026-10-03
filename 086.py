import sqlite3


conn=sqlite3.connect('./output/sample.db')
cur=conn.cursor()


sql="""
create table product(
id integer primary key autoincrement,
title text not null,
price integer,
link text)
"""

cur.execute(sql)


conn.commit()


conn.close()

