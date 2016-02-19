import MyDB
db = MyDB.DB()

db.conn.rollback()
db.execute("DROP TABLE ZONES")
print "drop Measurement database successfully"

db.commit()
db.close()