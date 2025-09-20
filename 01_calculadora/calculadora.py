numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite outro numero:"))
operação = input("Digite a operação que deseja realizar (+, -, *, /)")
if operação == "+":
    print(numero1 + numero2)
    print("obrigado por usar o programa")
elif operação == "-":
    print(numero1 - numero2)
    print("obrigado por usar o programa")
elif operação == "*":
    print(numero1 * numero2)
    print("obrigado por usar o programa")
elif operação == "/": 
   if numero2 == 0:
    print("não e possível realizar esta operação:")
   else:   
    print(numero1 / numero2)
    print("Obrigado por usar o programa")
