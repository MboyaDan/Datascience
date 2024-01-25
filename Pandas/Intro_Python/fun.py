def cookies(fname,sname):
    print(fname + ": " + sname)
    
    
cookies("default","wordpress")
#list fun

def continent(country):
    for i in country:
        print(country)
africa = ['kenya','uganda','ghana']
continent(africa)

#lambda
x = lambda a : a + 10
print(x(5))

b = lambda x,z : x * z
print(b(5,8))

#lambda and normal function

def mul(n):
    return lambda d : d *n
my_double = mul(2)
print(my_double(6))

#try block function
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")