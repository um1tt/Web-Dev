N = int(input())  # Считываем количество элементов
arr = []  # Создаем пустой список

for _ in range(N):  
    arr.append(int(input()))  # Считываем каждое число отдельно и добавляем в список

print(*arr[::2])  # Выводим элементы с четными индексами через распаковку списка
