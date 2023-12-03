
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():
# Solution goes here

    inp = get_input()

    maxes = {"blue": 14, "red": 12, "green": 13}

    losers = set()
    for i in inp:
        game = i.split(":")
        pulls = game[1].split(";")
        for j in pulls:
            pieces = j.split(",")
            for k in pieces:
                counts = k.strip().split(" ")
                if maxes[counts[1]] < int(counts[0]):
                        losers.add(int(game[0].split(" ")[1]))
                        break

    all = range(1,len(inp)+1,1) 
    all_s = set(all)

    possible = all_s - losers

    print(sum(possible))

    

    powers = 0
    for i in inp:
        mins = {"blue": 0, "red": 0, "green": 0}
        game = i.split(":")
        pulls = game[1].split(";")
        for j in pulls:
            pieces = j.split(",")
            for k in pieces:
                counts = k.strip().split(" ")
                if mins[counts[1]] < int(counts[0]):
                    mins[counts[1]] = int(counts[0])
        powers += mins['red'] * mins['blue'] * mins['green']

    print(powers)
if __name__ == "__main__":
    main()