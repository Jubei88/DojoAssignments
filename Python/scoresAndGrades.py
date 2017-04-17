# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
#
# * Score: 60 - 69; Grade - D
# * Score: 70 - 79; Grade - C
# * Score: 80 - 89; Grade - B
# * Score: 90 - 100; Grade - A

import random

for num in range(10):
    random_num = random.randint(60, 100)
    # print random_num
    if random_num > 59 and random_num < 70:
        print "* Score: %d; Grade - D" % random_num
    elif 10 <= random_num <= 79:
        print "* Score: %d; Grade - C" % random_num
    elif 80 <= random_num <= 89:
        print "* Score: %d; Grade - B" % random_num
    elif 90 <= random_num <= 100:
        print "* Score: %d; Grade - A" % random_num
