#create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New-York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of states and cities in them
cities = {
	'CA': 'San-Francisco',
	'MI': 'Detroit',
	'FL': 'Jackson-ville'
}


#add more cities

cities['NY'] = 'New-York'
cities['OR'] = 'Portland'

#print out some cities
print "-" *10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

#print some states
print "-"*10
print "Michigan's abbreviation is: " , states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" %(state,abbrev)
	
	
#print every city in state
print '-'*10
for abbrev,city in cities.items():
	print "%s has the city %s" %(abbrev,city)
	
	
#now do both at the same time

print "-" *10
for state, abbrev in states.items():
	print"%s state is abbreviated %s and has city %s"% (state, abbrev, cities[abbrev])

print "-"*10
#safely get a abbreviation by state that might not be there 

state = states.get('Texas')

if not state:
	print "Sorry, no Texas."
	
#get a city with a default value

city = cities.get('TX', 'D.N.E.')
print "The city for the state 'TX' is: %s" %city



	
	
	

