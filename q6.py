num = 2
cont = 1
while num < 35:
    if num % 2 == 1:
        num += cont
        cont += 1
    elif num % 3 == 0:
        cont += 1
        num += cont
    else:
        num += cont + 1

print(f"Valores: num={num} e cont={cont}")

