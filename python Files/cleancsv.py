'''
Molly Shopper, Raphael Baysa, Amalia Safer
final project cs105
cleancsv.py
'''

data = open('crime.csv')
new_data = open('new_crime.csv', 'w')

crimes = ['RESIDENTIAL BURGLARY', 'AGGRAVATED ASSAULT', 'ROBBERY', 'COMMERCIAL BURGLARY', 'SIMPLE ASSAULT', 'FRAUD', 'WEAPONS CHARGE', 'DRUG CHARGES', 'OTHER LARCENY', 'AUTO THEFT', 'VANDALISM', 'CRIMES AGAINST CHILDREN', 'LARCENY FROM MOTOR VEHICLE', 'EMBEZELLMENT']
print('INCIDENT_TYPE_DESCRIPTION' + ',' + 'TIME' + ',' + 'WEAPONTYPE' + ',' + 'SHOOTING' + ',' + 'DAY_WEEK', file = new_data)

for row in data:
    x = row.split(',')
    if x[2] in crimes:
        from_date = x[6].split(' ')
        if str(from_date[1][:2]) == '12' and from_date[2] == 'AM':
            time = '00' + str(from_date[1][2:])
        elif from_date[2] == 'PM' and str(from_date[1][:2]) != '12':
            time = str(int(from_date[1][:2]) + 12) + str(from_date[1][2:])
        else:
            time = from_date[1]
        print(x[2] + ',' + time + ',' + x[7] + ',' + x[8] + ',' + x[13], file = new_data)
