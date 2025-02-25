numero = int(input("Digite um numero de 0 a 99: "))

if 0 <= numero <= 99: # garantir que o numero esta entre 0 e 99
    if numero >= 10: # se for numero de dois digitos
        numero_str = str(numero)
        dg1 = int(numero_str[0]) # separa o primeiro digito
        dg2 = int(numero_str[1]) # separa o segundo digito
        exiba = dg1 + dg2
        print(f"{numero} -> {dg1} + {dg2} = {exiba}")
    else: # se for numero de um digito
        print(f"{numero} -> {numero}")
else:
    print("O numero deve estar entre 0 e 99.")