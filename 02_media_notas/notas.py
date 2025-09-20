nota = float(input("Digite a nota do aluno: "))
if nota < 5:
    print("Aluno reprovado!")
elif nota >= 5 and nota <= 6.9:
    print("Aluno em recuperação!")
elif nota >= 7 and nota <= 10:
    print("Aluno aprovado!")
else:
    print("Só são aceitas notas de 0 a 10")
