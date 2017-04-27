sum_of_the_squares = 0

square_of_the_sum = 0 
for i in range(0,101):
	sum_of_the_squares += i**2


for j in range(0,101):
	square_of_the_sum += j

square_of_the_sum = square_of_the_sum**2

print(square_of_the_sum - sum_of_the_squares)
