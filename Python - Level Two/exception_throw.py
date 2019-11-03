try:
	f = open('simple.txt','w')
	f.write("Test write to simple text")
except IOError:
	print("Error: Could not find file or read data!")
finally:
	print("I alawys work no matter what!")
	
# else:
# 	print("Success!")
# 	f.close()