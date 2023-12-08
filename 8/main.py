import math

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():
    inp = get_input()

    dirs = inp[0].strip()

    nodes = dict()
    for i in inp[2:]:
        line = i.split()
        nodes[line[0].strip()] = (line[2][1:-1], line[3][:-1])
    
    idx = 0
    curr_node = 'AAA'
    count = 0
    while curr_node != 'ZZZ':
        if dirs[idx%len(dirs)] == 'L':
            curr_node = nodes[curr_node][0]
        else:
            curr_node = nodes[curr_node][1]
        idx += 1
    print("1:", idx)

    # want the least common multiple of all paths from XXA to XXZ
    starts = []
    for i in nodes.keys():
        if i[-1] == "A":
            starts.append(i)

    ans = 1
    for i in starts:
        curr_node = i
        idx = 0
        while curr_node[-1] != 'Z':
            if dirs[idx % len(dirs)] == "L":
                curr_node = nodes[curr_node][0]
            else:
                curr_node = nodes[curr_node][1]
            idx += 1
        ans = math.lcm(ans, idx)
        
    print("2:", ans)

if __name__ == "__main__":
    main()