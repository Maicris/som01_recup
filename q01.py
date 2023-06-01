soma = 0
while True:
    num = input("Digite um número par para somar (enter para sair): ")
    if num == "":
        break
    elif int(num) % 2 == 0:
        soma += int(num)
    else:
        print(f"{num} não é um número par")
print("A soma dos números pares na lista é:", soma)
