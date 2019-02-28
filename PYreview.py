"""
review

python-interpreted language
high-level
"""

#print the current date
import time
import datetime

print ("Time(s) since epoch: %s" %time.time())
print ("Current datetime: " , datetime.datetime.now())
print ("#day of Month year week#(day)# dayOfWeek: ")
print(datetime.date.today().strftime("%j %d %B %Y %W %w %A"))
print (time.strftime("%m|%d~{%H:%M}"))

some_limit = 3
condition = True #1
#condition for
#while loop
while(condition<some_limit):
    print("do something repetetive a couple times")
    condition+=1
#for iterating though lists
example_list = ["collection", "of", 'things'] #group of objects
#we can use a for-loop to iterate through items
for thing in example_list:
    print("{} {}".format(thing,example_list.index(thing)))
    #prints thing and it's position in the list
#or a range of numbers (from, to, by)
for x in range (4,47,3):
    print(x, end=' ')
    #print that number
    #and if that number is even/divisible by 2
    even = x%2
    if(even==0):
        print('e', end = " ") #for even
    #takes the square
    power = x**2
    arbitrary_limit = 1437
    #less than arbistrary limit
    if(power<arbitrary_limit):
        continue
    #greater than or equal to number
    elif(power>=arbitrary_limit):
        break
    #is never reached, but is here just in case
    else:
        break

#encapsulate a function in a...function
def printList(some_list) :
    for entry in some_list:
        print(some_list.index(entry), entry)
        
list_of_parameters = ["example", "parameters"]  
printList(list_of_parameters)

x = 427300000 #grand scope
#global?
print(x)
#this x is just a placeholder and the 
for x in range(20, 2200000000,x):
    print(x, end = ' ')
    print("local scope")
#since we used x it changed
print(x)

