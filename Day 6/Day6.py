#Function that Reads in the data and formats it to be computable
#abc = one persons answers
#
#askd = 
#ldk = two person in groups answers
def readAnswers():
    with open('/Users/alexwing/Desktop/Advent_Of_Code/Day 6/data.txt', mode='r') as f:
        return f.read().split("\n\n")

#Using a set for this as duplicate as we are counting how many yes's we are requiring
#across the group for all answers. For this a set doesnt contain duplicates so we can count each
# Groups answers in a set.
def part1(answers):
    count = 0
    for answer in answers:
        group = set("".join(answer.split())) 
        count += len(group)
    return count

#Had to follow a youtube tutorial for this. Advanced lists and sets
def part2(answers):
    count = 0
    for answer in answers:
        people = list(map(set, answer.split("\n")))
        #print(people)
        count += len(people[0].intersection(*people[1:]))
    return count

#Main function
def main():
    answers = readAnswers()
    print(f"Part 1: {part1(answers)}\nPart 2: {part2(answers)}")

main()
