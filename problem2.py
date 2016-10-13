n = 32
fibs=[]
def fibonacci(n):
	fibonacci_numbers = [0, 1]
	for i in range(2,n + 2):
		if i >= 4000000:
			pass
		else:
			fibonacci_numbers.append(fibonacci_numbers[i -1]+fibonacci_numbers[i - 2])
	fibonacci_numbers = fibonacci_numbers[2:]
	evens = []
	sum = 0
	for j in fibonacci_numbers:
		if j % 2 == 0:
			sum += j
	return sum
def main():
	print(fibonacci(n))

if __name__ == '__main__':
	main()
