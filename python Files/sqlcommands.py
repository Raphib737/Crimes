import sqlite3

# Connect to the database and create a cursor for it.
filename = 'crime.db'
db = sqlite3.connect(filename)
cursor = db.cursor()

# Get the year from the user and build the SELECT command
# using string concatenation.
print('number of crimes per day of the week, in descending order')
command = '''SELECT DayWeek, COUNT(*)
FROM Crime
GROUP BY DayWeek
ORDER BY COUNT(*) desc;'''

# Execute the command.
cursor.execute(command)

# Iterate over the results and print them out.
for tuple in cursor:
    if tuple[0] != 'Saturda':
        print(tuple[0], tuple[1])


command = '''SELECT COUNT(*)
             FROM Crime
             WHERE DayWeek = 'Friday'AND Time < "12:00:00";'''

cursor.execute(command)

for tuple in cursor:
    before6 = tuple[0]

command = '''SELECT COUNT(*)
             FROM Crime
             WHERE DayWeek = 'Friday'AND Time >= "12:00:00";'''

cursor.execute(command)

for tuple in cursor:
    after6 = tuple[0]

print('number of crimes committed on friday before noon vs after:')
print(before6, after6)






db.commit()
db.close()
