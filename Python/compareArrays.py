sa_list_one = [1, 2, 5, 6, 2]
sa_list_two = [1, 2, 5, 6, 2]

sb_list_one = [1, 2, 5, 6, 5]
sb_list_two = [1, 2, 5, 6, 5, 3]

sc_list_one = [1, 2, 5, 6, 5, 16]
sc_list_two = [1, 2, 5, 6, 5]

sd_list_one = ['celery', 'carrots', 'bread', 'milk']
sd_list_two = ['celery', 'carrots', 'bread', 'cream']

def evalList(listOne, listTwo):
    if listOne == listTwo:
        print "So far so good"
    else:
        print "the list are not a match"


evalList(sb_list_one, sb_list_two);