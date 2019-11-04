import one
print("Top level two.py")
one.func()

if __name__ == '__main__':
	print("Two.py being run dirctly")
else:
	print("two is being imported")