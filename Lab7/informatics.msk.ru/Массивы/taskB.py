N = int(input())  
arr = [0] * N  

for i in range(N):  
    arr[i] = int(input())  
for i in range(0, N, 2):  
    print(arr[i], end=" ")  
