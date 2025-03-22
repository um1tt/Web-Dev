n = int(input()) 
arr = input().split()

positive_count = 0

for i in range(n):
    if int(arr[i]) > 0:  
        positive_count += 1

print(positive_count)
