with open("password_list.txt") as file:
    #Makes list of 'line' strings
    lines=file.readlines()


count = 0
for line in lines:
    #Split string into list
    obj=line.split()

    #Get letter indexes 0-indexing artifcially adds 1 to index
    indexes = list(map(int,obj[0].split('-')))
    start= indexes[0]-1
    end= indexes[1]-1

    #get the string and the letter being tested
    string=obj[2]
    test_letter=obj[1].replace(':','')

    #Test for hits

    #if start == test_letter ^^ end
    same = [string[0] == letter for letter in string]

    print(string)

    #Only one letter match if uou read the instructions which I did not
    if sum(same) == 1:
        count+=1

print(count)