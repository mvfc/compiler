a = "(Lexema='real', Token='real')"

c = a.split(",")

print(c)
print(a)

c = c[1].replace(")", "")
c = c.replace("Token='", "")
c = c.replace("'", "")
c = c.replace(" ","")
print(c)

lexema = "real"

aux = "Lexema='"+lexema+"'"

print(aux)

if(aux in a):
    print("Ok")