"""
Project due Friday 2/5
Design an optimal domain-Specific Hash Table
Stay within 60/60, aim for 75/75. (60% capacity of hash table is used) (i.e. if you have 300 elements,
180 spots are taken at least
World cities, US cities, CA cities
"""
import math

def readFile(filename):
    f = open(filename , "r")
    cities = []
    count = 0
    for line in f:
        line = line.strip()
        count += 1
        if count % 4 == 2: # and line not in cities:
            cities.append(line)
    return cities

"""
def hash_city(city):
    numVowels = 0
    for x in city:
        x = x.lower()
        if x in ["a" , "e" , "i" , "o" , "u" , "y"]:
            numVowels += 1
    return numVowels * len(city)
"""
def hash_city(city):
    numVowels = getNumVowels(city)
    sumVowelsSquared = getSumVowelPosSquared(city)
    middleChar = getMiddleCharacter(city)
    vowelDistance = getRepeatVowelDistances(city)
    temp = eachCharValued(city)
    return simpleChaos(city) % 300
    return abs(chaos(city)) % 300
    return ((((sumVowelsSquared + (numVowels ** 2)) + middleChar ** 2) + \
            vowelDistance) + temp) % 300

def chaos(city):
    sum = 0
    for x in xrange(len(city)):
        char = city[x]
        sum += int(math.sin(x) * 100) * (ord(char) - 97)
    return sum

#Trying to use O(1) to hash
def simpleChaos(city):
    sum = 0
    length = len(city)
    vowels = ["a" , "e" , "i" , "o" , "u" , "y" , "A" , "E" , "I" , "O" , "U" , "Y"]
    first = city[0]
    last = city[-1]
    middle = city[length / 2]
    strcombo = int(str(abs(ord(first) - 96)) + str(abs(ord(middle) - 96)) + str(abs(ord(last) - 96)))
    firstVal = 0
    secondVal = 0
    thirdVal = 0
    if first in vowels:
        firstVal = 1
    if middle in vowels:
        secondVal = 1
    if last in vowels:
        thirdVal = 1
    valcombo = int(str(firstVal) + str(secondVal) + str(thirdVal) , 2)
    return (int((ord(first) - 97)**2) + int((ord(middle) - 97)**2) + \
            int((ord(last) - 97)**2)) + length**2 + 2**valcombo + 2**strcombo
    

def getNumVowels(city):
    for x in city:
        x = x.lower()
        numVowels = 0
        if x in ["a" , "e" , "i" , "o" , "u" , "y"]:
            numVowels += 1
        return numVowels

def getSumVowelPosSquared(city):
    sumVowels = 0
    for x in xrange(len(city)):
        if city[x] in ["a" , "e" , "i" , "o" , "u" , "y"]:
            sumVowels += x ** 2
    return sumVowels

def getMiddleCharacter(city):
    pos = len(city) / 2
    return ord(city[pos]) - 97

def getRepeatVowelDistances(city):
    total = 0
    vowels = ["a" , "e" , "i" , "o" , "u" , "y"]
    usedVowelIndexes = []
    for x in xrange(len(city)):
        if city[x] in vowels:
            usedVowelIndexes.append(x)
    for x in xrange(0 , len(usedVowelIndexes) , 2):
        if not(x + 1 >= len(usedVowelIndexes)):
            total += 2 ** (usedVowelIndexes[x + 1] - usedVowelIndexes[x])
    return total

def eachCharValued(city):
    total = 0
    for x in city:
        total += 7**ord(x)
    return total

dictionary = dict()
cities = readFile("Cities.txt")
results = []
goodness = 0
for x in cities:
    hashCode = hash_city(x)
    if hashCode in dictionary:
        dictionary[hashCode].append(x)
    else:
        dictionary[hashCode] = [x]
    results.append(hashCode)

results.sort()
print results

spaceUsed = 0
for x in dictionary:
    spaceUsed += 1
print "Space used: " + str(spaceUsed)
print "Space Available: " + str(len(cities))
print "Efficiency: " + str(float(spaceUsed) / float(len(cities)))

print dictionary

"""
results.sort()
print results
for x in dictionary:
    print str(x) + str(dictionary[x])
"""

    
    
        
