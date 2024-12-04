def adicionar_planeta(planetas):
    nome = input("Digite o nome do planeta: ")
    tamanho = input("Digite o tamanho do planeta (em km de diâmetro): ")
    distancia = input("Digite a distância do Sol (em milhões de km): ")
    apelido = input("Digite o apelido do planeta: ")
    
    planeta = {
        "nome": nome,
        "tamanho": tamanho,
        "distancia": distancia,
        "apelido": apelido
    }
    
    planetas.append(planeta)
    print(f"Planeta {nome} adicionado com sucesso!")

def exibir_planetas(planetas):
    if len(planetas) == 0:
        print("Nenhum planeta cadastrado.")
    else:
        for i, planeta in enumerate(planetas):
            print(f"{i+1}. Nome: {planeta['nome']}, Tamanho: {planeta['tamanho']} km, Distância do Sol: {planeta['distancia']} milhões de km")

def buscar_planeta(planetas):
    nome = input("Digite o nome do planeta que deseja buscar: ")
    for planeta in planetas:
        if planeta["nome"].lower() == nome.lower():
            print(f"Planeta encontrado: Nome: {planeta['nome']}, Tamanho: {planeta['tamanho']} km, Distância do Sol: {planeta['distancia']} milhões de km")
            return
    print(f"Planeta {nome} não encontrado.")

def atualizar_planeta(planetas):
    nome = input("Digite o nome do planeta que deseja atualizar: ")
    for planeta in planetas:
        if planeta["nome"].lower() == nome.lower():
            print(f"Planeta encontrado: Nome: {planeta['nome']}, Tamanho: {planeta['tamanho']} km, Distância do Sol: {planeta['distancia']} milhões de km")
            tamanho = input("Digite o novo tamanho do planeta (em km de diâmetro): ")
            distancia = input("Digite a nova distância do Sol (em milhões de km): ")
            apelido = input("Digite o novo apelido do planeta: ")
            planeta["tamanho"] = tamanho
            planeta["distancia"] = distancia
            planeta["apelido"] = apelido
            print(f"Planeta {nome} atualizado com sucesso!")
            return
    print(f"Planeta {nome} não encontrado.")

def excluir_planeta(planetas):
    nome = input("Digite o nome do planeta que deseja excluir: ")
    for planeta in planetas:
        if planeta["nome"].lower() == nome.lower():
            planetas.remove(planeta)
            print(f"Planeta {nome} removido com sucesso!")
            return
    print(f"Planeta {nome} não encontrado.")

planetas = []

# Funções para gerenciamento de planetas
def adicionar_planeta(planetas):
    nome = input("Digite o nome do planeta: ")
    tamanho = input("Digite o tamanho do planeta (em km de diâmetro): ")
    distancia = input("Digite a distância do Sol (em milhões de km): ")
    apelido = input("Digite o apelido do planeta: ")
    
    planeta = {
        "nome": nome,
        "tamanho": tamanho,
        "distancia": distancia,
        "apelido": apelido
    }
    
    planetas.append(planeta)
    print(f"Planeta {nome} adicionado com sucesso!")

def exibir_planetas(planetas):
    if len(planetas) == 0:
        print("Nenhum planeta cadastrado.")
    else:
        for i, planeta in enumerate(planetas):
            print(f"{i+1}. Nome: {planeta['nome']}, Tamanho: {planeta['tamanho']} km, Distância do Sol: {planeta['distancia']} milhões de km")

def buscar_planeta(planetas):
    nome = input("Digite o nome do planeta que deseja buscar: ")
    for planeta in planetas:
        if planeta["nome"].lower() == nome.lower():
            print(f"Planeta encontrado: Nome: {planeta['nome']}, Tamanho: {planeta['tamanho']} km, Distância do Sol: {planeta['distancia']} milhões de km")
            return
    print(f"Planeta {nome} não encontrado.")

def atualizar_planeta(planetas):
    nome = input("Digite o nome do planeta que deseja atualizar: ")
    for planeta in planetas:
        if planeta["nome"].lower() == nome.lower():
            print(f"Planeta encontrado: Nome: {planeta['nome']}, Tamanho: {planeta['tamanho']} km, Distância do Sol: {planeta['distancia']} milhões de km")
            tamanho = input("Digite o novo tamanho do planeta (em km de diâmetro): ")
            distancia = input("Digite a nova distância do Sol (em milhões de km): ")
            apelido = input("Digite o novo apelido do planeta: ")
            planeta["tamanho"] = tamanho
            planeta["distancia"] = distancia
            planeta["apelido"] = apelido
            print(f"Planeta {nome} atualizado com sucesso!")
            return
    print(f"Planeta {nome} não encontrado.")

def excluir_planeta(planetas):
    nome = input("Digite o nome do planeta que deseja excluir: ")
    for planeta in planetas:
        if planeta["nome"].lower() == nome.lower():
            planetas.remove(planeta)
            print(f"Planeta {nome} removido com sucesso!")
            return
    print(f"Planeta {nome} não encontrado.")

# Menu de opções
def menu():
    while True:
        print("\nMenu de Gerenciamento de Planetas")
        print("1. Adicionar planeta")
        print("2. Exibir planetas")
        print("3. Buscar planeta")
        print("4. Atualizar planeta")
        print("5. Excluir planeta")
        print("6. Sair")
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            adicionar_planeta(planetas)
        elif opcao == "2":
            exibir_planetas(planetas)
        elif opcao == "3":
            buscar_planeta(planetas)
        elif opcao == "4":
            atualizar_planeta(planetas)
        elif opcao == "5":
            excluir_planeta(planetas)
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executar o menu
menu()
