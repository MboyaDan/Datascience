#lists
Lst1 = ["apple","cow",'sheep','dog','human']
if "cow" in Lst1:
    print("yes it is ")
#changing items in the list
Lst1 [1] = 'google'
print(Lst1)
#inserting items in the list it inserts at a particular index
Lst1.insert(1, 'berry')
print(Lst1)#adding items in the list
Lst1.append('orange')
print(Lst1)
#Extending the list
Lst2 = ['apple','cow','sheep','dog','human']
Lst1.extend(Lst2)
print(Lst1)
#removing items in the list
Lst2.remove("apple")
print(Lst2)
#pop keywod removes the last item from the list
Lst2.pop(1)
# removing an item from the list using index
del Lst2[1]
#clearing items in the list
Lst2.clear()
#looping through the list
Lst1 = ['apple','cow','sheep','dog','human']
for i in Lst1:
    print(i)
    
for i in range (len(Lst1)):
    print(Lst1[i])
    #using while loop
Lst1 =['apple','cow','sheep','dog','human']
i = 0
while i < len(Lst1):
    print(Lst1[i])
    i += 1
#List Comprehension offers the shortest syntax for looping through lists

Lst1 = ['shee','goat','house','tree','hill','appl']
[print(x) for x in Lst1]
#List comprehension

fruits = ["apple"]