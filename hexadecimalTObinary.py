#hexadecimal para binario
digito_bin = ""
resultado_bin = ""
string = "" # trocar pelo input do usuario
a = input("Digite seu numero hexadecimal").upper() # fazer upper em todas as outras
                                                   # conversoes de hexadecimal pra estetica
for string in a:
    if string == "0":
        digito_bin = "0000"
    elif string == "1":
        digito_bin = "0001"
    elif string == "2":
        digito_bin = "0010"
    elif string == "3":
        digito_bin = "0011"
    elif string == "4":
        digito_bin = "0100"
    elif string == "5":
        digito_bin = "0101"
    elif string == "6":
        digito_bin = "0110"
    elif string == "7":
        digito_bin = "0111"
    elif string == "8":
        digito_bin = "1000"
    elif string == "9":
        digito_bin = "1001"
    elif string == "A":
        digito_bin = "1010"
    elif string == "B":
        digito_bin = "1011"
    elif string == "C":
        digito_bin = "1100"
    elif string == "D":
        digito_bin = "1101"
    elif string == "E":
        digito_bin = "1110"
    elif string == "F":
        digito_bin = "1111"
    else:
        print("Digite apenas caracteres hexadecimais (0-9, A-F).")
        resultado_bin = ""
        break

    resultado_bin += digito_bin # 

if resultado_bin:
    print(resultado_bin)