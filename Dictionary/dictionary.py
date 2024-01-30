# How to create a dictionary?
# dictionaries are an unordered collection hence they may not print out the same way 
# you initialized them  

myDict = dict()
print(myDict)

secondDict = {}
print(secondDict)

engToSpanish = {"one": "uno", "two": "dos", "three": "tres"} 
print(engToSpanish) 
print(engToSpanish["one"]) 
# print(engToSpanish["four"]) gives a KeyError

# Accessing a value from a dictionary takes O(1) Time Complexity

# Update / add an element to the dictionary
# Time and space complexity - O(1)

myDict = {'name': 'John', 'age': 22}
print(myDict) 
myDict["age"] = 23
print(myDict) 

# adding
# Time - O(1)
# Space Complexity - amortized O(1) - because at some point it may be O(n) it's kinda dynamic
myDict['address'] = 'Kampala'
print(myDict) 

# Traversing through a dictionary
# Time Complexity - O(n) where n is the number of elements in the dictionary
# Space Complexity - O(1)

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
        
traverseDict(myDict)

# How to find an element in a dictionary
# Time Complexity - O(n)
# Space Complexity - O(1)
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            # return key, value
            return True
    return "The value does not exist"
            
print(searchDict(myDict, 23)) # returns True
print(searchDict(myDict, 45)) # returns The value does not exist

# Delete an element from a dictionary
# Time Complexity - O(1) but is O(n) in amortized worst case
# Space complexity - O(1)

print(myDict.pop('name'))
print(myDict)
print(myDict.popitem()) # returns an arbitrary value, after deleting it
print(myDict)
myDict.clear() # delete all elements from the dictionary
print(myDict)

myDict = {'name': 'Emma', 'age': 22}

del myDict['age']
print(myDict)

# DICTIONARY METHODS

myDict = {'name': 'John', 'age': 22, 'address': 'London', 'education': 'master'}

# myDict.clear() clears the entire dictionary

dict = myDict.copy()
print(myDict)
print(dict)

newDict = {}.fromkeys([1, 2, 3], 0)
# newDict = {}.fromkeys([1, 2, 3]) values by default assigned to None
print(newDict)

# dictionary.get(key, value) second parameter is the value to return if key is not found
print(myDict.get('age', 27))

print(myDict.items()) # returns a list of dictionary key and pairs tuple pairs
print(myDict.keys()) # returns a list of dictionary keys
print(myDict.popitem()) # returns and removes an arbitrary element from the dictionary
print(myDict)

# setdefault returns the value of the key if key is in the dictionary, if not it inserts the default value to insert in the dictionary
print(myDict.setdefault('name1', 'added'))
print(myDict)

print(myDict.pop('name1', 'not')) # removes and returns an element from the dictionary having a given key, not is default value to return

print(myDict.values()) 

# update method adds elements to the dictionary if the key is in the dictionary, else it updates the values of the specified keys

newDict = {'a' : 1, 'b' : 2, 'c' : 3}
myDict.update(newDict)
print(myDict)


# OPERATIONS AND BUILT IN FUNCTIONS

myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuarto'}

print('uno' in myDict.values()) # Time Complexity for in operator is O(1)

# Time Complexity - O(n)
for key in myDict:
    print(key, myDict[key])
    
myDict = {1: True, 2: True}
print(all(myDict))
print(any(myDict))

myDict = {1: 'True', 2: 'True'}
print(all(myDict))
print(any(myDict))

myDict = {0: False, 1: False}
print(all(myDict))
print(any(myDict))

myDict = {0: True, 1: False, 2: False}
print(all(myDict))
print(any(myDict))

newDict = {}
print(all(newDict))
print(any(newDict))

print(len(myDict))

myDict = {'e': 1, 'a': 2, 'u': 3, 'o' : 4, 'i' : 5}

print(sorted(myDict))
print(sorted(myDict, reverse= True))

myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo' : 4, 'werwi' : 5}

print(sorted(myDict, key=len))
