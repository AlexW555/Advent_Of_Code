# from collections import Counter
# too_short = 0
# too_long = 0
# passed_passwords = 0

with open("password_list.txt") as file:
    #Makes list of 'line' strings
    lines=file.readlines()


count = 0
for line in lines:
    #Split string into list
    obj=line.split()

    #Get a list of acceptable character frequencies in string, assing obj[0]
    start_end_int=list(map(int,obj[0].split('-')))
    obj[0]=list(range(start_end_int[0],start_end_int[1]+1))

    #format string character for searching
    obj[1]=obj[1].replace(':','')

    #See if letter frequency is acceptable
    if obj[2].count(obj[1]) in obj[0]:
        count+=1

print(count)
#
#
#     passwords = [str(x) for x in file.readlines()]
#
#     for i in passwords:
#         words = i.split()
#         Min = words[0]
#         Max = i[2]
#         Letter = i[4]
#
#         password = words[-1]
#
#         print(Min,Max,Letter, password)
#         count = 0
#
#         Count = Counter(c for c in password if c in Letter)
#         for value, count in Count.most_common():
#             print(count)
#         if count < int(Min):
#             print("Failed to meet minimum Count")
#             too_short += 1
#         elif count > int(Max):
#             print("Failed due to Max Count")
#             too_long += 1
#         else:
#             print("passed")
#             passed_passwords += 1
#
# print("The number of too short passwords was " + str(too_short))
# print("The number of too long passwords was " + str(too_long))
# print("The number of valid passwords was " + str(passed_passwords))