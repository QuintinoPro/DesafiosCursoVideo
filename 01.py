
n1 = int(input("\nDigite um numero: "))

print("\n------Desafio 05")
print(f'Sucessor: {n1 + 1}')
print(f'Antecessor: {n1 - 1}')

print("\n------Desafio 06")
print(f'Dobro: {n1*2}')
print(f'Raiz Quadrada: {n1**2}')

print("\n------Desafio 07")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

print(f'Media das Notas: {(nota1+nota2)/2}')

print("\n------Desafio 08")
metros = float(input("Digite os Metros: "))

print(f'Centimetros: {metros * 100}')
print(f'Milimetros: {metros * 1000}')

print("\n------Desafio 09")
for x in range(1,10):
    print(f'{n1} * {x} = {n1 * x}')

print("\n------Desafio 10")
salr = float(input("Saldo em Reais: "))
print(f'Saldo em Dolares: {salr/4.94:.2f}')

print("\n------Desafio 11")
larg = float(input("Largura: "))
alt = float(input("Altura: "))
area = larg * alt
litro = 2
litros = area/2
print(f'Precisa de {litros} litros para pintar')

print("\n------Desafio 12")
preco = float(input("Preco: "))
print(f'O novo preco com 5% de desconto é {preco - (preco * 0.05):.2f}')

print("\n------Desafio 13")
sala = float(input("Digite seu Salario: "))
print(f'Salario com 15% de Aumento {sala + (sala * 0.15):.2f}')

print("\n------Desafio 14")
celsius = float(input("Digite a Temperatura em  Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f'A Temperatura de Fahrenheit é: {fahrenheit}')

print("\n------Desafio 15")
km = float(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade de dias que o carro foi Alugado: "))
print(f'O valor total a Pagar é: {(60 * dias) + (km * 0.15)}')



