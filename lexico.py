			####D E L  >= <= +  -  " " . <- >  <  =  *  \  (  )  { } ; \. eof
transicao = [[1,99,14,17,17,10,10,6,99,99,13,17,17,17,10,10,11,12,8,99,16,99,15 ],
			[1,4,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,2],
			[3,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[3,4,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,18,18,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[5,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,7,6,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,8,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[14,99,14,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[15,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99]]
print(transicao[0][2])

final = [1, 3, 5, 17, 7, 9, 10, 11, 12, 13, 14, 15, 16]

def consulta(x):
	if(x[0] == 0 || x[0] == 1 || x[0] == 2 || x[0] == 3 || x[0] == 4 || x[0] == 5 || x[0] == 6 || x[0] == 7 || x[0] == 8 || x[0] == 9):
		i = transicao[0][1]
		while(x[i] != 0 && x[i] != 1 && x[i] != 2 && x[i] != 3 && x[i] != 4 && x[i] != 5 && x[i] != 6 && x[i] != 7 && x[i] != 8 && x[i] != 9):
			i = transicao[0][1]
		if(x[i] != 1 && x[i] != 2 && x[i] != 4 && x[i] != None):
			return 1
