student = {
	"first_name": "Randy",
	"last_name": "Ventura",
	"age": 67
}
print student["first_name"]
#This will print out the values
for item in student:
	print student[item]
#add more details
	print "Student ",item, student[item]


student = {
	"first_name": "Randy",
	"last_name": "Ventura",
	"age": [12,15,26,40,67]
}
print student["first_name"]
print student["age"][2] #selects 26 from the list

#This will print out the values
for item in student:
	print student[item]
#add more details
	print "Student ",item, student[item]


# FUNCTIONS
#def = definition

def ourFunction():
	print "hello"

ourFunction();

# to make this print multiple times - the \n makes a line break
def ourFunction2(num):
	print "hello\n" * num

ourFunction2(5);

# I thought of using a for loop myself -

for number in range(10):
	ourFunction();


i,j = (1,2), [3,4]
#i[0] = 42  this line would cause an error because truples are emurable
j[0] = 42
print i[1] + j[1]
