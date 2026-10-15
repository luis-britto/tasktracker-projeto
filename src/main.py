"""
TaskTracker - Fase 2 (Bootcamp II)
Autor: Luis Otavio Da Costa Britto

Aplicacao de linha de comando (CLI) para gerenciamento de tarefas,
implementando a logica definida no planejamento da Fase 1.
"""

tarefas = []


def normalizar_prioridade(valor):
    """Padroniza a prioridade digitada para um dos tres valores oficiais.
    Retorna None se o valor informado nao for valido."""
    valor_tratado = valor.strip().lower()
    if valor_tratado == "alta":
        return "Alta"
    if valor_tratado in ("media", "média"):
        return "Média"
    if valor_tratado == "baixa":
        return "Baixa"
    return None


def cadastrar_tarefa():
    print("\n--- Cadastro de Nova Tarefa ---")

    # Titulo: obrigatorio, nao pode ser vazio nem so espacos
    titulo = input("Titulo da tarefa: ").strip()
    while titulo == "":
        print("Erro: o titulo nao pode ficar vazio.")
        titulo = input("Titulo da tarefa: ").strip()

    descricao = input("Descricao da tarefa: ").strip()

    # Prioridade: validacao estrita (Alta, Media/Média ou Baixa)
    prioridade = normalizar_prioridade(
        input("Prioridade (Alta, Media ou Baixa): "))
    while prioridade is None:
        print("Erro: prioridade invalida. Digite Alta, Media ou Baixa.")
        prioridade = normalizar_prioridade(
            input("Prioridade (Alta, Media ou Baixa): "))

    data_limite = input(
        "Data limite (DD/MM/AAAA) ou deixe em branco: ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Nao definida",
        "status": "Pendente",  # definido automaticamente no cadastro
    }

    tarefas.append(tarefa)
    print(f"\nTarefa '{titulo}' cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- Lista de Tarefas ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    ordem_prioridade = {"Alta": 0, "Média": 1, "Baixa": 2}
    tarefas_ordenadas = sorted(
        tarefas, key=lambda t: ordem_prioridade[t["prioridade"]])

    for indice, tarefa in enumerate(tarefas_ordenadas, start=1):
        print(f"\nTarefa {indice}")
        print(f"  Titulo:      {tarefa['titulo']}")
        print(f"  Descricao:   {tarefa['descricao'] or '(sem descricao)'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")

    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")
    print(
        f"\nTotal: {len(tarefas)} tarefa(s) | Pendentes: {pendentes} | Concluidas: {concluidas}")


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
            print("\nEncerrando o TaskTracker. Ate a proxima!")
            break
        else:
            print("\nOpcao invalida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
