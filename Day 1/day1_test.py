#Reading in the numbers from text file
f = open("expenses.txt", "r")
numbers = [int(x) for x in f.readlines()]
f.close()
print(numbers)

#Brute Force
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print("found, It's " + str(i) + "and" + str(j) + "and" + str(k))
      
#HashTable
hashTable = {}
for i in range(len(numbers)):
  complement = 2020 - numbers[i]
  if complement in hashTable:
    print("Pair with sum", 2020,"is: (", numbers[i], ",",complement,")")
  hashTable[numbers[i]] = numbers[i]
