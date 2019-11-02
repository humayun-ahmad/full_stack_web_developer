# use of filter

mylist = [1,2,3,4,5,6,7]

def odd_bool(num):
	return num%2 == 1

result = filter(odd_bool,mylist)


# using labda function get the same result like above
result = filter(lambda num : num%2 == 1,mylist)

print(list(result))