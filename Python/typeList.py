listOne = ['magical unicorns',19,'hello',98.98,'world']
listTwo = [2,3,1,7,4,12]
listThree = ['magical','unicorns']

floater = 5.5
numSum = []
fullString = ""

for item in listOne:
    if type(item) is int or type(item) is float:
        # print item, " is number"
        numSum.append(item)
        # print numSum
    elif type(item) is str:
        # print item , " is string"
        fullString += item + " "
numList = len(numSum)

# print numList

if numList > 0 and fullString != "":
    print "mix of data types"
    print numSum
    print fullString
if numList > 0 and fullString == "":
    print " all numbers"
    print sum(numSum)
if numList is 0 and fullString != "":
    print "Just string"
    print fullString

