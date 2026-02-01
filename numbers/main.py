import random
def random_number():
    numbers = []
    for i in range(3, 21):
        numbers.append(i)
    a = random.choice(numbers)
    return a
a = random_number()
print(a)
res = ""
for i in range(1, a//2 + 1):
    for j in range(i, a+1):
        if a % (i + j) == 0 and i != j:
            print(i, j)
            x = str(i) + str(j)
            res += x
print(res)