ourList = ["Martin", "Michael"]

for val in enumerate(ourList):
	print val

for idx,value in enumerate(ourList):
	print value,idx



name = {"sw": "Sara Wong", "mp":"Martin Puryear"}
for key,value in name:
	print key, value

# when the value is added python will try to unpack the keywords

name2 = {"sw": "Sara Wong", "mp":"Martin Puryear"}
for key in name2.items():
	print key

#items is a method of dictionary - it prints the key and value of a tuple

# to unpack the tuple - add a second variable
name2 = {"sw": "Sara Wong", "mp":"Martin Puryear"}
for key, bacon in name2.items():
	print key, bacon