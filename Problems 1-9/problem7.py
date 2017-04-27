import math


count = 2
primes = []
    
while True:
    is_prime = True
        
    for j in range(2, int(math.sqrt(count) + 1)):
        if count % j == 0: 
            is_prime = False
            break
        
    if is_prime :
        primes.append(count)
        
    count += 1

    if len(primes) - 1 > 10001:
        break

print(primes[10000])
