# results
# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

aboutMe = {}
aboutMe["firstName"] = "Joel"
aboutMe["age"] = 88
aboutMe["birthCty"] = "USA"
aboutMe["programming"] = "JavaScript"

for key, data in aboutMe.iteritems():
    #print key, data
    if key == "age":
        print "My age is ", data
    elif key == "firstName":
        print "My name is ", data
    elif key == "birthCty":
        print "My country of birth is ", data
    elif key == "programming":
        print "My favorite language is ", data


