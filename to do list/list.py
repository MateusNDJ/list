# Gerenciador de Tarefas (To-Do List)


tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def marcar_concluida():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        tarefas.pop(indice)
        print("Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("Entrada inválida. Certifique-se de escolher um número válido.")

def main():
    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
