import time

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

def find_prev_map(inp, line):
    end_line = line
    while inp[line] != '':
        line -= 1
    
    return inp[line + 2: end_line+1], line - 1

def find_prev_number(map, seed):
    for i in map:
        arr = [int(j) for j in i.split()]
        if arr[0] <= seed < arr[0] + arr[2]:
            return seed - arr[0] + arr[1]
    return seed


def find_next_map(inp, line):

    start_line = line
    while inp[line] != '':
        line += 1

    return inp[start_line + 1:line], line + 1

def find_next_number(map, seed):
    for i in map:
        arr = [int(j) for j in i.split()]
        if arr[1] <= seed < arr[1] + arr[2]:
            return seed - arr[1] + arr[0]
    return seed

def is_seed_in_values(seeds, seed):
    for start,length in seeds:
        if start <= seed < start + length:
            return True
    return False

def main():

    inp = get_input()

    seeds = [int(i) for i in inp[0].split()[1:]]

    min_seed = 100000000000
    for seed in seeds:
        curr_seed = seed
        line = 2
        while line < len(inp) - 2:
            map, line = find_next_map(inp, line)  
            curr_seed = find_next_number(map, curr_seed)
            
        min_seed = min(curr_seed, min_seed)

    print("1:", min_seed)


    seed_ranges = []    
    sum = 0
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))

    start = time.perf_counter()    
    count = 0
    for seed in range(0, 141314689):
        if seed % 1000000 == 0:
            print(seed)
        curr_seed = seed
        line = len(inp) - 1
        while line > 1:
            map, line = find_prev_map(inp, line)  
            curr_seed = find_prev_number(map, curr_seed)
            
        if is_seed_in_values(seed_ranges, curr_seed):
            print("2:", seed)
            print("Time (sec):", time.perf_counter() - start)
            break
        
    return

if __name__ == "__main__":
    main()