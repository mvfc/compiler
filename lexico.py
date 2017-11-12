from collections import namedtuple

node = namedtuple("node", "Lexema Token")

c = node("inicio", "inicio")
d = node("varinicio", "varinicio")
e = node("varfim", "varfim")
f = node("escreva", "escreva")
g = node("leia", "leia")
h = node("se", "se")
i = node("entao", "entao")
j = node("fimse", "fimse")
k = node("fim", "fim")
l = node("inteiro", "inteiro")
m = node("entao", "entao")
n = node("literal", "literal")
o = node("real", "real")

tabelaSimbolo = [c, d, e, f, g, h, i, j, k, l, m, n, o]

retorno = []

def lexico(linha):
    i = 1
    global retorno
    if(linha[0].isalpha() == True):
        while(len(linha) < i or linha[i].isalpha() == True or linha[i].isdigit() == True or linha[i] == "_"):
            i = i + 1
        criaNode(linha[:i], "id")
        if(linha[i:] != ""):
            if(linha[i] == " "):
                i += 1
            lexico(linha[i:])
    elif(linha[0].isdigit() == True):
        while(len(linha) < i or linha[i].isdigit() == True or linha[i] == "E" or linha[i] == "."):
            i = i + 1
        criaNode(linha[:i], "num")
        if (linha[i:] != ""):
            if (linha[i] == " "):
                i += 1
            lexico(linha[i:])
    elif(linha[0] == "("):
        criaNode(linha[:1], "ab_p")
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == ")"):
        criaNode(linha[:1], "fc_p")
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == "+" or linha[0] == "-" or linha[0] == "/" or linha[0] == "*"):
        criaNode(linha[:1], "opm")
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == ";"):
        criaNode(linha[:1], "pt_v")
        if (linha[1:] != ""):
            lexico(linha[1:])

    elif(linha[0] == "<" and linha[1] == "-"):
        criaNode(linha[:2], "rcb")
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == "<" and linha[1] == "="):
        criaNode(linha[:2], "opr")
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == ">" and linha[1] == "="):
        criaNode(linha[:2], "opr")
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == "<" and linha[1] == ">"):
        criaNode(linha[:2], "opr")
        if (linha[2:] != ""):
            lexico(linha[2:])

    elif(linha[0] == "<" or linha[0] == ">" or linha[0] == "="):
        criaNode(linha[:1], "opr")
        if (linha[1:] != ""):
            lexico(linha[1:])
    elif(linha[0] == '"'):
        while(len(linha) < i or linha[i] != '"'):
            i = i + 1
        criaNode(linha[:i], "ARG")
        i += 1
        if (linha[i:] != ""):
            if (linha[i] == " "):
                i += 1
            lexico(linha[i:])
    elif(linha[0] == ""):
        criaNode("", "EOF")

def criaNode(lexema, token):
    new = node(lexema, token)
    newrsv = node(lexema, lexema)
    check = nodeExists(new, newrsv)
    if (check == 2):
        retorno.append(lexema)
    else:
        tabelaSimbolo.append(new)
        retorno.append(token)

def nodeExists(node, nodersv):
    i = 0
    while (len(tabelaSimbolo) > i):
        if(nodersv == tabelaSimbolo[i]):
            return 2
        elif (node == tabelaSimbolo[i]):
            return 1
        i = i + 1
    return 0

"""def MostrarTabela():
    open("output.txt", "w").close()
    saida = open("output.txt", "w")
    indexval = 0
    for i in range(len(tabelaSimbolo)):
        print(tabelaSimbolo[indexval])
        saida.write(str(tabelaSimbolo[indexval]).replace("node",""))
        saida.write("\n")
        indexval += 1
    print(retorno)

def __main__():
    arquivo = open("texto.alg", "r")
    linha = arquivo.readline()
    while(linha != ""):
        lexico(linha)
        linha = arquivo.readline()
    if(linha == ""):
        criaNode("", "EOF")
    MostrarTabela()"""

def __main__(args):
    global retorno
    retorno = []
    tabelaSimbolo = []
    tabelaSimbolo = [c, d, e, f, g, h, i, j, k, l, m, n, o]
    lexico(args)
    return retorno
