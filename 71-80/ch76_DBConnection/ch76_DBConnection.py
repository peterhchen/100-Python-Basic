# Step 1: import mysql.connector
import mysql.connector
# step 2: connect to database
mydb = mysql.connector.connect (host="localhost", user="root", passwd="Pc1997=ch", 
  database="mydb", auth_plugin='caching_sha2_password')
mycursor = mydb.cursor()
mycursor.execute ("select * from student")
# print ('Use mycurcors')
# for i in mycursor:
#     print (i)

# There is another way. You can store the data soemwhere
print ('Use ftechall')
res = mycursor.fetchall ()
for i in res:
    print(i)