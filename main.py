import sqlite3 as db

def showData(limit=None):
	# Takes in 0 or 1 parameter. if provided one parameter that is the # of data we want to select. 
	# If 0 parameters are given shows EVERYTHING in the database
	if(limit is not None):
		print("Invalid Type of Parameter")
	else:
	#Displays all the data in the Crime Table
		conn = db.connect('crime.db')
		cursor = conn.cursor()
		counter = 0
		for data in cursor.execute("SELECT * FROM Crime"):
			if(limit is None):
				print data
			else:
				if(counter == limit):
					break
				else:
					print data
					counter = counter + 1
		conn.close()
	return


if __name__ == "__main__":
	showData();











#  -----------------------------------------------------------------------------------------------------
# | DATA INSERTION METHODS ARE FOUND HERE: createTable() , insertData(), cleanData DO NOT TOUCH OR MODIFY OR USE |
#  -----------------------------------------------------------------------------------------------------

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
				(Inc_Type_Desc varchar(255), Time varchar(255), WeaponType varchar(255),  Shooting varchar(255), DayWeek varchar(255)); ''')

	conn.commit()
	print("Successfully created Crime Table")

def insertData():
	#Takes in our csv data and puts it into our crime.db which is just a local database. 
	#Only needs to be ran once

	conn = db.connect('crime.db')
	cursor = conn.cursor()
	data = open("new_crime.csv")
	counter = 0
	for x in data:
		if counter == 0:
			counter = counter + 1
		else:
			x = x.split(",")
			cursor.execute(('''INSERT INTO Crime VALUES('%s','%s','%s','%s','%s')'''%(x[0],x[1],x[2],x[3],x[4])))
	print("Successfully inserted into database")
	conn.commit()
	data.close()

# def cleanData():
# 	#Takes our crime.csv and cleans up the data so that the new csv only contain 
# 	#the data we need so database insertion is easy.
# 	data = open('crime.csv')
# 	new_data = open('new_crime.csv', 'w')

# 	crimes = ['RESIDENTIAL BURGLARY', 'AGGRAVATED ASSAULT', 'ROBBERY', 'COMMERCIAL BURGLARY', 'SIMPLE ASSAULT', 'FRAUD', 'WEAPONS CHARGE', 'DRUG CHARGES', 'OTHER LARCENY', 'AUTO THEFT', 'VANDALISM', 'CRIMES AGAINST CHILDREN', 'LARCENY FROM MOTOR VEHICLE', 'EMBEZELLMENT']
# 	print('INCIDENT_TYPE_DESCRIPTION' + ',' + 'TIME' + ',' + 'WEAPONTYPE' + ',' + 'SHOOTING' + ',' + 'DAY_WEEK', file = new_data)

# 	for row in data:
# 	    x = row.split(',')
# 	    if x[2] in crimes:
# 	        from_date = x[6].split(' ')
# 	        time = from_date[1]        
# 	        print(x[2] + ',' + time + ',' + x[7] + ',' + x[8] + ',' + x[13], file = new_data)


