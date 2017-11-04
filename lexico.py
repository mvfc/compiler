from collections import namedtuple
import sys

node = namedtuple("node", "Token Lexema Tipo")

c = node("inicio", "inicio", "rsv")
d = node("varinicio", "varinicio", "rsv")
e = node("varfim", "varfim", "rsv")
f = node("escreva", "escreva", "rsv")
g = node("leia", "leia", "rsv")
h = node("se", "se", "rsv")
i = node("entao", "entao", "rsv")
j = node("fimse", "fimse", "rsv")
k = node("fim", "fim", "rsv")
l = node("Inteiro", "Inteiro", "rsv")
m = node("entao", "entao", "rsv")
n = node("literal", "literal", "rsv")
o = node("real", "real", "rsv")

tabelaSimbolo = [c, d, e, f, g, h, i, j, k, l, m, n, o]

arquivo = open("texto.alg")

def lexico(linha):
    i = 0
    if(linha[0].isalpha() == True):
        while(len(linha) < i or linha[i].isalpha() == True or linha[i].isdigit() == True or linha[i] == "_"):
            i = i + 1
        criaNode("Identificador", linha[:i], "id")
        if(linha[i:] != ""):
            lexico(linha[i:])
    if(linha[0].isdigit() == True):
        while(len(linha) < i or linha[i].isdigit() == True or linha[i] == "E" or linha[i] == "."):
            i = i + 1
        criaNode("Constante numerica", linha[:i], "Num")
        if (linha[i:] != ""):
            lexico(linha[i:])
    if(linha[0] == "("):
        criaNode("Abre parenteses", linha[:1], "AB_P")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == ")"):
        criaNode("Fecha parenteses", linha[:1], "FC_P")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == "+" or linha[0] == "-" or linha[0] == "/" or linha[0] == "*"):
        criaNode("Operador aritmetico", linha[:1], "OPM")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == ";"):
        criaNode("Ponto e virgula", linha[:1], "PT_V")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == "<" and linha[1] == "-"):
        criaNode("Atribuicao", linha[:1], "RCB")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == "<" and linha[1] == "="):
        criaNode("Operador relacional", linha[:1], "OPR")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == ">" and linha[1] == "="):
        criaNode("Operador relacional", linha[:1], "OPR")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == "<" and linha[1] == ">"):
        criaNode("Operador relacional", linha[:1], "OPR")
        if (linha[1:] != ""):
            lexico(linha[1:])

    if(linha[0] == "<" or linha[0] == ">" or linha[0] == "="):
        criaNode("Operador relacional", linha[:1], "OPR")
        if (linha[1:] != ""):
            lexico(linha[1:])

def criaNode(token, lexema, tipo):
    new = node(token, lexema, tipo)
    if (nodeExists(new) == 0):
        tabelaSimbolo.append(new)

def nodeExists(node):
    i = 0
    while (len(tabelaSimbolo) > i):
        if (node == tabelaSimbolo[i]):
            return 1
        i = i + 1
    return 0

def MostrarTabela():
    print(tabelaSimbolo)

def __main__():
    """str(sys.argv)
    arquivo = open(argv[1])"""
    arquivo = open("texto.alg")
    linha = arquivo.readline()
    while(linha != ""):
        lexico(linha)
        linha = arquivo.readline()
    MostrarTabela()

__main__()
