from collections import deque
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

directions = {"U": (0, -1),"R": (1, 0),"D": (0, 1),"L": (-1, 0)}
directions_arr = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def print_field(ss, fs, ts, lx, mx, ly, my):
    with open("test.txt", 'w') as f:
        f.write("----------------------------------------\n")
        for y in range(ly, my):
            for x in range(lx, mx):
                if (x,y) in fs:
                    f.write("#")
                elif (x,y) in ts:
                    f.write("*")
                elif (x,y) in ss:
                    f.write("s")
                else:
                    f.write(".")
            f.write("\n")

def fill_count(search_set, field, min_x, max_x, min_y, max_y):
    enclosed_set = set()
    unenclosed_set = set()
    while len(search_set):
        temp_set = set()
        left_to_check = deque()
        left_to_check.append(search_set.pop())
        enclosed = True
        while len(left_to_check):
            curr_x, curr_y = left_to_check.popleft()
            temp_set.add((curr_x, curr_y))
            for dx, dy in list(directions.values()):
                new_x = curr_x + dx
                new_y = curr_y + dy
                if new_x not in range(min_x, max_x) or new_y not in range(min_y, max_y):
                    enclosed = False
                elif (new_x, new_y) not in temp_set and (new_x, new_y) not in field:
                    temp_set.add((new_x, new_y))
                    left_to_check.append((new_x, new_y))

            
        if not enclosed:
            unenclosed_set = unenclosed_set.union(temp_set)
            search_set = search_set.difference(unenclosed_set)
        else:
            enclosed_set = enclosed_set.union(temp_set)
            search_set = search_set.difference(enclosed_set)
        print_field(search_set, field, enclosed_set, min_x, max_x, min_y, max_y)
    
    return len(enclosed_set) + len(field)


def partOne():
    inp = get_input()

    field = set()
    loc = (0,0)
    field.add(loc)
    max_x = 0
    min_x = 10000000
    max_y = 0
    min_y = 10000000
    for line in inp:
        dir, dist, color = line.split()
        for i in range(int(dist)):
            loc = (loc[0] + directions[dir][0], loc[1] + directions[dir][1])
            field.add(loc)
            max_x = max(loc[0], max_x)
            max_y = max(loc[1], max_y)
            min_x = min(loc[0], min_x)
            min_y = min(loc[1], min_y)
    
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    search_set = set()
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if (x,y) not in field:
                search_set.add((x,y))

    print("Part One:", fill_count(search_set, field, min_x, max_x, min_y, max_y)) #3152 - too low


def partTwo():

    inp = get_input()

    loc = (0,0)
    field = list()
    field.append(loc)
    perimeter = 0

    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for line in inp:
        _, _, color = line.split()
        steps = int(color[2:7], base=16)
        perimeter += steps
        loc = (loc[0] + dirs[int(color[-2])][0] * steps, loc[1] + dirs[int(color[-2])][1] * steps)
        field.append(loc)

    sum_xy = 0
    sum_yx = 0
    for i, curr_point in enumerate(field[:-1]):
        sum_xy += curr_point[0] * field[i+1][1]
        sum_yx += curr_point[1] * field[i+1][0]
    
    print("Part Two:", abs((sum_xy - sum_yx)//2) + perimeter//2 + 1) # 147839462116154 too low
    

def main():
# Solution goes here
    partOne()
    partTwo()

if __name__ == "__main__":
    main()