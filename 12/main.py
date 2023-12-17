from functools import cache

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

@cache
def arrange(springs, counts):
    if not springs:
        return len(counts) == 0
                
    if not counts:
        return '#' not in springs
    
    result = 0

    if springs[0] in ".?":
        result += arrange(springs[1:], counts)

    if (
        springs[0] in "#?" 
        and counts[0] <= len(springs) and 
        "." not in springs[:counts[0]] 
        and (counts[0] == len(springs) or springs[counts[0]] != "#")
    ):
            result += arrange(springs[counts[0] + 1 :], counts[1:])

    return result

def main():
# Solution goes here
    inp = get_input()

    total = 0

    for line in inp:
        springs = line.split()[0]
        counts = [int(i) for i in line.split()[1].split(",")]
        
        total += arrange(springs, tuple(counts))

    print("1:", total)

    total = 0
    for line in inp:
        springs = ((line.split()[0] + "?") * 5)[:-1]
        counts = [int(i) for i in line.split()[1].split(",")] * 5
        
        total += arrange(springs, tuple(counts))
    
    print("2:", total)
    return

if __name__ == "__main__":
    main()