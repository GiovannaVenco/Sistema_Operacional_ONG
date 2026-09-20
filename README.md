# Sistema de Gerenciamento de Voluntários para ONG

Sistema desenvolvido em Python para auxiliar ONGs no gerenciamento de voluntários, habilidades, disponibilidades, atividades e alocações.

O projeto surgiu como uma **APS (Atividade Prática Supervisionada)** do curso de Engenharia da Computação e também está sendo desenvolvido como projeto de estudo e portfólio.

## Objetivo

Criar uma plataforma capaz de organizar voluntários e auxiliar na escolha das pessoas mais adequadas para cada atividade, considerando suas habilidades e disponibilidade.

## Funcionalidades

### Habilidades
- Cadastrar habilidades
- Listar habilidades
- Editar habilidades
- Ativar e inativar
- Excluir
- Impedir nomes duplicados

### Voluntários
- Cadastrar voluntários
- Listar voluntários
- Editar nome, telefone e e-mail
- Ativar e inativar
- Excluir
- Associar habilidades
- Remover habilidades

### Disponibilidade
- Registrar dias da semana
- Registrar horário inicial e final
- Validar horários
- Listar disponibilidades
- Editar disponibilidades
- Excluir disponibilidades

### Atividades
Em desenvolvimento:
- Cadastro de atividades
- Data e horário
- Número de vagas
- Habilidades necessárias

### Alocação
Planejado:
- Verificar voluntários ativos
- Verificar disponibilidade
- Comparar habilidades
- Calcular compatibilidade
- Selecionar os voluntários mais adequados

## Lógica de alocação

Para participar de uma atividade, o voluntário deverá:

1. Estar ativo
2. Estar disponível no dia e horário
3. Possuir pelo menos uma habilidade exigida

A compatibilidade será calculada por:

```text
Compatibilidade = (habilidades compatíveis / habilidades exigidas) × 100
```

Os voluntários com maior compatibilidade terão prioridade no preenchimento das vagas.

## Estrutura do projeto

```text
projeto_ong/
│
├── main.py
├── menu.py
├── funcoes.py
├── habilidade.py
├── voluntario.py
├── disponibilidade.py
├── atividade.py
└── alocacao.py
```

## Tecnologias e conceitos

- Python
- Programação Orientada a Objetos
- Classes e objetos
- Funções
- Listas e dicionários
- Estruturas condicionais
- Estruturas de repetição
- Validação de entradas
- Relacionamento entre classes
- UML

## Status do projeto

- [x] Habilidades
- [x] Voluntários
- [x] Associação de habilidades
- [x] Estrutura de disponibilidade
- [x] Cadastro e edição de disponibilidade
- [ ] Finalizar disponibilidade
- [ ] Atividades
- [ ] Alocação
- [ ] Relatórios
- [ ] Testes finais

## Próximos passos

- Finalizar o módulo de disponibilidade
- Desenvolver atividades
- Implementar alocação automática
- Criar relatórios
- Realizar testes finais

Após a conclusão da APS, o projeto poderá ser evoluído com persistência de dados e interface gráfica.

## Contexto acadêmico

Projeto desenvolvido como **APS – Atividade Prática Supervisionada** do curso de **Engenharia da Computação**.
