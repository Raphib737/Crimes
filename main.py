#Done by: Amalia Safer Molly Shopper Raphael Baysa
#Final Project cs105 Analyzing Crime Data

import sqlite3 as db
import matplotlib.pyplot as plt

#  --------------------------------------------------------------------------------------------------------------------------
# | DATA manipulation/Graphing  Methods: showData() , crimesPerDay(type:List), CrimesPerHour(type:List) KindsOfCrime()      |
#  --------------------------------------------------------------------------------------------------------------------------
def showData(limit=None):
	# Takes in 0 or 1 parameters. If provided one parameter that is the # of data we want to select. 
	# If 0 parameters are given shows EVERYTHING in the database
	conn = db.connect('crime.db')
	cursor = conn.cursor()
	counter = 0
	Data = []
	for partialdata in cursor.execute("SELECT * FROM Crime"):
		if(limit is None):
			Data.append(partialdata)
		else:
			if(counter == limit):
				break
			else:
				Data.append(partialdata)
				counter = counter + 1
	conn.close()
	# for x in Data:
	# 	print x
	return Data
#******************************************************************************************************************
def crimesPerDay(data):
	#Displays a bar graph that shows the amount of 
	#crimes done on each day of the week based on the data provided.

	#Static Data 
	daytoNum = {"Sunday":1,"Monday":2,"Tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6,"Saturday":7,"Saturda":7}
	daysOfWeek = [0,"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",0]

	#X and Y axis for the graph
	numOccurences = [0,0,0,0,0,0,0,0,0]
	xAxis = [x for x in range(9)]
	
	#Traverse through data and +1 each index pertaining to the day of the week
	for record in data:
		numOccurences[daytoNum[record[4]]] = numOccurences[daytoNum[record[4]]] + 1

	#Graphing data from above
	plt.xlabel('Days of the Week')
	plt.ylabel('Crimes Committed')
	plt.title('Crimes Committed per Day from Data')
	plt.xticks(xAxis,daysOfWeek,rotation='vertical')
	plt.ylim([1000,max(numOccurences)+1000])
	ax = plt.subplot(111)
	ax.bar(xAxis, numOccurences, align='center', color = "orange", edgecolor="black")
	plt.show()
#******************************************************************************************************************
def crimesPerHour(data):

	#Static Data for yaxis
	normalizedHours = ["12am","1am","2am","3am","4am","5am","6am","7am","8am","9am","10am","11am","12pm","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm"]
	
	#Hour = xAxis | numOccurences = yAxis
	hour = [x for x in range(24)]
	numOccurences = [0 for x in range(24)]
	
	#deserialize Values by Hour thus round down by the hour
	for x in data:
		numOccurences[int(x[1].split(":")[0])] =  numOccurences[int(x[1].split(":")[0])] + 1

	#Plot the Data
	plt.xlabel('Hours of the day')
	plt.ylabel('Number Crimes Committed')
	plt.title('Crimes Committed per Hour from Data')
	plt.xticks(hour,normalizedHours,rotation='vertical')
	ax = plt.subplot(111)
	ax.plot(hour, numOccurences, color = "blue")
	plt.show()
#******************************************************************************************************************
def KindsOfCrime():
	#Will Read from the crime.csv and make a graph out of crime in our list of crimes and 
	#will display how many of each were accounted for.
	
	#Static Data
	crimes = ['RESIDENTIAL BURGLARY', 'AGGRAVATED ASSAULT', 'ROBBERY', 'COMMERCIAL BURGLARY', 'SIMPLE ASSAULT', 'FRAUD', 'WEAPONS CHARGE', 'DRUG CHARGES', 'OTHER LARCENY', 'AUTO THEFT', 'VANDALISM', 'CRIMES AGAINST CHILDREN', 'LARCENY FROM MOTOR VEHICLE', 'EMBEZELLMENT']
	xAxis = [x for x in range(len(crimes))]
	
	#Read Data
	data = open('crime.csv')

	#Dynamic Data
	histoData = {}
	counter = 0

	#Parse Data and count the crimes if they meet criteria
	for record in data:
		record = record.split(",")
		if record[2] in crimes:
			try:
				histoData[record[2]] = histoData[record[2]] + 1
			except:
				histoData[record[2]] = 1
		counter += 1

	#Create x,y list values for the graph plot 
	key = []
	values = []
	for keys in histoData.keys():
  		key.append(keys)
  		values.append(histoData[keys])

  	#Plot the Data
  	plt.xlabel('Type of Crime')
	plt.ylabel('Number Committed')
	plt.title('Crimes Committed by Type')
	plt.xticks(xAxis,key,rotation='vertical')
	ax = plt.subplot(111)
	ax.bar(xAxis, values, align='center', color = "blue", edgecolor="black")
	plt.show()
#******************************************************************************************************************


if __name__ == "__main__":
	#Will delete any prior tables and create a new Table and insert the csv specified into the db
	#createTable()
	#insertData()

	#Shows data from the database
	# data = showData()

	#Display Data
	#crimesPerDay(data)
	#crimesPerHour(data)
	#KindsOfCrime()
	pass


#  ---------------------------------------------------------------------------------------------------------------
# | DATA INSERTION METHODS ARE FOUND HERE: createTable() , insertData(), cleanData DO NOT TOUCH OR MODIFY OR USE |
#  ---------------------------------------------------------------------------------------------------------------
#******************************************************************************************************************
def createTable():
	#Creates the table in the database we need 
	#This table will be Crime(String Inc_Type, String Time, String WeaponType,String Shooting,String DayWeek)
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
#******************************************************************************************************************
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
			cursor.execute(('''INSERT INTO Crime VALUES('%s','%s','%s','%s','%s')'''%(x[0],x[1],x[2],x[3],x[4][:-1])))
	print("Successfully inserted into database")
	conn.commit()
	data.close()
#******************************************************************************************************************
#def cleanData():
	#Takes our crime.csv and cleans up the data so that the new csv only contain 
	#the data we need so database insertion is easy.
	# data = open('crime.csv')
	# new_data = open('new_crime.csv', 'w')

	# crimes = ['RESIDENTIAL BURGLARY', 'AGGRAVATED ASSAULT', 'ROBBERY', 'COMMERCIAL BURGLARY', 'SIMPLE ASSAULT', 'FRAUD', 'WEAPONS CHARGE', 'DRUG CHARGES', 'OTHER LARCENY', 'AUTO THEFT', 'VANDALISM', 'CRIMES AGAINST CHILDREN', 'LARCENY FROM MOTOR VEHICLE', 'EMBEZELLMENT']
	# print('INCIDENT_TYPE_DESCRIPTION' + ',' + 'TIME' + ',' + 'WEAPONTYPE' + ',' + 'SHOOTING' + ',' + 'DAY_WEEK', file = new_data)

	# for row in data:
	#     x = row.split(',')
	#     if x[2] in crimes:
	#         from_date = x[6].split(' ')
	#         if str(from_date[1][:2]) == '12' and from_date[2] == 'AM':
	#             time = '00' + str(from_date[1][2:])
	#         elif from_date[2] == 'PM' and str(from_date[1][:2]) != '12':
	#             time = str(int(from_date[1][:2]) + 12) + str(from_date[1][2:])
	#         else:
	#             time = from_date[1]
	#         print(x[2] + ',' + time + ',' + x[7] + ',' + x[8] + ',' + x[13], file = new_data)

