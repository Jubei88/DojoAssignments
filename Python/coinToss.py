# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
#
# Hint: Use the python built-in round function to convert that floating point number into an integer
#
# x = .23945593
# x_rounded = round(x)

import random


def coinToss(tosses):
    count = 1
    heads = 0
    tails = 0
    for num in range(tosses):
        num += 1
        random_num = random.randint(1, 2)
        if random_num == 1:
            heads += 1
            # print "Thru a heads " , heads , " times"
            print "Attempt # %d: Throwing a coin... It's a head! ... Got" % num, heads, "head(s) so far and", tails, "tail(s) so far"
        elif random_num == 2:
            tails += 1
            # print "Thru a tails " , tails , " times"
            print "Attempt # %d: Throwing a coin... It's a tail! ... Got" % num, heads, "head(s) so far and", tails, "tail(s) so far"


coinToss(10);
