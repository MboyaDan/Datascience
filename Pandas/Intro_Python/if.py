
#contol flow statements
#if condition:
#statement to excecute if condition is true

i=10
if (i<15):
    print("10 is less than 15")
print ("I am not in if")
"""Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""
#write a program that asks user to enter a number.program should then tell if number is odd or even.
#if (condition):
    # Executes this block if
    # condition is true
#else:
    # Executes this block if
    # condition is false
num = input('Enter a number:')
num =  int(num)
if num%2==0:
    print ('number is even')
else:
    print ('number is odd')
    
#voter eligibility


age = 15
if age >= 18: 
    print("You are eligible to vote.") 
else: 
    print("You are not eligible to vote.")


#and & or operator
3>2 and 4>1
3>2 and 4>5
3>2 or 4>5
not 4==4

#write a program that asks user to enter dish name and it should print which cuisine is that dish
#el if condition

uk=['samosa','daal','naan']
chinese=['eggs','pot samosa','fried rice']
italian=['pizza','pasta','risotto']
dish = input('enter dish name:')

if dish in uk:
    print ('uk')
elif dish in chinese:
    print ('chinese')
elif dish in italian:
    print ('italian')
else:
    print ('dish not found')



# python program to illustrate nested If statement 
  
i = 10
if (i == 10): 
    
    #  First if statement 
    if (i < 15): 
        print("i is smaller than 15") 
          
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print("i is smaller than 12 too") 
    else: 
        print("i is greater than 15") 
        
        
        
#for loop
#used when you want to same operation on range of things
 #A program to track your monthly expenses
exp = [3000,2500,2100,3100,2980]
total = 0
for item in exp:
    total=total + item
print(total)

#print 1 to 10
#range must have start index and stop index(1,11),if you don't provide it will assume it'szero
for i in range(1,11):
    print(i)
    #print square
    print(i*i)
    
#print our month number and expense and then in the end print total expense
exp = [3000,2500,2100,3100,2980]
#len(exp) will find the length of our list
for i in range (len(exp)):
    print('month:',(i+1),'expense:',exp[i])
    total = total + exp[i]
print('total expense:',total)

#finding your key
#use break whenever your goal has been achieved and you want to terminate
#Python break statement brings control out of the loop.
key_location= "chair"
locations = ['garage',"living","chair",'closet']
for i in locations:
    if i == key_location:
        print('key location found',i)
        break
    else:
        print('key location not found',i)
        
        
#continue statements
#print square of numbers between 1 to 5 except even numbers
#it has to be n+1 because it will always skip your second index
#Python continue Statement returns the control to the beginning of the loop.
for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)
 
#smart wash
clothes = ["shirt", "sock", "pants", "sock", "towel"] 
paired_socks = [] 
for item in clothes: 
	if item == "sock": 
		continue
	else: 
		print(f"Washing {item}") 
paired_socks.append("socks") 
print(f"Washing {paired_socks}"

 
 
 #while loop
 #while loop only takes one condition if it satisfies the condition it will continue
i=1
while i <= 5:
     print(i)
     i = i+1
