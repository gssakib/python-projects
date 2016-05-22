

def list_add(cnt,increase):
	numbers =[]
	i = 0
	while i < cnt:
		print"Numbers before appending: %s, Count before appending:%s" %(numbers,i)
		numbers.append(i)
	
		i = i+increase
		print"Numbers after appending: %s, Count after appending:%s" %(numbers,i)
		

	print "The final numbers are:  "
	return numbers

	



		
def make_list(cnt):
	numbers = []
	for num in range(0,cnt):
		print"Numbers before appending: %s, Count before appending:%s" %(numbers,num)
		numbers.append(num)
		print"Numbers after appending: %s, Count after appending:%s" %(numbers,num)
	print "The final numbers are:"
	return numbers
