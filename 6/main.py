
def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():
# Solution goes here

    times = [int(i) for i in get_input()[0].split()[1:]]
    distances = [int(i) for i in get_input()[1].split()[1:]]

    total = 1
    for i in range(len(times)):
        t = times[i]
        d = distances[i]

        count = 0
        for j in range(t + 1):
            speed = j
            dist = (t - j) * j

            if dist > d:
                count += 1
        
        total *= count
    print("1:", total)

    count = 0
    for i in range(61709067):
        speed = i
        dist = (61709066 - i) * i

        if dist > 643118413621041:
            count += 1

    print("2:", count)

    
    return

if __name__ == "__main__":
    main()