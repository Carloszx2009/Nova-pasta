input_numbers = []
for i in range(5):
    number = int(input(f"Digite o {i+1}º número: "))
    input_numbers.append(number)

pares = [num for num in input_numbers if num % 2 == 0]
if pares:
    media = sum(pares) / len(pares)
    print(f"A média dos números pares é: {media}")
else:
    print("Nenhum número par foi digitado.")
