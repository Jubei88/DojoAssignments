
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(arr1, arr2):
  new_dict = {}
  zipList = zip(arr1, arr2)
  new_dict = dict(zipList)
  # your code here
  return new_dict

print make_dict(name, favorite_animal);

