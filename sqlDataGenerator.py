from random import randint, randrange
import datetime

#name generater
def generate_name():
    #split words to clear space
    firstTemp = fNameList.split()
    lastTemp = lNameList.split()

    #get first and last name by selecting random line
    firstNum = randint(0, len(firstTemp)-1)
    firstName = firstTemp[firstNum]
    lastNum = randint(0, len(lastTemp)-1)
    lastName = lastTemp[lastNum]

    return firstName + ',' + lastName


#get number of rows
while True:
    rowCount = input('Enter row count (max 500): ')
    try:
        rowCount = int(rowCount)
        if 0 < rowCount < 501:
            break
        else:
            print('Invalid. Try again.')
    except ValueError:
        print('Invalid. Try again.')

#open files with first and last names
with open('firstnames.txt', 'rt') as myfile: fNameList = myfile.read()
myfile.close()
with open('lastnames.txt', 'rt') as myfile: lNameList = myfile.read()
myfile.close()

#prep
i = 0 #counter for employees
employeeID = randint(4765894,9256417) #random starting point for employee ID
div = {
    '1': 'Retail',
    '2': 'Commercial',
    '3': 'Global',
    '4': 'Private',
    '5': 'Investment'}
thisYear = datetime.datetime.now().year
cutOffYear = thisYear - 40 #max employment 40 years
stat = ['Full Time', 'Contract']

newFile = open('employeeData.txt', 'w')
newFile.seek(0)
#start generating data
while i < rowCount:
    #generate employee ID
    employeeID += randint(5,50) #randomize increment of id
    #generate names and add to string
    name = generate_name()
    #generate banking division
    division = div[str(randint(1,5))]
    #generate employment year
    year = randint(cutOffYear, thisYear)
    #generate employment status (under 2 year possible contract employees)
    if (thisYear - year) < 3:
        status = stat[randint(0,1)]
    else:
        status = stat[0]
    #generate compensation (depends on employment status and years employed)
    if status == 'Contract':
        pay = '$' + str(randrange(25,40,5)) + '/hour'
    elif (thisYear - year) < 3:
        pay = '$' + str(randrange(60000, 70000, 5000))
    elif 2 <(thisYear - year) < 6:
        pay = '$' + str(randrange(70000, 90000, 5000))
    elif 5 <(thisYear - year) < 8:
        pay = '$' + str(randrange(95000, 115000, 5000))
    elif 7 <(thisYear - year) < 10:
        pay = '$' + str(randrange(120000, 140000, 5000))
    else:
        pay = '$' + str(randrange(160000, 500000, 20000))

    i += 1
    #print(str(employeeID) + ',' + name + ',' + division + ',' + str(year) + ',' + status + ',' + pay + '|')
    newFile.write(str(employeeID) + ',' + name + ',' + division + ',' + str(year) + ',' + status + ',' + pay + '|\n')
    newFile.truncate()
