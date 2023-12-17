from collections import deque

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

collisions = {("\\", 0): [3], 
              ("\\", 1): [2],
              ("\\", 2): [1],
              ("\\", 3): [0],
              ("/",  0): [1],
              ("/",  1): [0],
              ("/",  2): [3],
              ("/",  3): [2],
              ("|",  0): [0],
              ("|",  1): [0, 2],
              ("|",  2): [2],
              ("|",  3): [0, 2],
              ("-",  0): [1, 3],
              ("-",  1): [1],
              ("-",  2): [1, 3],
              ("-",  3): [3],
              (".",  0): [0],
              (".",  1): [1],
              (".",  2): [2],
              (".",  3): [3]
              }

def bound_check(loc, max_x, max_y):
    return 0 <= loc[0] < max_x and 0 <= loc[1] < max_y

def shine(loc, dir, max_x, max_y, field):
    next_beams = deque()
    visited = set()
    cur_loc = loc
    next_beams.append((cur_loc, dir))
    while next_beams:
        cur_loc, dir = next_beams.pop()
        next_loc = (cur_loc[0] + directions[dir][0], cur_loc[1] + directions[dir][1])
        if bound_check(next_loc, max_x, max_y) and (next_loc, dir) not in visited:
            visited.add((next_loc, dir))
            for res in collisions[(field[next_loc], dir)]:
                next_beams.append((next_loc, res))
    
    visited_raw = set()
    for loc, dir in list(visited):
        visited_raw.add(loc)

    return len(visited_raw)

def main():
# Solution goes here

    inp = get_input()
    field = dict()

    max_y = len(inp)
    max_x = len(inp[0])

    for y, line in enumerate(inp):
        for x, tile in enumerate(line):
            field[(x, y)] = tile

    print(shine((-1, 0), 1, max_x, max_y, field))

    starts = []
    starts.extend( [ ((-1, i), 1)    for i in range(0, max_y) ] )
    starts.extend( [ ((i, -1), 2)    for i in range(0, max_x) ] )
    starts.extend( [ ((max_x, i), 3) for i in range(0, max_y) ] )
    starts.extend( [ ((i, max_y), 0) for i in range(0, max_x) ] )

    biggest = 0
    for loc, dir in starts:
        biggest = max(shine(loc, dir, max_x, max_y, field), biggest)  

    print(biggest) #8695 too low

if __name__ == "__main__":
    main()