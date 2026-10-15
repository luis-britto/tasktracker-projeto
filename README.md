# TaskTracker

Aplicação de linha de comando (CLI) para gerenciamento de tarefas, desenvolvida como parte da disciplina Bootcamp II (CEUB).

## Sobre o projeto

O TaskTracker permite cadastrar tarefas com título, descrição, prioridade e data limite, além de visualizar a lista de tarefas cadastradas organizadas por prioridade.

Este é um projeto cumulativo, desenvolvido em 3 fases:
- **Fase 1:** Planejamento lógico e arquitetural (concluída)
- **Fase 2:** Estruturação do repositório e implementação em Python (etapa atual)
- **Fase 3:** Containerização com Docker

## Tecnologias utilizadas

- Python 3

## Como executar

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   ```
2. Acesse a pasta do projeto:
   ```
   cd tasktracker-projeto
   ```
3. Execute o programa:
   ```
   python src/main.py
   ```

## Funcionalidades

- Cadastrar nova tarefa (título, descrição, prioridade, data limite)
- Visualizar tarefas cadastradas, ordenadas por prioridade
- Validação de título obrigatório (não aceita campo vazio)
- Validação estrita de prioridade (aceita apenas Alta, Média ou Baixa)

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Autor

Luis Otavio Da Costa Britto — Bootcamp II — CEUB
