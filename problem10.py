import math

count = 2
primes = []
sum = 0  
while True:
    is_prime = True
        
    for j in range(2, int(math.sqrt(count) + 1)):
        if count % j == 0: 
            is_prime = False
            break
        
    if is_prime :
        primes.append(count)
    
    if count > 2000000:
        break

    count += 1
for i in primes:
    sum = sum + i
print(sum)