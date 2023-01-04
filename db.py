import pymysql

conn = pymysql.Connect(host='127.0.0.1', user='root', password='', database='project3')

cursor = conn.cursor()

# sql = '''CREATE TABLE user (
#         id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         name varchar(255))'''

sql = '''CREATE TABLE coffee (
        id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        price varchar(255),
        tasty varchar(255),
        tast varchar(255),
        blend varchar(255),
        roasting varchar(255),
        target int(10)
        )
        '''




cursor.execute(sql)

conn.close()