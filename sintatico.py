import lexico

        #############inicio | varinicio | varfim | id| ; | int | real | leia | escreva | literal | num | rcb | opm | se | ( | ) | entao | opr | fimse | fim | $ | P | V | LV | D | TIPO | A | ES | ARG | CMD | LD | OPRD | COND | CABECALHO| EXP_RCORPO
tabela_slr = """0""" [    2,      99,     99,      99, 99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,  99, 1,  99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99],
             """1"""[   99,      99,     99,      99, 99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,  00, 99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99],
             """2"""[   99,       4,     99,      99, 99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,  99, 99,  3, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99],
             """3"""[   99,      99,     99,      12, 99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,  99, 99, 99, 99,  99,  99,   5,   7,   99,   8,   99,   99,    6,         14,    99],
             """3"""[   99,      99,     17,      49, 99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,  99, 99, 99, 15,  16,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99],    
             """4"""[   99,      99,     99,      "r5", 99,  99,  99,     "r5",     "r5",     99,        99,  99,   99,   "r5",  99, 99,   99,   99,    99,     "r5",  99, 99, 99, 99,  99,  99,   5,  99,   99,  99,   99,   99,   99,         99,    99],
             """5"""[   99,      99,     99,      12, 99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,  99, 99, 99, 99,  99,  99,  18,   7,   99,   8,   99,   99,    6,         14,    99],
             """6"""[   99,      99,     99,      12, 99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,  99, 99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99],

  
######## algoritmo parcialmente implementado
stack = [0]
i = 0

while(1):
    ip = entrada[i]
    if(tabela_slr[s][a].isdigit() == True and tabela_slr[s,a] != 99):
        stack.append(entrada[i])
        stack.append(tabela_slr[s][a])
    elif(tabela_slr[s][a].isdigit() != True):
        for p in range(2*len(dirprod)): #dirprod = parte direita da producao
            stack.pop() #da pop nas 2 * tamanho de Beta entradas da pilha
        stack.append(stack[len(stack)]) #append no número do estado
        stack.append(tabela_slr[stack[len(stack)]][esqprod]) #esqprod = parte esquerda da producao
        print(prod) #printa a producao na tela
    elif(tabela_slr[s][a] == 00):
        return 0
    else:
        raise Exception("Erro!")
