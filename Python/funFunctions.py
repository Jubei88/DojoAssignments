def odd_even(top):
    for num in range(0, top):
        if num % 2 == 1:
            print "Number is " + str(num) + ". This is an odd number."
        else:
            print "Number is " + str(num) + ". This is an even number."


# odd_even(200);

a = [2, 4, 10, 16]


def multiply(a, num):
    for j in a:
        by5 = j * num
        print by5


# multiply(a, 5);


def layered_multiples(arr, num):
    new_array = []
    # your code here
    for a in arr:
        j = a * num
        new_array.append("1" * j)
    return new_array

x = layered_multiples(multiply([2, 4, 5], 3))
print x

# output
# [[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
