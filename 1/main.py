
def get_input():
    inp = []
    with open("input.txt") as f:
        return f.readlines()


numbers = '0123456789'

inp = get_input()
sum = 0
for i in inp:
    first = -1
    last = -1
    for j in i:
        if j in numbers:
            if first == -1:
                first = int(j)
            last = int(j)
    sum += first * 10 + last
print("1:", sum)

strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum2 = 0
for i in inp:
    first = -1
    last = -1
    for x, j in enumerate(i):
        if j in numbers:
            if first == -1:
                first = int(j)
            last = int(j)
        else:
            for k in strs:
                if i[x:].startswith(k):
                    if first == -1:
                        first = strs.index(k) + 1
                    last = strs.index(k) + 1
                    
    sum2 += first * 10 + last

print("2:", sum2)


