"""TaskTracker - Fase 2 (Bootcamp II)"""

tarefas = []


def cadastrar_tarefa():
    print("\n--- Cadastro de Nova Tarefa ---")
    titulo = input("Titulo da tarefa: ")
    descricao = input("Descricao da tarefa: ")
    prioridade = input("Prioridade (Alta, Media ou Baixa): ")
    data_limite = input("Data limite (DD/MM/AAAA): ")

    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print("Tarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for i, t in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}")
        print(f"  Titulo:      {t['titulo']}")
        print(f"  Descricao:   {t['descricao']}")
        print(f"  Prioridade:  {t['prioridade']}")
        print(f"  Data limite: {t['data_limite']}")
        print(f"  Status:      {t['status']}")


def exibir_menu():
    print("\n===== TaskTracker =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicacao")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker.")
            break
        else:
            print("Opcao invalida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()