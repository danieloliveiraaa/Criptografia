def cripto(frase):
    translate = ""
    
    for letra in frase:
        if letra in "Aaâáà":
            translate = translate + "!"
        elif letra in "Bb":
            translate = translate + "@"
        elif letra in "Cc":
            translate = translate + "#"
        elif letra in "Dd":
            translate = translate + "$"
        elif letra in "Eeêé":
            translate = translate + "%"
        elif letra in "Ff":
            translate = translate + "&"
        elif letra in "Gg":
            translate = translate + "*"
        elif letra in "Hh":
            translate = translate + "("
        elif letra in "Iiíì":
            translate = translate + "|"    
        elif letra in "Jj":
            translate = translate + ")"
        elif letra in "Kk:":
            translate = translate + "^"
        elif letra in "Ll":
            translate = translate + "="
        elif letra in "Mm":
            translate = translate + "+"
        elif letra in "Nn":
            translate = translate + ">"
        elif letra in "Ooôóò":
            translate = translate + "<"
        elif letra in "Pp":
            translate = translate + ";"
        elif letra in "Qq":
            translate = translate + "]"    
        elif letra in "Rr":
            translate = translate + "["
        elif letra in "Ss":
            translate = translate + "´"
        elif letra in "Tt":
            translate = translate + "8"
        elif letra in "Uuúù":
            translate = translate + "¨"
        elif letra in "Vv":
            translate = translate + "-"
        elif letra in "Ww":
            translate = translate + "_+"
        elif letra in "Xx":
            translate = translate + "+++"
        elif letra in "Yy":
            translate = translate + "~_~"
        elif letra in "Zz":
            translate = translate + "#_@"    
        
        else:
            translate = translate + letra
    return translate



def descripto(frase):
    translate = ""
    
    for letra in frase:
        if letra in "!":
            translate = translate + "a"
        elif letra in "@":
            translate = translate + "b"
        elif letra in "#":
            translate = translate + "c"
        elif letra in "$":
            translate = translate + "d"
        elif letra in "%":
            translate = translate + "e"
        elif letra in "&":
            translate = translate + "f"
        elif letra in "*":
            translate = translate + "g"
        elif letra in "(":
            translate = translate + "h"
        elif letra in "|":
            translate = translate + "i"    
        elif letra in ")":
            translate = translate + "j"
        elif letra in "^":
            translate = translate + "k"
        elif letra in "=":
            translate = translate + "l"
        elif letra in "+":
            translate = translate + "m"
        elif letra in ">":
            translate = translate + "n"
        elif letra in "<":
            translate = translate + "o"
        elif letra in ";":
            translate = translate + "p"
        elif letra in "]":
            translate = translate + "q"    
        elif letra in "[":
            translate = translate + "r"
        elif letra in "´":
            translate = translate + "s"
        elif letra in "8":
            translate = translate + "t"
        elif letra in "¨":
            translate = translate + "u"
        elif letra in "-":
            translate = translate + "v"
        elif letra in "_+":
            translate = translate + "w"
        elif letra in "+++":
            translate = translate + "x"
        elif letra in "~_~":
            translate = translate + "y"
        elif letra in "#_@":
            translate = translate + "z"    
        else:
            translate = translate + letra
    return translate



escolha = 0
while escolha != 3:
    escolha = int(input("[1]Criptografar \n[2]Descriptografar \n[ ]Qualquer Para Encerrar. \n "))

    if escolha == 1:
        print(cripto(input("Digite uma mensagem a ser criptografada: \n")))
    elif escolha == 2:
        print(descripto(input("Digite uma mensagem a ser criptografada, para descriptografa-la: \n")))
    else:
        break





    


        


        
    






















            
