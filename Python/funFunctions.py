def odd_even(top):
    for num in range(0, top):
        if num % 2 == 1:
            print "Number is " + str(num) + ". This is an odd number."
        else:
            print "Number is %d. This is an even number." % num  # an interesting option to the str() variation


# print odd_even(20)

a = [2, 4, 10, 16]


def multiply(a, num):
    for j in a:
        by5 = j * num
        print by5


# print multiply(a, 5)


# Still not working... this version from someone else git
# def layered_multiples(arr):
#     new_array = []
#     for idx in range(0, len(arr)):
#         twoDlist = []
#         for num in range(0, arr[idx]):
#             twoDlist.append(1)
#             if num == arr[idx] - 1:
#                 new_array.append(twoDlist)
#     return new_array
#
#
# x = layered_multiples(multiply([2, 4, 5], 3))
# print x

def twodimlist(list):
    new_array = []
    for number in range(0, len(list)):
        value = list[number]
        for idx in range(0, value):
            new_array.append(1)
            # return new_array
            # print new_array


x = twodimlist([2, 4, 5])
x = twodimlist(multiply([2, 4, 5], 3))
print x
