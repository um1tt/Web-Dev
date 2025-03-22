a = int(input())
b = int(input())

for i in range(int(a ** 0.5), int(b ** 0.5) + 1):
    square = i * i
    if a <= square <= b:
        print(square, end=" ")
