data = []
with open('./beresford061203.csv','r') as f:
	for line in f.readlines()[55:]:
		#print(type(line))
		data.append(line)
	
with open('./data.csv','w') as fo:
	for line in data:
		#print(type(line))
		fo.write(line)		
