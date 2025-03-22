def logical_function(x, y):
    return int(x != y)  

x, y = map(int, input().split())  
print(logical_function(x, y))  
