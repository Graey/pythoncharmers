def createMap(bin_oct_map): 
	bin_oct_map["000"] = '0'
	bin_oct_map["001"] = '1'
	bin_oct_map["010"] = '2'
	bin_oct_map["011"] = '3'
	bin_oct_map["100"] = '4'
	bin_oct_map["101"] = '5'
	bin_oct_map["110"] = '6'
	bin_oct_map["111"] = '7'

def convertBinToOct(bin): 
	l = len(bin) 
	 
	t = -1
	if '.' in bin: 
		t = bin.index('.') 
		len_left = t 
	else: 
		len_left = l 
	 
	for i in range(1, (3 - len_left % 3) % 3 + 1): 
		bin = '0' + bin
	 
	if (t != -1): 
		
		len_right = l - len_left - 1
		 
		for i in range(1, (3 - len_right % 3) % 3 + 1): 
			bin = bin + '0'
	
	bin_oct_map = {} 
	createMap(bin_oct_map) 
	i = 0
	octal = "" 
	
	while (True) : 
		 
		octal += bin_oct_map[bin[i:i + 3]] 
		i += 3
		if (i == len(bin)): 
			break
			
		if (bin[i] == '.'): 
			octal += '.'
			i += 1

	return octal 

bin = "1111001010010100001.010110110011011"
print("Octal number = ", 
	convertBinToOct(bin)) 

