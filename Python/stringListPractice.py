str = "It's thanksgiving day. It's my birthday,too!"
print str

print(str[18:21])
#or
print(str.find("day"))

print(str.replace("day ", "month"))


# Min and Max
x = [2,54,-2,7,12,98]
print "Smallest value of list x :", min(x)
print "Largest value of list x :", max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
firstWord = x[0]
print firstWord
lastWord = x[-1]
print lastWord
newList = []
#newList.extend((firstWord , lastWord))
#or
newList.append(firstWord)
newList.append(lastWord)
print newList


#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
half = len(x)/2
secondHalf = len(x) - half
short = []
short = x[:half]
print short
newX = x[secondHalf:]
print "new list", newX
newX.insert(0, short)
print newX