# Leia o nome e a idade de 5 pessoas. Ao final, mostre o nome e a idade da pessoa mais velha.

input_data = []
for i in range(5):
    name = input(f"Digite o nome da {i+1}ª pessoa: ")
    age = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    input_data.append((name, age))

oldest_person = max(input_data, key=lambda x: x[1])
print(f"A pessoa mais velha é {oldest_person[0]} com {oldest_person[1]} anos.")
