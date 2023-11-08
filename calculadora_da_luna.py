print("Bem-vindo à calculadora da Luna!")

valor_1 = float(input("Informe o valor 1: "))
operacao = input("Informe a operação (+, -, * ou /): ")
valor_2 = float(input("Informe o valor 2: "))

if operacao == "+":
    resultado = valor_1 + valor_2
elif operacao == "-":
    resultado = valor_1 - valor_2
elif operacao == "/":
    resultado = valor_1 / valor_2
elif operacao == "*":  # Correção: removi o "=" extra
    resultado = valor_1 * valor_2
else:
    print("Operação inválida")
    resultado = None

if resultado is not None:
    print(f"Resultado da operação: {resultado}")
