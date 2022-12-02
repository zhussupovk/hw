arr = [2, 5, 13, 7, 6, 4]
size = 6
index = 0
avg = 0
sumOfArr = 0
while index < size:
    sumOfArr = sumOfArr + arr[index]
    index = index + 1
avg = sumOfArr / size
print(int(avg))
