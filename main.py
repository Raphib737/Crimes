import sqlite3 as db

def createTable():
	#Creates the table in the database we need 
	#This table will be Crime(String date,String Time, String IncidentType,String WeaponType)
	#If you would like to add another table change Line #16 with your new table
	conn = db.connect('crime.db')
	cursor = conn.cursor()
	try:
		cursor.execute("Drop Table Crime")
		conn.commit()
		print("Successfully dropped Crime Table")
	except:
		print("No Crime Table Found")

	cursor.execute('''CREATE Table Crime 
				(date varchar(255), day varchar(255), Time varchar(255),  IncType varchar(255), WepType varchar(255)); ''')

	conn.commit()
	print("Successfully created Crime Table")


def insertData():
	#Takes in our csv data and puts it into our crime.db which is just a local database. 
	#Only needs to be ran once

	conn = db.connect('crime.db')
	cursor = conn.cursor()
	
	data = open("crime.csv")
	counter = 0
	for x in data:
		if counter == 0:
			counter = counter + 1
		else:
			x = x.split(",")
			date = x[6].split(" ")[0]
			time = x[6].split(" ")[1]
			cursor.execute(('''INSERT INTO Crime VALUES('%s','%s','%s','%s','%s')'''%(date,x[13],time,x[2],x[7])))
	print("Successfully inserted into database")
	conn.commit()
	data.close()


def showData():
	#Displays all the data in the Crime Table
	conn = db.connect('crime.db')
	cursor = conn.cursor()
	
	for data in cursor.execute("SELECT * FROM Crime"):
		print data

	conn.close()


if __name__ == "__main__":
	createTable()
	insertData()
	showData()









