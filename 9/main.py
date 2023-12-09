
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

def breakdown(pattern):
    new_pattern = []
    next_diff = 0
    for i in range(1, len(pattern)):
        new_pattern.append(pattern[i] - pattern[i-1])

    for i in new_pattern:
        if i != 0:
            return breakdown(new_pattern) + new_pattern[-1]
            
    return 0

def breakdown2(pattern):
    new_pattern = []
    next_diff = 0
    for i in range(1, len(pattern)):
        new_pattern.append(pattern[i] - pattern[i-1])

    
    for i in new_pattern:
        if i != 0:
            prev = new_pattern[0] - breakdown2(new_pattern)
            return prev
            
    return 0

def main():
    inp = get_input()
    patterns = []
    for i in inp:
        patterns.append([int(j) for j in i.split()])

    sum = 0
    for i in patterns:        
        sum += i[-1] + breakdown(i)

    print("1:", sum)

    sum = 0
    for i in patterns:
        sum += i[0] - breakdown2(i)
        
    print("2:", sum)
    return

if __name__ == "__main__":
    main()