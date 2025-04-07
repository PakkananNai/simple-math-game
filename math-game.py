import random

a = random.randint(1, 99)
b = random.randint(1, 99)
oj = random.choice(["+", "-", "*", "/"])
point = 0

if oj == "+":
    c = a + b
elif oj == "-":
    c = a - b
elif oj == "*":
    c = a * b
else:
    c = a / b

while True:
    print(f"{a} {oj} {b} = ?")
    ans = float(input())
    if ans == c:
        print("Correct!")
        point += 1
    elif ans != 0:
        print("Incorrect! The answer is", c)
        print("Your point is", point)
        break

