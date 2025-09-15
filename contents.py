import sqlite3
import hashlib

connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata(
id INTEGER PRIMARY KEY ,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL 
)
""")

username1,password1 = "tehseen1301" , hashlib.sha256("tehseen@1301".encode()).hexdigest()
username2,password2 = "tanya1301" , hashlib.sha256("tanya@1301".encode()).hexdigest()
username3,password3 = "tara1301" , hashlib.sha256("tara@1301".encode()).hexdigest()
username4,password4 = "tina1301" , hashlib.sha256("tina@1301".encode()).hexdigest()

cursor.execute("INSERT INTO userdata (username , password) VALUES(?, ?)" , (username1, password1))
cursor.execute("INSERT INTO userdata (username , password) VALUES(?, ?)" , (username2, password2))
cursor.execute("INSERT INTO userdata (username , password) VALUES(?, ?)" , (username3, password3))
cursor.execute("INSERT INTO userdata (username , password) VALUES(?, ?)" , (username4, password4))

connection.commit()