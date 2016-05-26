import hashmap

#states that I visited and their abbreviations
states = hashmap.new()

hashmap.set(states, 'New-York','NY')
hashmap.set(states, 'Texas','TX')
hashmap.set(states, 'Massachusetts','MA')
hashmap.set(states, 'Rhode-Island','RI')
hashmap.set(states, 'Florida','FL')
hashmap.set(states, 'Maine','ME')
hashmap.set(states, 'Connecticut','CT')


#countries I have visited and the continent

countries = hashmap.new()

hashmap.set(countries,'USA','North-America')
hashmap.set(countries,'Bangladesh','Asia')
hashmap.set(countries,'India','Asia')
hashmap.set(countries,'Saudi-Arabia','Asia')
hashmap.set(countries,'UAE','Asia')
hashmap.set(countries,'Canada','North-America')

print "Please input the name of the state you think you visited."
rqst = raw_input(">>>>>>>>>  ")

st = hashmap.get(states, rqst, 'Not-Visited')

if st == 'Not-Visited':
	print "Nope,%s is %s" %(rqst,st)
else:
	print "Yes %s(%s) was visited" %(rqst,st)

