dictionary = {1: 1}

def get_terms(num):
	return dictionary[num] if num in dictionary else dictionary.setdefault(num, 1 + (get_terms(3 * num + 1) if num % 2 else get_terms(num/2)))

def main():

	print(max((get_terms(num),num) for num in range(2, 10 ** 6))[1])
  
if __name__ == '__main__':
	main()
