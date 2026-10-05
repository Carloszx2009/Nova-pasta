input_numbers = []
for i in range(10):
    number = int(input(f"Digite o {i+1}º número: "))
    input_numbers.append(number)

soma = sum(input_numbers)
print(f"A soma dos números informados é: {soma}")
