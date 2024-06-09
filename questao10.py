print("sou uma tabuada")
numero = int(input("digite um numero: "))
print("a tabuada desse numero é")
for valor in range(1,11):
    print(f"{numero} x {valor} = {numero * valor}")