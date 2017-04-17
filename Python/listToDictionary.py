
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(arr1, arr2):
  new_dict = {}
  zipList = zip(arr1, arr2)
  new_dict = dict(zipList)
  # your code here
  return new_dict

#print make_dict(name, favorite_animal);

# print len(arr1)

def makeDict(arr1, arr2):
    newDict = {}
    for i in range(len(arr1)):
        newDict[arr1[i]] = arr2[i]
    return newDict
print makeDict(name, favorite_animal);