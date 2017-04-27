
solution = 0
for x in range(2520,1000000000,420):
    for y in [11, 13, 14, 16, 17, 18, 19]:
        if x % y != 0:
            break
        if x % y == 0:
            if y == 19:
                solution = x
            continue
    if solution != 0:
        break
print (solution)
