clothes = ["shirt", "sock", "pants", "sock", "towel"] 
paired_socks = [] 
for item in clothes: 
	if item == "sock": 
		continue
	else: 
		print(f"Washing {item}") 
paired_socks.append("socks") 
print(f"Washing {paired_socks}")
