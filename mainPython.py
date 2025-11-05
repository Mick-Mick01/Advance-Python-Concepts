# Checking if list and dictionaries are mutable or not. We have already seen that list are mutable in out projects

myDict = {
    "name":"Dev",
    "age":45
}
myLis = ['d', 'd', 'y', 'e']


# I WILL LEARN ALL THE FUNCTONS APPLICABLE TO A DICTIONARY LATER ON-!!
def myFunc(myDict):
    for key, value in myDict.items():
        myDict[key] = "Harry"

def myFunc2(lis):
    for i in range(len(lis)):
        lis[i] = 'a'

myFunc(myDict)
print(myDict)
myFunc2(myLis)
print(myLis)