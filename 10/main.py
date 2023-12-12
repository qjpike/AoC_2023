from collections import deque

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp
# Moves           Type   N  E  S  W
tile_alignment = {"|" : (1, 0, 1, 0),
                  "-" : (0, 1, 0, 1),
                  "L" : (1, 1, 0, 0),
                  "J" : (1, 0, 0, 1),
                  "7" : (0, 0, 1, 1),
                  "F" : (0, 1, 1, 0),
                  "." : (0, 0, 0, 0),
                  "S" : (1, 1, 1, 1)}

tile_fill =      {"|" : ("|", " ", "|", " "),
                  "-" : (" ", "-", " ", "-"),
                  "L" : ("|", "-", " ", " "),
                  "J" : ("|", " ", " ", "-"),
                  "7" : (" ", " ", "|", "-"),
                  "F" : (" ", "-", "|", " ")}

#                N       E       S        W
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

def move(heading, leaving, destination):
    return tile_alignment[leaving][heading] and tile_alignment[destination][(heading + 2) % 4]

def part1(inp):
    starts = deque()
    field = dict()
    for y, i in enumerate(inp):
        for x, j in enumerate(i):
            field[(x,y)] = j
            if j == "S":
                starts.append((x, y, 0))

    field_dists = dict()
    
    while len(starts):
        curr_x, curr_y, dist = starts.popleft()

        for move_dir in range(len(directions)):
            next_pos = (curr_x + directions[move_dir][0], curr_y + directions[move_dir][1])

            if not (0 <= next_pos[0] < len(inp[0]) and 0 <= next_pos[1] < len(inp)):
                continue
            
            # see if it's worth trying the step
            if next_pos in field_dists and dist + 1 > field_dists[next_pos]:
                continue

            # Try the step
            if move(move_dir, field[(curr_x, curr_y)], field[next_pos]):
                starts.append((next_pos[0], next_pos[1], dist + 1))
                field_dists[next_pos] = dist + 1

    print("1:", max(field_dists.values()))

    return field, field_dists

def main():
    inp = get_input()
    field, field_dists = part1(inp)
                
    new_field = dict()
    
    for curr_x, curr_y in field_dists.keys():
        new_field[(curr_x * 2, curr_y * 2)] = field[(curr_x, curr_y)]
        for idx, dloc in enumerate(directions):
            dx, dy = dloc
            if field[(curr_x, curr_y)] == "S":
                continue
            new_x = curr_x * 2 + dx
            new_y = curr_y * 2 + dy
            new_fill = tile_fill[field[(curr_x, curr_y)]][idx]
            if  new_fill != ' ':
                new_field[(new_x, new_y)] = new_fill

    max_x = len(inp[0]) * 2
    max_y = len(inp) * 2
    search_set = set()
    for y in range(max_y):
        for x in range(max_x):
            if (x,y) not in new_field:
                search_set.add((x,y))

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
            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy
                if new_x not in range(max_x) or new_y not in range(max_y):
                    enclosed = False
                elif (new_x, new_y) not in temp_set and (new_x, new_y) not in new_field:
                    temp_set.add((new_x, new_y))
                    left_to_check.append((new_x, new_y))

        if enclosed == False:
            unenclosed_set = unenclosed_set.union(temp_set)
            search_set = search_set.difference(unenclosed_set)
        else:
            enclosed_set = enclosed_set.union(temp_set)
            search_set = search_set.difference(enclosed_set)

    count = 0
    for x,y in list(enclosed_set):
        if x % 2 == 0 and y % 2 == 0:
            count += 1
    print("2:", count) 


if __name__ == "__main__":
    main()