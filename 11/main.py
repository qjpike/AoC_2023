from collections import deque

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():

    inp = get_input()

    galaxies = deque()
    blank_horiz = set()
    blank_vert = set()
    for y, line in enumerate(inp):
        if len(set(line)) == 1:
            blank_horiz.add(y)
        for x, loc in enumerate(line):
            if loc == "#":
                galaxies.append((x,y)) 

    arr = list(map(list, zip(*inp)))
    for x, line in enumerate(arr):
        if len(set(line)) == 1:
            blank_vert.add(x)

    remaining_galaxies = deque(galaxies)

    count1 = 0
    count2 = 0
    part2_scalar = 999999
    while len(remaining_galaxies):
        curr_galaxy = remaining_galaxies.popleft()
        for dest_galaxy in remaining_galaxies:
            vert_crosses = blank_vert.intersection(range(min(curr_galaxy[0], dest_galaxy[0]), max(curr_galaxy[0], dest_galaxy[0])))
            horiz_crosses = blank_horiz.intersection(range(min(curr_galaxy[1], dest_galaxy[1]), max(curr_galaxy[1], dest_galaxy[1])))

            count1 += abs(curr_galaxy[0] - dest_galaxy[0]) + abs(curr_galaxy[1] - dest_galaxy[1]) + len(vert_crosses) + len(horiz_crosses)
            count2 += abs(curr_galaxy[0] - dest_galaxy[0]) + abs(curr_galaxy[1] - dest_galaxy[1]) + len(vert_crosses)*part2_scalar + len(horiz_crosses)*part2_scalar
            
    print("1:", count1)
    print("2:", count2)
    return

if __name__ == "__main__":
    main()