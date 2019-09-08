course = 52

# if elif

if course == 50:
    print (course)
elif not course == 50:
    print (str(course)+"CS51")

# boolean
alphaonly = True if input().isalpha() else False
print (alphaonly)

#while
counter = 0
while counter <= 100:
    print (counter)
    counter += 1

# for loop
for x in range(100):
    print (x)

for y in range(0,100,3):
    print (y)

# list
list = [x for x in range(0,100,9)]
print (list)

list1 = [1,2,3,4]
list1[len(list1):] = [5]
print (list1)


#tuple
presidents = [
    ("shantanu",1),
    ("shanthanu",2),
    ("SHANTANU",3),
    ("SHANTHANU",4)
    ]

for prez, year in presidents:
    print ("In {1},{0} took office".format(prez,year))


#dictionary

pizzas = {
    "cheese":9,
    "pepperoni":8,
    "bacon":10,
    "chicken":1
    }

for pie, price in pizzas.items():
    print ("A whole {} pizza costs ${}".format(pie,price))


#function


def sqr(x):
    return x*x

print (sqr(100))


#class

class Student():
    def __init__(self, name,id):
        self.id = id
        self.name = name

    def changeId(self, id):
        self.id = id

    def prints(self):
        print ("{} - {}".format(self.name,self.id))

jane = Student("Shantanu",10)
jane.prints()
jane.changeId(11)
jane.prints()


#arithematic operators

a = 10
b = 20
print ("a + b =", a+b)
print ("a - b =", a-b)
print ("a * b =", a*b)
print ("a / b =", a/b)

print ('5^3=', 5**3)
print ("20 % 3 =", 20%3)
print ("pie number (22/7) value with floor division: ", 22//7)


#Assignmet Operator

b+=a
print(b)


#comparison operator

print ("Is a > b ?",  a > b)
print ("Is a = b ?",  a ==b)
print ("Is a!= b ?", a != b)

# logical operator

x = True
y = False

print ("X and Y: ",  x and y)
print ("X OR Y: ", x or y)
print ("x not of Y: ", not x)


#bitwise operator

e = 6 #110
f = 2 #010

print ("Bitwise and = ", e & f)
print ("Bitwsie OR = ",  e | f)
print ("Bitwise XOR = ",  e ^ f)

print ("e right shit by 2 ", e >> 2 )
print ("e left shit by 2 ", e << 2 )


# membership operator

x = [1,2,3,4,5]

print (3 in x)

print (10 in x)

#concatenationn

str1 = 'shantanu'
str2 = 'hi'

print ("concatenate str1 and str2: ", str1+str2)

#string repetetion
print (str1*2)

#string slicing

print (str1[2:4])
print (str1[3])
print (str1[-3])

# string functions

print (str1.count('s',0,7))
print (str1.find("ta"))

print (str1.isalpha())
