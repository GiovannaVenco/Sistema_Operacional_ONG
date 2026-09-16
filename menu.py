# Importa as funções utilizadas pelo menu
from funcoes import (
    cadastrar_habilidade,
    listar_habilidades,
    editar_habilidade,
    alterar_status_habilidade,
    excluir_habilidade,
    cadastrar_voluntario,
    listar_voluntarios,
    editar_voluntario,
    alterar_status_voluntario,
    excluir_voluntario,
    associar_habilidade_voluntario,
    remover_habilidade_voluntario
)

# Menu de gerenciamento de habilidades
def menu_habilidades(habilidades):

    while True:

        print("\nMENU DE HABILIDADES")
        print("1 - Cadastrar habilidade")
        print("2 - Listar habilidades")
        print("3 - Editar habilidade")
        print("4 - Alterar status da habilidade")
        print("5 - Excluir habilidade")
        print("0 - Voltar")

        opcao = input(
            "Escolha o número da opção desejada: "
        ).strip()

        if not opcao.isdigit():
            print("Erro: digite apenas o número da opção desejada.")

        elif opcao == "1":
            cadastrar_habilidade(habilidades)

        elif opcao == "2":
            listar_habilidades(habilidades)

        elif opcao == "3":
            editar_habilidade(habilidades)

        elif opcao == "4":
            alterar_status_habilidade(habilidades)

        elif opcao == "5":
            excluir_habilidade(habilidades)

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print(
                "Erro: opção inválida. "
                "Digite apenas 1, 2, 3, 4, 5 ou 0."
            )
            
# Menu de gerenciamento de voluntários
def menu_voluntarios(voluntarios, habilidades):

    while True:

        print("\nMENU DE VOLUNTÁRIOS")

        print("1 - Cadastrar voluntário")
        print("2 - Listar voluntários")
        print("3 - Editar voluntário")
        print("4 - Alterar status do voluntário")
        print("5 - Excluir voluntário")
        print("6 - Associar habilidade")
        print("7 - Remover habilidade")
        print("0 - Voltar")

        # Guarda a opção escolhida pelo usuário
        opcao = input(
            "Escolha o número da opção desejada: "
        ).strip()

        # Verifica se o usuário digitou apenas números
        if not opcao.isdigit():

            print(
                "Erro: digite apenas o número da opção desejada."
            )

        # Cadastra um voluntário
        elif opcao == "1":

            cadastrar_voluntario(voluntarios)

        # Lista os voluntários
        elif opcao == "2":

            listar_voluntarios(voluntarios)

        # Edita um voluntário
        elif opcao == "3":

            editar_voluntario(voluntarios)

        # Altera o status
        elif opcao == "4":

            alterar_status_voluntario(voluntarios)

        # Exclui um voluntário
        elif opcao == "5":

            excluir_voluntario(voluntarios)

        # Associa uma habilidade ao voluntário
        elif opcao == "6":

            associar_habilidade_voluntario(
                voluntarios,
                habilidades
            )

        # Remove uma habilidade do voluntário
        elif opcao == "7":

            remover_habilidade_voluntario(voluntarios)

        # Volta ao menu principal
        elif opcao == "0":

            print("Voltando...")
            break

        # Caso o número digitado não exista no menu
        else:

            print(
                "Erro: opção inválida. "
                "Digite apenas 1, 2, 3, 4, 5, 6, 7 ou 0."
            )


# Menu principal do sistema
def menu_principal(habilidades, voluntarios):

    while True:

        print("\nMENU PRINCIPAL")

        print("1 - Gerenciar habilidades")
        print("2 - Gerenciar voluntários")
        print("0 - Sair")

        # Guarda a opção digitada pelo usuário
        opcao = input(
            "Escolha o número da opção desejada: "
        ).strip()

        # Verifica se o usuário digitou apenas números
        if not opcao.isdigit():

            print(
                "Erro: digite apenas o número da opção desejada."
            )

        # Abre o menu de habilidades
        elif opcao == "1":

            menu_habilidades(habilidades)

        # Abre o menu de voluntários
        elif opcao == "2":

            menu_voluntarios(
                voluntarios,
                habilidades
            )

        # Encerra o sistema
        elif opcao == "0":

            print("Saindo do sistema...")
            break

        # Caso seja digitado um número que não existe no menu
        else:

            print(
                "Erro: opção inválida. "
                "Digite apenas 1, 2 ou 0."
            )