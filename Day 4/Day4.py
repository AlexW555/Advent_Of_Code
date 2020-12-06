valids = 0
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
file = open('data.txt', mode='r')
for line in file.read().split("\n\n"):
    print(line)
    line = line.replace("\n", " ")
    if all(key + ":" in line for key in keys):
        print("\nnew line = " + line)
        valids+=1
print("Number of Valid Passports" + valids)