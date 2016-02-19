# this python file use for insert sensor data in database

#import MyDB connection module
import MyDB
db = MyDB.DB()
i=12
j=22
k=33
db.execute("INSERT INTO Zones (user_id,zone1) \
      VALUES (%s, NOW() )", [i]);


db.commit()
print "Records created successfully";
db.close()