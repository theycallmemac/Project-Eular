largest = 0
for i in range (100, 999):
    for j in range(100, 999):
        num = str(i * j)
        reverse = num[::-1]
        if num == reverse:
            num = int(num)
            if num > largest:
                largest = num
print(largest)