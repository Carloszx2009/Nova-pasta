#para informar o nome, ano de nascimento e ano atual. Deverá calcular a
#idade. (idade = anoatual – anonascimento). Se a idade for 18 anos ou mais, exibir
#mensagem: Voce já é de maior e pode fazer a carteira de motorista. Se a idade for
#menor que 18 e maior ou igual a 16, exibir a mensagem: Voce já pode votar. 

input_name = input("Digite seu nome: ")
birth_year = int(input("Digite seu ano de nascimento: "))
current_year = int(input("Digite o ano atual: "))
age = current_year - birth_year

if age >= 18:
    print(f"{input_name}, você já é de maior e pode fazer a carteira de motorista.")
elif age >= 16:
    print(f"{input_name}, você já pode votar.")
else:
    print(f"{input_name}, você ainda não pode votar.")
