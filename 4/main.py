
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():

    inp = get_input()
    sum_1 = 0

    i = [(k,1) for k in range(1,len(inp)+1)]
    counts = dict(i)

    for idx, i in enumerate(inp):
        winning_nums_set = set([int(j) for j in i.split(":")[1].split("|")[0].strip().split()])
        # winning_nums_set = set()
        # for j in winning_nums_arr:
        #     winning_nums_set.add(int(j))
        my_nums_arr = i.split(":")[1].split("|")[1].split()
        my_nums_set = set()
        for j in my_nums_arr:
            my_nums_set.add(int(j))
        wins = my_nums_set.intersection(winning_nums_set)
        if len(wins) > 0:
            sum_1 += pow(2, len(wins)-1)

            for z in range(idx + 2,idx + len(wins) + 2):
                counts[z] += 1 * counts[idx+1]

    print("1:", sum_1)
    print("2:", sum(counts.values()))

if __name__ == "__main__":
    main()