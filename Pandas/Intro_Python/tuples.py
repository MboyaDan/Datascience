#itemsto a tuple
tup1 =('g','f','a','b','d')
tp2 = list(tup1)
tp2[1] = 'cow'
tup1 = tuple (tp2)
print(tup1)