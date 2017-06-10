def get_ways(num):

    way = [1]
    ways = 0

    while ways < num:

        i = 0
        new_way = [1, 1]

        while len(new_way) - 1 <= ways and i < len(way) - 1:

            found_way = way[i] + way[i + 1]
            new_way.insert(i + 1, found_way)

            i += 1
        way = new_way
        ways += 1

    return way



def main():

	pascal_it = get_ways(40)
	mid = len(pascal_it) // 2

	print(pascal_it[mid])

if __name__ == '__main__':
	main()
