menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

extrato = ""
saldo = 0
numero_saques = 0
limite_saque = 500
LIMITES_SAQUES = 3

while True:
  print(menu)
  opcao = int(input(": "))

  if opcao == 1:
    valor = float(input("Informe o valor que deseja depositar: "))

    if valor <= 0:
      print("O valor informado não pode ser depositado!")
    else:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      
  elif opcao == 2:
    saque = float(input("O informe o valor que deseja sacar: "))

    excedeu_saldo = saque > saldo

    excedeu_limite = saque > limite_saque

    excedeu_saques = numero_saques >= LIMITES_SAQUES

    if excedeu_saldo:
      print("Você não tem saldo suficiente para sacar esse valor!")

    elif saque < 0:
      print("O valor informado não pode ser sacado!")

    elif excedeu_limite:
      print("O seu limite diário de saque é de R$500")

    else:
      numero_saques += 1

      if excedeu_saques:
        print("Você já atingiu o limite de saques diário!")

      else:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        print("Você sacou R$%.2f" %saque)
        
 
  elif opcao == 3:
    print("===========EXTRATO===========\n")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f} \n")
    print("=============================")

  elif opcao == 0:
    break
  else:
    print("Opção informada não existe!")