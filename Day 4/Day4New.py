valids = 0
fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]

f = open("data.txt", mode='r')
for line in f.read().split("\n\n"):
    line = line.replace("\n", " ")
    if all(field + ":" in line for field in fields):
        valids+=1
print("num of valids = " + str(valids))