#para informar 10 números e no final, mostrar a quantidade de números
#pares, a quantidade de números ímpares, a soma dos números pares e a soma dos
#números ímpares... 

input("Digite 10 números inteiros: ")
input_numbers = []
for i in range(10):
    number = int(input(f"Digite o {i+1}º número: "))
    input_numbers.append(number)

pares = [num for num in input_numbers if num % 2 == 0]
impares = [num for num in input_numbers if num % 2 != 0]

even_count = len(pares)
odd_count = len(impares)
even_sum = sum(pares)
odd_sum = sum(impares)
