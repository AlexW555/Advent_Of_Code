#Function that Reads in the data and formats it to be computable
def readSeats():
    with open("data.txt", 'r') as f:
        return f.read().splitlines()

#Here we convert the F,B,L,R into their retrospective binary objects F -> 0
# BFBBBFFLRR -> 1011100011
# we convert it into a int with base 2
def getSeatLocation(seat):
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
    return row, col

#Formula for finding out seatId From the instructions
def getSeatID(seat):
    row, col = getSeatLocation(seat)
    return row * 8 + col

#Using this we search through seats, find the seatId of each seat and then compare to
#The max seat value
def part1(seats):
    maxVal = 0
    for seat in seats:
        seatID = getSeatID(seat)

        if seatID > maxVal:
            maxVal = seatID
    return maxVal

#Here we are trying to find the missing seat value in the set. Ignoring the top end and the bottom end
#To do this we use part 1's max value list for all the possible seats. Then for every seat we come across we remove it
def part2(seats):
    unseen = list(range(part1(seats) + 1))
    for seat in seats:
        unseen.remove(getSeatID(seat))
    return unseen[-1]

#Main function
def main():
    seats = readSeats()
    print(f"Part 1: {part1(seats)}\nPart 2: {part2(seats)}")

main()