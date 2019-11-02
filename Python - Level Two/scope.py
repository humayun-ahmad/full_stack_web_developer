x = 50

def func():
	global x
	x = 1000


print("before function call, x is : ", x)
func()
print("after function call, x is : ", x)
