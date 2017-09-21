from collections import namedtuple

			####D E L  >= <= +  -  " " . <- >  <  =  *  \  (  )  { } ; \. eof
transicao = [[1,99,14,17,17,10,10,6,99,99,13,17,17,17,10,10,11,99,8,99,16,99,15 ],
	   		[1,4,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,2],
	   		[3,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[3,4,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,18,18,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[5,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,7,6,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,8,99,99,99,99,99,99,99,99,9,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,19,99,99,99,99,99,99,99,12,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[14,99,14,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[15,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
			[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,12,99,99,99,99,99]]

final = [1, 3, 5, 17, 7, 9, 10,12, 13, 14, 15, 16]

def verificaDigito(x):
	if(x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9"):
		return 1
	else:
		return 0

def consulta(x):
	j = 0 #armazenando estado
	i = 0 #string[0]
	if(x[0] == "0" or x[0] == "1" or x[0] == "2" or x[0] == "3" or x[0] == "4" or x[0] == "5" or x[0] == "6" or x[0] == "7" or x[0] == "8" or x[0] == "9"):		
		while(x[i] != "0" and x[i] != "1" and x[i] != "2" and x[i] != "3" and x[i] != "4" and x[i] != "5" and x[i] != "6" and x[i] != "7" and x[i] != "8" and x[i] != "9" and len(x) > i):
			j = transicao[j][0]
			i = i + 1
		if(x[i] == "E"):
			j = transicao[j][1]
			i = i + 1
		if(x[i] == "\."):
			j = transicao[j][21]
			i = i + 1
		
		if(j == 1):
			return 1 #token e um digito
		
		if(j == 2 and verificaDigito(x[i] == 1)):
			while(x[i] != "0" and x[i] != "1" and x[i] != "2" and x[i] != "3" and x[i] != "4" and x[i] != "5" and x[i] != "6" and x[i] != "7" and x[i] != "8" and x[i] != "9" and len(x) > i):
				j = transicao[j][0]
				i = i + 1
			if(x[i] == "E"):
				j = transicao[j][1]
				i = i + 1
			if(j == 3):
				return 1 #token e um numerico
		if(j == 4):
			if(x[i] == "+" | x[i] == "-"):
				j = transicao[j][5]
				i = i + 1
			if(verificaDigito(x[i]) == 1):
				j = transicao[j][0]
			while(x[i] != "0" and x[i] != "1" and x[i] != "2" and x[i] != "3" and x[i] != "4" and x[i] != "5" and x[i] != "6" and x[i] != "7" and x[i] != "8" and x[i] != "9" and len(x) > i):
				j = transicao[j][0]
				i = i + 1
#<-
	if(x[0] == "<" and x[1] == "-"):
		return 9
	#>=			
	if(x[0] == ">" and x[1] == "="):
		j = transicao[j][3]
		return 2
	
	#<=
	if(x[0] == "<" and x[1] == "="):
		j = transicao[j][4]
		return 2
	
	#<>
	if(x[0] == "<" and x[1] == ">"):
		j = transicao[j][4]
		return 2
	
	#> ou < ou = 
	if(x[0] == ">" or x[0] == "<" or x[0] == "="):
		j = transicao[j][4]
		return 2
	
	###" ... "
	if(x[0] == "\""):
		j = transicao[j][7]
	   	while(x[i] != "\""):
		      i = i + 1 
		      if(x[i] == "\""):
			 	j = transicao[j][8]
		return 4
	
	#{...}
	if(x[0] == "{"):
		j = transicao [j][18]
		while(x[i] != "}"):
		      i = i + 1
		      if(x[i] == "}"):
		      	j = transicao[j][19]
		return 5
		      
 	#(..)
	if(x[0] == "("):
		j = transicao[j][11]
		while(x[i] != ")"):
		      i = i + 1	
		      if(x[i] == ")"):
		      	j = transicao[j][12]
		return 6
#;
	if(x[0] == ";"):
		j = transicao[j][20]
		return 7
		
	#operandos
	if(x[0] == "+" or x[0] == "-" or x[0] == "/" or x[0] == "*"):
		j = transicao[j][10]
		return 8
		      

#id
	if(x[0].isalpha() == True):
		if(len(x) > 1):
			while(x[i].isalpha() != False and x[i].isdigit() != False and x[i] != "_" and len(x) > i):
				i = i + 1
		if(x[i].isalpha() == True or x[i].isdigit() == True or x[i] == "_" or x[i] == None):
			return 10
			 

node = namedtuple("node", "Token Lexema Tipo")

c = node("inicio", "inicio", "rsv")
d = node("varinicio","varinicio","rsv")
e = node("varfim", "varfim", "rsv")
f = node("escreva", "escreva", "rsv")
g = node("leia", "leia", "rsv")
h = node("se", "se", "rsv")
i = node("entao","entao", "rsv")
j = node("fimse","fimse", "rsv")
k = node("fim","fim", "rsv")
l = node("Inteiro","Inteiro", "rsv")
m = node("entao","entao", "rsv")
n = node("literal","literal", "rsv")
o = node("real","real", "rsv")

tabelaSimbolo = [c, d, e, f, g, h, i, j, k, l, m, n, o]

def criaNode(token,lexema,tipo):
	new = node(token,lexema,tipo)
	if(nodeExists(new) == 0):
		tabelaSimbolo.append(new)

def nodeExists(node):
	i = 0
	while(len(tabelaSimbolo) > i):
		if(node == tabelaSimbolo[i]):
			return 1
		i = i + 1
	return 0

criaNode("inicioop", "inicio", "rsv")
