#Tuples

tup = ('Raj', 'Shantanu', 'Sandy',  'div')
print (tup)

#concatenation

print (tup+('jon', 'ron'))


#repetetion

print (tup*3)

#slicing

print (tup[1:5])


#List

list = [1,2,'a',"sf",234,543]
print (list)
list.append('3')
print (list)
list.extend(['white','black'])
print (list)

#dictionalry

dict = {1:"green", 2:"black", 3:"red"}

print (dict)

dict.update({4:'white'})

print (dict)

# sets : no duplicate element in sets

set = {1,2,3,4,6,7,7}
print (set)

s1 = {1,2,'d','a'}
s2 = {1,'e','d'}

print ("union: ", s1|s2)
print ("Intersection: ", s1 & s2)
print ("Difference: ", s1-s2)
