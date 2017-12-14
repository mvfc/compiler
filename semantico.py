import analisadorsintatico
import lexico

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.tipo = None
        self.lexema = None
        self.token = None
        self.pai = None

root = Tree()
arvore = None

x = 0

def __init__():
    arquivo = open("programa.c", "w")
    arquivo.write("#include <stdio.h>\n\n")
    arquivo.write("typedef char literal[256];\n")
    arquivo.write("void main(void)\n{\n\n")
    arquivo.close()

def __semantico__(lexema, token, regra, i):
    global x
    global arvore
    arquivo = open("programa.c", "a")
    if(regra == 1):
        if(arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "P'"
        if(arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 2):
        if (arvore == None):
            arvore = Tree()
            arvore.token = "inicio"
            arvore.lexema = "inicio"
            arvore.tipo = "inicio"
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "P"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 3):
        if (arvore == None):
            arvore = Tree()
            arvore.token = "varinicio"
            arvore.lexema = "varinicio"
            arvore.tipo = "varinicio"
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "V"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 4):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "LV"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 5):
        arquivo.write("\n\n\n")
        if (arvore == None):
            arvore = Tree()
            arvore.token = "varfim"
            arvore.lexema = "varfim"
            arvore.tipo = "varfim"
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "varfim"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 7):
        if (arvore == None):
            arvore = Tree()
            arvore.token = "int"
            arvore.lexema = lexema
            arvore.tipo = "int"
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "TIPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = "int"
        arvore.pai.token = "int"
        arvore = arvore.pai
    elif(regra == 8):
        if (arvore == None):
            arvore = Tree()
            arvore.token = "real"
            arvore.lexema = lexema
            arvore.tipo = "double"
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "TIPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = "double"
        arvore = arvore.pai
    elif(regra == 9):
        if (arvore == None):
            arvore = Tree()
            arvore.token = "literal"
            arvore.lexema = lexema
            arvore.tipo = "literal"
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "TIPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = "literal"
        arvore.pai.lexema = lexema
        arvore = arvore.pai
    elif(regra == 6):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = lexico.__getlexema__(i-3)
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = arvore.tipo
        arvore = arvore.pai
        arquivo.write( arvore.tipo +" "+arvore.lexema+";\n")
        if(arvore.tipo == "int"):
            analisadorsintatico.__settipo__("int", i-3)
        else:
            analisadorsintatico.__settipo__(arvore.tipo, i-3)
    elif(regra == 10):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "A"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 11):
        if(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-2))) == "id"):
            print("Erro: Variável não declarada:" + lexico.__getlexema__(i-2))
        else:
            if(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-2))) == "literal"):
                arquivo.write('scanf("%s", '+lexico.__getlexema__(i-2)+');\n')
            if(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-2))) == "int"):
                arquivo.write('scanf("%d", &' + lexico.__getlexema__(i-2) + ');\n')
            if(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-2))) == "real"):
                arquivo.write('scanf("%lf", &' + lexico.__getlexema__(i-2) + ');\n')
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = lexema
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 12):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.lexema = lexico.__getlexema__(i-2)
        if('"' in arvore.lexema):
            arquivo.write('printf(' + arvore.lexema + '");\n')
        else:
            arquivo.write('printf(' + arvore.lexema + ');\n')
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 13):
        if (arvore.pai == None):
            arvore.pai = Tree()
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.lexema = lexema
        arvore.pai.token = token
        arvore.pai.tipo = "literal"
        arvore = arvore.pai
    elif(regra == 14):
        if (arvore.pai == None):
            arvore.pai = Tree()
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.lexema = lexema
        arvore.pai.token = token
        arvore.pai.tipo = "num"
        arvore = arvore.pai
    elif(regra == 15):
        analisadorsintatico.__settipo__("id", i)
        if (arvore.pai == None):
            arvore.pai = Tree()
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = "id"
        arvore.pai.lexema = lexema
        arvore.pai.token = token
        arvore = arvore.pai
    elif(regra == 16):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.tipo = "A"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right
        arvore = arvore.pai
    elif(regra == 17):
        if(lexico.__getlexema__(i-5) == ";"):
           if(lexico.__getlexema__(i-1) == ";"):
               arquivo.write(lexico.__getlexema__(i-4)+analisadorsintatico.__gettipo__(i-3)+lexico.__getlexema__(i-2)+"\n")
           elif(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-4))) == "id"):
                print("Erro: Variável não declarada:" + lexico.__getlexema__(i-3))
           else:
                if(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-2))) == analisadorsintatico.__gettipo__(i-2)):
                    arquivo.write(lexico.__getlexema__(i-4)+analisadorsintatico.__gettipo__(i-3)+lexico.__getlexema__(i-2)+"\n")
                else:
                    print("Erro: Tipos diferentes para atribuição")
        else:
            if (analisadorsintatico.__gettipo__(i - 5) == "id"):
                print("Erro: Variável não declarada:" + lexico.__getlexema__(i - 5))
            else:
                if (analisadorsintatico.__gettipo__(i - 6) == analisadorsintatico.__gettipo__(i - 4)):
                    arquivo.write(str(lexico.__getlexema__(i - 6)) + str(analisadorsintatico.__gettipo__(i - 5)) + arvore.lexema + "\n")
                else:
                    print("Erro: Tipos diferentes para atribuição")
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.tipo = "CMD"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 18):
        arquivo.write(analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-3)))+" "+"T"+str(x)+"\n")
        arquivo.write("T"+str(x)+" = "+lexico.__getlexema__(i-3)+" "+analisadorsintatico.__gettipo__(i-2)+" "+lexico.__getlexema__(i-1)+"\n")
        x = x + 1
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.tipo = "LD"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.lexema = "T"+str(x-1)
        if(arvore.right != None):
            arvore.pai.tipo = arvore.right.tipo
        else:
            arvore.pai.tipo = arvore.left.tipo
        arvore = arvore.pai
    elif(regra == 19):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.tipo = arvore.tipo
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = arvore.tipo
        arvore.pai.lexema = arvore.lexema
        arvore.pai.token = arvore.token
        arvore = arvore.pai
    elif(regra == 20):
        if (arvore.pai == None):
            arvore.pai = Tree()
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = "id"
        arvore.pai.lexema = lexico.__getlexema__(i-1)
        arvore.pai.token = token
        arvore = arvore.pai
    elif(regra == 21):
        if (arvore.pai == None):
            arvore.pai = Tree()
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore.pai.tipo = "num"
        arvore.pai.lexema = lexico.__getlexema__(i-1)
        arvore.pai.token = token
        arvore = arvore.pai
    elif(regra == 22):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "A"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 23):
        arquivo.write("}\n")
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "COND"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 24):
        arquivo.write("if(T"+str(x-1)+") {\n")
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = arvore.lexema
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 25):
        arquivo.write("\n"+analisadorsintatico.__gettipo__(lexico.__getindex__(lexico.__getlexema__(i-3))) + " " + "T" + str(x)+"\n")
        arquivo.write("T" + str(x) + " = " + lexico.__getlexema__(i-3) + " " + analisadorsintatico.__gettipo__(i-2) + " " + lexico.__getlexema__(i-1)+"\n")
        x = x + 1
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = arvore.lexema
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 26):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "CORPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 27):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "CORPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 28):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "CORPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 29):
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "CORPO"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    elif(regra == 30):
        arvore = Tree()
        if (arvore.pai == None):
            arvore.pai = Tree()
        arvore.pai.lexema = "A"
        if (arvore.pai.left == None):
            arvore.pai.left = arvore
        else:
            arvore.pai.right = arvore
        arvore = arvore.pai
    arquivo.close()
