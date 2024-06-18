AGENCIA = "0001"
LIMITES_SAQUES = 3
extrato = ""
saldo = 0
numero_saques = 0
limite_saque = 500
usuarios = []

contas = []

def menu():
  print("""
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Criar Usuário
  [5] Criar Conta
  [6] Listar Contas
  [0] Sair
    """)

def depositar(valor, saldo, extrato, /):
  if valor <= 0:
    print("\n@@@ O valor informado não pode ser depositado! @@@")
  else:
    saldo += valor
    extrato += f"Depósito: \tR$ {valor:.2f}\n"
    print("\n=== Depósitvo realizado com sucesso! ===")
  return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, limites_saques, numero_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limites_saques  

  if excedeu_saldo:
    print("\n@@@ Você não tem saldo suficiente para sacar esse valor! @@@")

  elif valor < 0:
    print("\n@@@ O valor informado não pode ser sacado! @@@")

  elif excedeu_limite:
    print("\n@@@ O seu limite diário de saque é de R$500 @@@")

  else:
    numero_saques += 1

    if excedeu_saques:
      print("\n@@@ Você já atingiu o limite de saques diário! @@@")

    else:
      saldo -= valor
      extrato += f"Saque: \t\tR$ {valor:.2f}\n"
      print("\n=== Saque realizado com sucesso! ===")
  return valor, extrato

def exibir_extrato(saldo, /, *, extrato):
  print("===========EXTRATO===========\n")
  print("\nNão foram realizadas movimentações" if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=============================")

def criar_usuario(usuarios):
  cpf = input("Informe o CPF (somente números): ")
  usuario = filtrar_usuarios(cpf, usuarios)

  if usuario:
    print("\n@@@ Já existe uma conta com esse CPF! @@@")
    return

  nome = input("Informe o nome do usuário: ")
  data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereço (logadoura, n° - bairro - cidade - estado): ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, endereco: "endereco"})

  print("=== Usuário criado com sucesso! ===")

def filtrar_usuarios(cpf, usuarios):
  for usuario in usuarios:
    if usuario["cpf"] == cpf:
      return usuario
  return None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtrar_usuarios(cpf, usuarios)

  if usuario:
    print("=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

  print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
  for conta in contas:
    print(f"""
----------------------------------------
Agência:\t {conta["agencia"]}
N°/C:\t\t {conta["numero_conta"]}      
Nome:\t\t {conta["usuario"]["nome"]}
CPF:\t\t {conta["usuario"]["cpf"]}
          """)

while True:
  menu()
  opcao = int(input(": "))

  if opcao == 1:
    valor = float(input("Informe o valor que deseja depositar: "))
    saldo, extrato = depositar(valor, saldo, extrato)
      
  elif opcao == 2:
    valor_saque = float(input("O informe o valor que deseja sacar: "))
    saldo, extrato = sacar(valor=valor_saque, saldo=saldo, extrato=extrato, limite=limite_saque, limites_saques=LIMITES_SAQUES, numero_saques=numero_saques)
 
  elif opcao == 3:
    exibir_extrato(saldo, extrato=extrato)

  elif opcao == 4:
    criar_usuario(usuarios)

  elif opcao == 5:
    numero_conta = len(contas) + 1

    conta = criar_conta(AGENCIA, numero_conta, usuarios)
    if conta:
      contas.append(conta)
  
  elif opcao == 6:
    listar_contas(contas)
  elif opcao == 0:
    break
  else:
    print("Opção informada não existe!")

