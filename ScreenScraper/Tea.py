import sqlite3

def sqlite_table_schema(conn, name):
	cur = conn.execute("SELECT sql FROM sqlite_master WHERE name=?;", [name])
	sql = cur.fetchone()[0]
	cur.close()
	print(sql)


conn = sqlite3.connect("tea.db")

def Get_Data(x):
	c = conn.cursor()
	
	query = 'SELECT Tea1, Tea2, Tea3 FROM Teas WHERE Name = ?'
	c.execute(query, (x,))
	records = c.fetchall()
	for i in records:
		print(i)

	print('\n' *3)
	query = 'SELECT Question FROM Questions WHERE Name = ?'
	c.execute(query, (x,))
	record1 = c.fetchall()

	query = 'SELECT Ans1, Ans2, Ans3 FROM Questions WHERE Name = ?'
	c.execute(query, (x,))
	record2 = c.fetchall()
	
	for i, j in enumerate(record1):
		print(j)
		print(record2[i])
		print()


	c.close()


x = input("enter the name : ")
x = x.lower()
x = x.capitalize()

print('\n' *3)

Get_Data(x)

conn.close()