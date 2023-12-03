# This doesn't work if one part has the same number in multiple places
# due to the use of sets in find_numbers. Luckily, not a problem today.

nums_str = '0123456789'

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp

def find_full_number(x, y, inp):
    # find the left edge of the number
    while x - 1 >= 0 and inp[y][x - 1] in nums_str:
        x -= 1

    min_x = x
    # find the right edge of the number
    while x + 1 < len(inp[1]) and inp[y][x + 1] in nums_str:
        x += 1
    
    return int(inp[y][min_x:x + 1])

def find_numbers(x, y, inp, part2=False):
    surrounds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    sum_set = set()

    for y_delta, x_delta in surrounds:
        if inp[y + y_delta][x + x_delta] in nums_str:
            sum_set.add(find_full_number(x + x_delta, y + y_delta, inp))

    if part2 and inp[y][x] == '*' and len(sum_set) == 2:
        num1 = sum_set.pop()
        num2 = sum_set.pop()
        return num1 * num2
    
    elif part2:
        return 0
    
    return sum(list(sum_set))

def main():

    inp = get_input()

    parts = []

    parts_list = '!@#$%^&*(){}[]/?=+\|-_;:\'\",<>'

    for y, line in enumerate(inp):
        for x, chr in enumerate(line):
            if inp[y][x] in parts_list:
                parts.append((x, y))
                             
    sum = 0
    for x,y in parts:
        sum += find_numbers(x, y, inp)

    print("1:", sum)

    sum = 0
    for x,y in parts:
        sum += find_numbers(x, y, inp, True)

    print("2:", sum)

if __name__ == "__main__":
    main()