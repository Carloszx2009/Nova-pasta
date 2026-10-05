 # Calcular a área de um triângulo e mostrar o valor da área.

input_numbers = []
for i in range(3):
    number = float(input(f"Digite o {i+1}º lado do triângulo: "))
    input_numbers.append(number)

s = sum(input_numbers) / 2
area = (s * (s - input_numbers[0]) * (s - input_numbers[1]) * (s - input_numbers[2])) ** 0.5
print(f"A área do triângulo é: {area}")