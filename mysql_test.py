# pip3 install pymysql
# pip3 install mysqlclient
# pip3 install mysql-connector-python

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='ec2-3-38-108-28.ap-northeast-2.compute.amazonaws.com',
                              database='bbgg')

cursor = cnx.cursor()
cursor.execute("SELECT * FROM Product")

result = cursor.fetchall()

for x in result:
  print(x)
cnx.close()