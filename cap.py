#code to make sure text is lower case and capitalized
lNameList = open('lastnames.txt', 'r+')
temp = lNameList.read().split()
lNameList.seek(0)
for i in range(len(temp)):
    lNameList.write(temp[i].lower() + '\n')
    lNameList.truncate()

lNameList.seek(0)
for i in range(len(temp)):
    lNameList.write(temp[i].capitalize() + '\n')
    lNameList.truncate()



