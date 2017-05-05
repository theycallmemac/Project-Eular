import math


def divisors(n):
    counter = 0
    for number in range(1, int(math.ceil(math.sqrt(n)))):
        if n % number == 0:
            counter +=2
        else:
            continue
    return counter

def main():
    i = 1
    for j in range(2,1000000):
        i += j
        if divisors(i) >= 500:
            print(i)
            break
if __name__ == '__main__':
	main()