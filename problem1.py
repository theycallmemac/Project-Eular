lst = []
for i in range(1000):
	lst.append(i)
	
def sum_of_multiples(lst):
	mults = []
	for i in lst:
		if i % 3 == 0:
			mults.append(i)
		elif i % 5 == 0: 
			mults.append(i)
		else:
			pass
			
	sum = 0
	for i in mults:
	   sum = sum + i
	return sum

def main():
	print(sum_of_multiples(lst))

if __name__ == '__main__':
	main()
