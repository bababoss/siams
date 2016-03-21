import MyDB
db = MyDB.DB()

db.conn.rollback()
db.execute("DROP TABLE monitor_analysis")
print "drop Measurement database successfully"

db.commit()
db.close()