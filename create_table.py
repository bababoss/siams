import MyDB
db = MyDB.DB()

try:
    db.execute("CREATE TABLE Zones (user_id INT NOT NULL,zone1 TIMESTAMP,zone2 TIMESTAMP,zone3 TIMESTAMP,zone4 TIMESTAMP);")
    print "table created successfully"
except:
    db.conn.rollback()
    db.execute("DROP TABLE ZONES")
    print "Drop database successfully"
    db.execute("CREATE TABLE ZONES (user_id INT NOT NULL , zone1 TIMESTAMP, zone2 TIMESTAMP,  zone3 TIMESTAMP,zone1 TIMESTAMP);")
    print "Drop database and again create successfully"
db.commit()
db.close()