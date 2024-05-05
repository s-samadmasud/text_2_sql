# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('test.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), DEPARTMENT VARCHAR(255), 
SECTION VARCHAR(255));"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Samad', 'Computer Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Suhal', 'Computer Science', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Masud', 'Accounting', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Rahul', 'Finance', 'C')''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()