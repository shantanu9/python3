# if elif else

marks = 43
if(marks > 80):
    print ("you are awesome !")
elif ( 61 < marks < 80 ):
    print ("Average")
elif (41 < marks < 60):
    print ("need to improve")
else:
    print ("congrats! You failed.")


# while loop

n = int(input('enter the number n: '))
if (n <= 0):
    print ("enter a positive integer")
else:
    sum = 0
    while (n > 0):
        sum+= n
        n-=1
print (sum)


# for loop

for qty  in range(99,0,-1):
    print (qty,"bottles of beer in the fridge,", 99-qty," in my belly")
    if (qty == 0):
        print ("no more beer in fridge,  please buy more.")


# break

count = 0
while True:
    print (count)
    count+=1
    if (count==10):
        break

# continue

for x in range(20):
    if (x%2)==0:
        continue
    print(x)

    
