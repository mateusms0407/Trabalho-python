nome=input("nome do aluno: ")
diciplina=input("qual a diciplina: ")
nota1=float(input("nota parcial: "))
nota2=float(input("nota bimestral: "))
media=(nota1+nota2)/2
if media>5:
    s=("aprovado")
else:
    s=("reprovado")
print(f"o aluno {nome} esta {s} na diciplina de {diciplina}")
