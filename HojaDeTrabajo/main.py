
cadena = """(
<
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
        [atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = false
    >,
    <
        [atributo_numerico] = 56.4,
        [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
        [atribut_booleano] = false
    >
)"""
txt = cadena.replace("\n","")
txt = txt.replace(" ","")
elementos = []
estado = 0
def automata(entrada):
    estado = 0
    for i in range(len(entrada)):
        if (estado == 0):
            if (entrada[i]=="("):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_parA")
                estado = 1
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado == 1):
            if(entrada[i]=="<"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_mayor")
                estado = 2
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado == 2):
            if(entrada[i]=="["):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_corcheteA")
                estado = 3
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado == 3):
            if(entrada[i] != "]"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_nombreAtributo")
                estado = 4
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado == 4):
            if(entrada[i]!="]"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_nombreAtributo")
                estado=4
                continue
            elif(entrada[i]=="]"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_corcheteC")
                estado=5
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado == 5):
            if(entrada[i]=="="):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_igual")
                estado = 6
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado == 6):
            if(entrada[i].isdigit()):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_numero")
                estado = 7
                continue
            elif(entrada[i]=='"'):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_comilla")
                estado = 10
                continue
            elif(entrada[i].isalpha):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_palabra")
                estado = 13
                continue
            elif(entrada[i]=="-"):
                elementos.append((entrada[i]))
                print(entrada[i]+" tk_signo")
                estado = 7
                continue
            elif (entrada[i] == "+"):
                elementos.append((entrada[i]))
                print(entrada[i] + " tk_signo")
                estado = 7
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==7):
            if(entrada[i].isdigit()):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_numero")
                estado = 7
                continue
            elif(entrada[i]=="."):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_punto")
                estado = 8
                continue
            elif(entrada[i]==","):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_coma")
                estado = 14
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==8):
            if(entrada[i].isdigit()):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_numero")
                estado =9
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==9):
            if(entrada[i].isdigit()):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_numero")
                estado = 9
                continue
            elif(entrada[i]==","):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_coma")
                estado = 14
                continue
            elif(entrada[i]==">"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_menoque")
                estado=15
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==10):
            if(type(entrada[i]!=str)):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_cadena")
                estado = 11
                continue
            else:
                print(type(entrada[i]))
                print("Entrada Incorrecta")
                break
        if(estado == 11):
            if(entrada[i] != '"'):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_cadena")
                estado=11
                continue
            elif(entrada[i]=='"'):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_comilla")
                estado=12
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==12):
            if(entrada[i]==","):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_coma")
                estado=14
                continue
            elif (entrada[i] == ">"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_menoque")
                estado = 15
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==13):
            if(entrada[i].isalpha()):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_palabra")
                estado=13
                continue
            elif(entrada[i]==","):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_coma")
                estado=14
                continue
            elif (entrada[i] == ">"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_menorque")
                estado = 15
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==14):
            if(entrada[i]=="["):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_corchetA")
                estado=3
                continue
            else:
                print("Entrada Inconrrecta")
                break
        if(estado==15):
            if(entrada[i]==","):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_coma")
                estado=16
                continue
            elif(entrada[i]==")"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_ParC")
                estado=17
                pass
            else:
                print("Entrada Incorrecta")
                break
        if(estado==16):
            if(entrada[i]=="<"):
                elementos.append(entrada[i])
                print(entrada[i]+" tk_mayorque")
                estado=2
                continue
            else:
                print("Entrada Incorrecta")
                break
        if(estado==17):
            print("Entrada Correcta")
            break

automata(txt)

