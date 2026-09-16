# Importa a classe habilidade
from habilidade import habilidade
from voluntario import Voluntario
from disponibilidade import Disponibilidade
from datetime import datetime


# FUNÇÕES DE HABILIDADES

# Lista todas as habilidades cadastradas no sistema
def listar_habilidades(habilidades):

    print("\nHabilidades cadastradas:")

    # Percorre a lista de habilidades
    for h in habilidades:
        print(h)


# Cadastra uma nova habilidade
def cadastrar_habilidade(habilidades):

    # Pede o nome da nova habilidade
    nome_nova_habilidade = input(
        "Digite o nome da nova habilidade: "
    ).strip()

    # Verifica se o usuário deixou o nome vazio
    if nome_nova_habilidade == "":
        print(
            "Erro: o nome da habilidade não pode ficar vazio."
        )
        return

    # Começa considerando que a habilidade ainda não existe
    habilidade_repetida = False

    # Percorre as habilidades já cadastradas
    for h in habilidades:

        # Compara o nome digitado com os nomes existentes
        if h.nome.lower() == nome_nova_habilidade.lower():
            habilidade_repetida = True
            break

    # Se já existir uma habilidade com esse nome
    if habilidade_repetida:
        print(
            "Erro: essa habilidade já está cadastrada."
        )
        return

    # Descobre o próximo ID disponível
    proximo_id = (
        max(h.id_habilidade for h in habilidades) + 1
        if habilidades
        else 1
    )

    # Cria a nova habilidade
    nova_habilidade = habilidade(
        proximo_id,
        nome_nova_habilidade
    )

    # Adiciona a nova habilidade na lista
    habilidades.append(nova_habilidade)

    # Confirma o cadastro
    print("\nHabilidade cadastrada com sucesso!")
    print(nova_habilidade)


# Edita uma habilidade existente
def editar_habilidade(habilidades):

    print(
        "\nDeseja visualizar a lista de habilidades cadastradas?"
    )
    print("1 - Sim")
    print("2 - Não")

    # Guarda a resposta
    ver_lista = input().strip()

    # Se escolher sim, mostra as habilidades
    if ver_lista == "1":
        listar_habilidades(habilidades)

    # Se escolher não, continua normalmente
    elif ver_lista == "2":
        pass

    else:
        print(
            'Erro: digite "1" para Sim ou "2" para Não.'
        )
        return

    # Pede o ID da habilidade
    id_digitado = input(
        "\nDigite o ID da habilidade que deseja editar: "
    ).strip()

    # Verifica se o ID contém apenas números
    if not id_digitado.isdigit():
        print(
            "Erro: digite apenas o número do ID."
        )
        return

    # Converte o ID para inteiro
    id_digitado = int(id_digitado)

    # Começa considerando que nenhuma habilidade foi encontrada
    habilidade_encontrada = None

    # Procura a habilidade pelo ID
    for h in habilidades:

        if h.id_habilidade == id_digitado:
            habilidade_encontrada = h
            break

    # Se não encontrar a habilidade
    if habilidade_encontrada is None:
        print("Erro: habilidade não encontrada.")
        return

    # Mostra a habilidade selecionada
    print("\nHabilidade selecionada:")
    print(habilidade_encontrada)

    # Pede o novo nome
    novo_nome = input(
        "\nDigite o novo nome da habilidade: "
    ).strip()

    # Impede nome vazio
    if novo_nome == "":
        print(
            "Erro: o nome da habilidade não pode ficar vazio."
        )
        return

    # Verifica se já existe outra habilidade com o mesmo nome
    for h in habilidades:

        if (
            h.nome.lower() == novo_nome.lower()
            and h.id_habilidade != id_digitado
        ):
            print(
                "Erro: já existe uma habilidade com esse nome."
            )
            return

    # Altera o nome
    habilidade_encontrada.editar_nome(novo_nome)

    # Confirma a edição
    print("\nHabilidade editada com sucesso!")
    print(habilidade_encontrada)


# Altera o status de uma habilidade
def alterar_status_habilidade(habilidades):

    print(
        "\nDeseja visualizar a lista de habilidades?"
    )
    print("1 - Sim")
    print("2 - Não")

    # Guarda a resposta
    ver_lista = input().strip()

    if ver_lista == "1":
        listar_habilidades(habilidades)

    elif ver_lista == "2":
        pass

    else:
        print(
            "Erro: digite 1 para Sim ou 2 para Não."
        )
        return

    # Pede o ID
    id_digitado = input(
        "\nDigite o ID da habilidade que deseja alterar: "
    ).strip()

    # Verifica se o ID é numérico
    if not id_digitado.isdigit():
        print(
            "Erro: digite apenas o número do ID."
        )
        return

    # Converte para inteiro
    id_digitado = int(id_digitado)

    # Começa sem habilidade encontrada
    habilidade_encontrada = None

    # Procura pelo ID
    for h in habilidades:

        if h.id_habilidade == id_digitado:
            habilidade_encontrada = h
            break

    # Verifica se encontrou
    if habilidade_encontrada is None:
        print("Erro: habilidade não encontrada.")
        return

    # Mostra a habilidade selecionada
    print("\nHabilidade selecionada:")
    print(habilidade_encontrada)

    # Se estiver ativa, inativa
    if habilidade_encontrada.status == "Ativa":

        habilidade_encontrada.inativar()

        print(
            "\nHabilidade inativada com sucesso!"
        )

    # Se estiver inativa, reativa
    else:

        habilidade_encontrada.reativar()

        print(
            "\nHabilidade reativada com sucesso!"
        )

    # Mostra o novo estado
    print(habilidade_encontrada)


# Exclui uma habilidade
def excluir_habilidade(habilidades):

    print(
        "\nDeseja visualizar a lista de habilidades?"
    )
    print("1 - Sim")
    print("2 - Não")

    # Guarda a resposta
    ver_lista = input().strip()

    if ver_lista == "1":
        listar_habilidades(habilidades)

    elif ver_lista == "2":
        pass

    else:
        print(
            "Erro: digite 1 para Sim ou 2 para Não."
        )
        return

    # Pede o ID da habilidade
    id_digitado = input(
        "\nDigite o ID da habilidade que deseja excluir: "
    ).strip()

    # Verifica se o ID é numérico
    if not id_digitado.isdigit():
        print(
            "Erro: digite apenas o número do ID."
        )
        return

    # Converte para inteiro
    id_digitado = int(id_digitado)

    # Procura a habilidade
    habilidade_encontrada = None

    for h in habilidades:

        if h.id_habilidade == id_digitado:
            habilidade_encontrada = h
            break

    # Se não encontrar
    if habilidade_encontrada is None:
        print("Erro: habilidade não encontrada.")
        return

    # Mostra qual habilidade será excluída
    print("\nHabilidade selecionada:")
    print(habilidade_encontrada)

    # Pede confirmação
    print(
        "\nDeseja realmente excluir essa habilidade?"
    )
    print("1 - Sim")
    print("2 - Não")

    confirmar = input().strip()

    # Exclui
    if confirmar == "1":

        habilidades.remove(
            habilidade_encontrada
        )

        print(
            "\nHabilidade excluída com sucesso!"
        )

    # Cancela
    elif confirmar == "2":

        print("\nExclusão cancelada.")

    else:

        print(
            "Erro: digite 1 para Sim ou 2 para Não."
        )


# FUNÇÕES DE VOLUNTÁRIOS


def cadastrar_voluntario(voluntarios):

    # Pede o nome do voluntário
    nome = input("Digite o nome do voluntário: ").strip()

    # Verifica se o nome ficou vazio
    if nome == "":
        print("Erro: o nome do voluntário não pode ficar vazio.")
        return

    # Pede o telefone
    telefone = input("Digite o telefone do voluntário: ").strip()

    # Verifica se o telefone ficou vazio
    if telefone == "":
        print("Erro: o telefone não pode ficar vazio.")
        return

    # Pede o e-mail
    email = input("Digite o e-mail do voluntário: ").strip()

    # Verifica se o e-mail ficou vazio
    if email == "":
        print("Erro: o e-mail não pode ficar vazio.")
        return

    # Descobre o próximo ID
    proximo_id = (
        max(v.id_voluntario for v in voluntarios) + 1
        if voluntarios
        else 1
    )

    # Cria o novo voluntário
    novo_voluntario = Voluntario(
        proximo_id,
        nome,
        telefone,
        email
    )

    # Adiciona o voluntário à lista
    voluntarios.append(novo_voluntario)

    # Confirma o cadastro
    print("\nVoluntário cadastrado com sucesso!")
    print(novo_voluntario)

# Lista todos os voluntários cadastrados
def listar_voluntarios(voluntarios):

    print("\nVoluntários cadastrados:")

    # Percorre a lista de voluntários
    for v in voluntarios:
        print(v)

# Edita os dados de um voluntário
# Função para editar os dados de um voluntário
def editar_voluntario(voluntarios):

    # Pergunta se o usuário deseja visualizar a lista de voluntários
    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    # Guarda a resposta do usuário
    ver_lista = input().strip()

    # Se escolher 1, mostra a lista de voluntários
    if ver_lista == "1":
        listar_voluntarios(voluntarios)

    # Se escolher 2, segue normalmente
    elif ver_lista == "2":
        pass

    # Se digitar qualquer outra opção, mostra erro e encerra a função
    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID do voluntário que será editado
    id_digitado = input(
        "\nDigite o ID do voluntário que deseja editar: "
    ).strip()

    # Verifica se o ID digitado contém apenas números
    if not id_digitado.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID de texto para número inteiro
    id_digitado = int(id_digitado)

    # Começa considerando que nenhum voluntário foi encontrado
    voluntario_encontrado = None

    # Percorre a lista de voluntários procurando o ID informado
    for v in voluntarios:

        # Verifica se o ID do voluntário atual é igual ao ID digitado
        if v.id_voluntario == id_digitado:

            # Guarda o voluntário encontrado
            voluntario_encontrado = v

            # Interrompe o for, pois já encontrou o voluntário
            break

    # Se nenhum voluntário tiver sido encontrado
    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    # Mostra os dados do voluntário selecionado
    print("\nVoluntário selecionado:")
    print(voluntario_encontrado)

    # Mostra quais informações podem ser editadas
    print("\nO que deseja editar?")
    print("1 - Nome")
    print("2 - Telefone")
    print("3 - E-mail")
    print("0 - Cancelar")

    # Guarda a opção escolhida
    opcao_edicao = input().strip()

    # Edita o nome
    if opcao_edicao == "1":

        novo_nome = input(
            "Digite o novo nome do voluntário: "
        ).strip()

        # Impede nome vazio
        if novo_nome == "":
            print("Erro: o nome não pode ficar vazio.")
            return

        # Chama o método da classe Voluntario
        voluntario_encontrado.editar_nome(novo_nome)

        print("\nNome alterado com sucesso!")

    # Edita o telefone
    elif opcao_edicao == "2":

        novo_telefone = input(
            "Digite o novo telefone do voluntário: "
        ).strip()

        # Impede telefone vazio
        if novo_telefone == "":
            print("Erro: o telefone não pode ficar vazio.")
            return

        # Chama o método da classe Voluntario
        voluntario_encontrado.editar_telefone(novo_telefone)

        print("\nTelefone alterado com sucesso!")

    # Edita o e-mail
    elif opcao_edicao == "3":

        novo_email = input(
            "Digite o novo e-mail do voluntário: "
        ).strip()

        # Impede e-mail vazio
        if novo_email == "":
            print("Erro: o e-mail não pode ficar vazio.")
            return

        # Chama o método da classe Voluntario
        voluntario_encontrado.editar_email(novo_email)

        print("\nE-mail alterado com sucesso!")

    # Cancela a edição
    elif opcao_edicao == "0":

        print("\nEdição cancelada.")
        return

    # Caso o usuário digite uma opção inválida
    else:

        print("Erro: opção inválida.")
        return

    # Mostra os dados do voluntário depois da alteração
    print("\nDados atualizados:")
    print(voluntario_encontrado)

# Altera o status de um voluntário
def alterar_status_voluntario(voluntarios):

    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    ver_lista = input().strip()

    if ver_lista == "1":
        listar_voluntarios(voluntarios)

    elif ver_lista == "2":
        pass

    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID do voluntário
    id_digitado = input(
        "\nDigite o ID do voluntário que deseja alterar: "
    ).strip()

    # Verifica se o ID é numérico
    if not id_digitado.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID para inteiro
    id_digitado = int(id_digitado)

    # Procura o voluntário
    voluntario_encontrado = None

    for v in voluntarios:
        if v.id_voluntario == id_digitado:
            voluntario_encontrado = v
            break

    # Verifica se encontrou
    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    # Mostra o voluntário selecionado
    print("\nVoluntário selecionado:")
    print(voluntario_encontrado)

    # Se estiver ativo, inativa
    if voluntario_encontrado.status == "Ativo":
        voluntario_encontrado.inativar()
        print("\nVoluntário inativado com sucesso!")

    # Se estiver inativo, reativa
    else:
        voluntario_encontrado.reativar()
        print("\nVoluntário reativado com sucesso!")

    # Mostra o novo status
    print(voluntario_encontrado)

# Função responsável por excluir um voluntário
def excluir_voluntario(voluntarios):

    # Pergunta se o usuário deseja visualizar a lista de voluntários
    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    # Guarda a resposta digitada pelo usuário
    ver_lista = input().strip()

    # Se o usuário digitar 1, mostra a lista de voluntários cadastrados
    if ver_lista == "1":
        listar_voluntarios(voluntarios)

    # Se digitar 2, continua sem mostrar a lista
    elif ver_lista == "2":
        pass

    # Se digitar qualquer outra coisa, mostra erro e encerra a função
    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID do voluntário que será excluído
    id_digitado = input(
        "\nDigite o ID do voluntário que deseja excluir: "
    ).strip()

    # Verifica se o usuário digitou apenas números
    if not id_digitado.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID de texto para número inteiro
    id_digitado = int(id_digitado)

    # Começa considerando que nenhum voluntário foi encontrado
    voluntario_encontrado = None

    # Percorre a lista de voluntários procurando o ID informado
    for v in voluntarios:

        # Verifica se o ID do voluntário atual é igual ao ID digitado
        if v.id_voluntario == id_digitado:

            # Guarda o objeto do voluntário encontrado
            voluntario_encontrado = v

            # Interrompe o for, pois o voluntário já foi encontrado
            break

    # Se nenhum voluntário tiver sido encontrado
    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    # Mostra os dados do voluntário antes da exclusão
    print("\nVoluntário selecionado:")
    print(voluntario_encontrado)

    # Pede confirmação antes de excluir
    print("\nDeseja realmente excluir esse voluntário?")
    print("1 - Sim")
    print("2 - Não")

    # Guarda a resposta da confirmação
    confirmar = input().strip()

    # Se o usuário confirmar
    if confirmar == "1":

        # Remove o objeto do voluntário da lista
        voluntarios.remove(voluntario_encontrado)

        # Informa que a exclusão foi realizada
        print("\nVoluntário excluído com sucesso!")

    # Se o usuário não quiser excluir
    elif confirmar == "2":

        # Cancela a exclusão sem alterar a lista
        print("\nExclusão cancelada.")

    # Se digitar uma opção diferente de 1 ou 2
    else:

        print("Erro: digite 1 para Sim ou 2 para Não.")

# Associa uma habilidade a um voluntário
def associar_habilidade_voluntario(voluntarios, habilidades):

    # Pergunta se o usuário deseja visualizar a lista de voluntários
    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    ver_voluntarios = input().strip()

    if ver_voluntarios == "1":
        listar_voluntarios(voluntarios)

    elif ver_voluntarios == "2":
        pass

    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID do voluntário
    id_voluntario = input(
        "\nDigite o ID do voluntário: "
    ).strip()

    # Verifica se foi digitado apenas número
    if not id_voluntario.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID para inteiro
    id_voluntario = int(id_voluntario)

    # Procura o voluntário
    voluntario_encontrado = None

    for v in voluntarios:
        if v.id_voluntario == id_voluntario:
            voluntario_encontrado = v
            break

    # Verifica se encontrou o voluntário
    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    # Pergunta se o usuário deseja visualizar as habilidades
    print("\nDeseja visualizar a lista de habilidades?")
    print("1 - Sim")
    print("2 - Não")

    ver_habilidades = input().strip()

    if ver_habilidades == "1":
        listar_habilidades(habilidades)

    elif ver_habilidades == "2":
        pass

    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID da habilidade
    id_habilidade = input(
        "\nDigite o ID da habilidade que deseja associar: "
    ).strip()

    # Verifica se foi digitado apenas número
    if not id_habilidade.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID para inteiro
    id_habilidade = int(id_habilidade)

    # Procura a habilidade
    habilidade_encontrada = None

    for h in habilidades:
        if h.id_habilidade == id_habilidade:
            habilidade_encontrada = h
            break

    # Verifica se encontrou a habilidade
    if habilidade_encontrada is None:
        print("Erro: habilidade não encontrada.")
        return

    # Impede associar habilidades inativas
    if habilidade_encontrada.status == "Inativa":
        print("Erro: não é possível associar uma habilidade inativa.")
        return

    # Verifica se o voluntário já possui essa habilidade
    if habilidade_encontrada in voluntario_encontrado.habilidades:
        print("Erro: o voluntário já possui essa habilidade.")
        return

    # Adiciona a habilidade ao voluntário
    voluntario_encontrado.adicionar_habilidade(
        habilidade_encontrada
    )

    print("\nHabilidade associada ao voluntário com sucesso!")

# Remove uma habilidade de um voluntário
def remover_habilidade_voluntario(voluntarios):

    # Pergunta se o usuário deseja visualizar a lista de voluntários
    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    ver_voluntarios = input().strip()

    if ver_voluntarios == "1":
        listar_voluntarios(voluntarios)

    elif ver_voluntarios == "2":
        pass

    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID do voluntário
    id_voluntario = input(
        "\nDigite o ID do voluntário: "
    ).strip()

    # Verifica se o ID contém apenas números
    if not id_voluntario.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID para inteiro
    id_voluntario = int(id_voluntario)

    # Procura o voluntário
    voluntario_encontrado = None

    for v in voluntarios:
        if v.id_voluntario == id_voluntario:
            voluntario_encontrado = v
            break

    # Verifica se encontrou o voluntário
    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    # Verifica se o voluntário possui alguma habilidade
    if not voluntario_encontrado.habilidades:
        print("Esse voluntário não possui habilidades cadastradas.")
        return

    # Mostra as habilidades que pertencem ao voluntário
    print("\nHabilidades do voluntário:")

    for h in voluntario_encontrado.habilidades:
        print(h)

    # Pede o ID da habilidade que será removida
    id_habilidade = input(
        "\nDigite o ID da habilidade que deseja remover: "
    ).strip()

    # Verifica se o ID contém apenas números
    if not id_habilidade.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID para inteiro
    id_habilidade = int(id_habilidade)

    # Procura a habilidade dentro das habilidades do voluntário
    habilidade_encontrada = None

    for h in voluntario_encontrado.habilidades:
        if h.id_habilidade == id_habilidade:
            habilidade_encontrada = h
            break

    # Verifica se encontrou a habilidade
    if habilidade_encontrada is None:
        print("Erro: esse voluntário não possui essa habilidade.")
        return

    # Remove a habilidade usando o método da classe Voluntario
    voluntario_encontrado.remover_habilidade(
        habilidade_encontrada
    )

    # Confirma a remoção
    print("\nHabilidade removida do voluntário com sucesso!")


# FUNÇÕES DE DISPONIBILIDADE

# Cadastra uma nova disponibilidade para um voluntário
def cadastrar_disponibilidade(voluntarios):

    # Pergunta se o usuário deseja visualizar a lista de voluntários
    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    ver_lista = input().strip()

    # Mostra os voluntários cadastrados
    if ver_lista == "1":
        listar_voluntarios(voluntarios)

    # Continua sem mostrar a lista
    elif ver_lista == "2":
        pass

    # Impede uma opção diferente de 1 ou 2
    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    # Pede o ID do voluntário
    id_voluntario = input(
        "\nDigite o ID do voluntário: "
    ).strip()

    # Verifica se o ID contém apenas números
    if not id_voluntario.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    # Converte o ID de texto para número inteiro
    id_voluntario = int(id_voluntario)

    # Começa considerando que nenhum voluntário foi encontrado
    voluntario_encontrado = None

    # Procura o voluntário pelo ID
    for v in voluntarios:

        if v.id_voluntario == id_voluntario:
            voluntario_encontrado = v
            break

    # Verifica se encontrou o voluntário
    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    # Mostra as opções de dias da semana
    print("\nEscolha o dia da semana:")
    print("1 - Segunda-feira")
    print("2 - Terça-feira")
    print("3 - Quarta-feira")
    print("4 - Quinta-feira")
    print("5 - Sexta-feira")
    print("6 - Sábado")
    print("7 - Domingo")

    # Guarda a opção escolhida
    opcao_dia = input().strip()

    # Relaciona cada número ao nome do dia
    dias_semana = {
        "1": "Segunda-feira",
        "2": "Terça-feira",
        "3": "Quarta-feira",
        "4": "Quinta-feira",
        "5": "Sexta-feira",
        "6": "Sábado",
        "7": "Domingo"
    }

    # Verifica se a opção existe
    if opcao_dia not in dias_semana:
        print("Erro: escolha um número de 1 a 7.")
        return

    # Guarda o nome correspondente ao dia escolhido
    dia_semana = dias_semana[opcao_dia]

    # Pede o horário inicial
    hora_inicio = input(
        "Digite o horário inicial (HH:MM): "
    ).strip()

    # Pede o horário final
    hora_fim = input(
        "Digite o horário final (HH:MM): "
    ).strip()

    # Cria uma lista com todos os IDs de disponibilidade já existentes
    ids_existentes = []

    for v in voluntarios:

        for d in v.disponibilidades:
            ids_existentes.append(d.id_disponibilidade)

    # Define o próximo ID disponível
    proximo_id = (
        max(ids_existentes) + 1
        if ids_existentes
        else 1
    )

    # Cria o objeto Disponibilidade
    nova_disponibilidade = Disponibilidade(
        proximo_id,
        dia_semana,
        hora_inicio,
        hora_fim
    )

    # Adiciona a disponibilidade ao voluntário
    voluntario_encontrado.adicionar_disponibilidade(
        nova_disponibilidade
    )

    # Confirma o cadastro
    print("\nDisponibilidade cadastrada com sucesso!")
    print(nova_disponibilidade)

    try:
        horario_inicio = datetime.strptime(hora_inicio, "%H:%M")
        horario_fim = datetime.strptime(hora_fim, "%H:%M")
    except ValueError:
        print("Erro: formato de horário inválido. Use HH:MM.")
        return
    if horario_inicio >= horario_fim:
        print("Erro: O horário inicial deve ser posterior ao horário final")
    return

def listar_disponibilidades(voluntarios):

    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    ver_lista = input().strip()

    if ver_lista == "1":
        listar_voluntarios(voluntarios)

    elif ver_lista == "2":
        pass

    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    id_voluntario = input(
        "\nDigite o ID do voluntário: "
    ).strip()

    if not id_voluntario.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    id_voluntario = int(id_voluntario)

    voluntario_encontrado = None

    for v in voluntarios:
        if v.id_voluntario == id_voluntario:
            voluntario_encontrado = v
            break

    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    if not voluntario_encontrado.disponibilidades:
        print("Esse voluntário não possui disponibilidades cadastradas.")
        return

    print(f"\nDisponibilidades de {voluntario_encontrado.nome}:")

    for d in voluntario_encontrado.disponibilidades:
        print(d)

def editar_disponibilidade(voluntarios):

    print("\nDeseja visualizar a lista de voluntários?")
    print("1 - Sim")
    print("2 - Não")

    ver_lista = input().strip()

    if ver_lista == "1":
        listar_voluntarios(voluntarios)

    elif ver_lista == "2":
        pass

    else:
        print("Erro: digite 1 para Sim ou 2 para Não.")
        return

    id_voluntario = input(
        "\nDigite o ID do voluntário: "
    ).strip()

    if not id_voluntario.isdigit():
        print("Erro: digite apenas o número do ID.")
        return

    id_voluntario = int(id_voluntario)

    voluntario_encontrado = None

    for v in voluntarios:
        if v.id_voluntario == id_voluntario:
            voluntario_encontrado = v
            break

    if voluntario_encontrado is None:
        print("Erro: voluntário não encontrado.")
        return

    if not voluntario_encontrado.disponibilidades:
        print("Esse voluntário não possui disponibilidades cadastradas.")
        return

    print(f"\nDisponibilidades de {voluntario_encontrado.nome}:")

    for d in voluntario_encontrado.disponibilidades:
        print(d)

    id_disponibilidade = input(
        "\nDigite o ID da disponibilidade que deseja editar: ").strip()
    
    if not id_disponibilidade.isdigit():
        print("Erro: digite apenas o número do ID.")
        return
    
    id_disponibilidade = int(id_disponibilidade)   

    for d in voluntario_encontrado.disponibilidades:
        if d.id_disponibilidade == id_disponibilidade:
            disponibilidade_encontrada = d
            break   
    if disponibilidade_encontrada is None:
        print("Erro: disponibilidade não encontrada.")
        return

    print("\nDisponibilidade selecionada:")
    print(disponibilidade_encontrada)

    print("\nO que deseja editar?")
    print("1 - Dia da semana")
    print("2 - Horário inicial")
    print("3 - Horário final")
    print("0 - Cancelar")

    opcao_edicao = input().strip()

    if opcao_edicao == "1":
        print("\nEscolha o novo dia da semana:")
        print("1 - Segunda-feira")
        print("2 - Terça-feira")
        print("3 - Quarta-feira")
        print("4 - Quinta-feira")
        print("5 - Sexta-feira")
        print("6 - Sábado")
        print("7 - Domingo")

        opcao_dia = input().strip()

        dias_semana = {
            "1": "Segunda-feira",
            "2": "Terça-feira",
            "3": "Quarta-feira",
            "4": "Quinta-feira",
            "5": "Sexta-feira",
            "6": "Sábado",
            "7": "Domingo"
        }

        if opcao_dia not in dias_semana:
            print("Erro: escolha um número de 1 a 7.")
            return

        disponibilidade_encontrada.dia_semana = dias_semana[opcao_dia]

        print("\nDia da semana alterado com sucesso!")

    elif opcao_edicao == "2":

        print("O que deseja alterar? ")
        print("1 - Alterar apenas o horário inicial")
        print("2 - Alterar apenas o horário final")
        print("3 - Alterar o horário inicial e o horário final")
        print("0 - Cancelar")

        opcao_horario = input().strip()

        if opcao_horario == "1":
            novo_horario_inicio = input("Digite o novo horário inicial (HH:MM): ").strip()
            try:
                    horario_fim = datetime.strptime(disponibilidade_encontrada.hora_fim, "%H:%M")
                    horario_inicio = datetime.strptime(novo_horario_inicio, "%H:%M")
            except ValueError:
                    print("Erro: formato de horário inválido. Use HH:MM.")
                    return
            if horario_inicio >= horario_fim:
                print("Erro: O horário inicial deve ser anterior ao horário final.")
                return

            disponibilidade_encontrada.hora_inicio = novo_horario_inicio
            print("\nHorário inicial alterado com sucesso!")

        elif opcao_horario == "2":
            novo_horario_fim = input("Digite o novo horário final (HH:MM): ").strip()

            try:
                horario_inicio = datetime.strptime(disponibilidade_encontrada.hora_inicio, "%H:%M")
                horario_fim = datetime.strptime(novo_horario_fim, "%H:%M")
            except ValueError:
                print("Erro: formato de horário inválido. Use HH:MM.")
                return
            if horario_fim <= horario_inicio:
                print("Erro: O horário final deve ser posterior ao horário inicial.")
                return
            disponibilidade_encontrada.hora_fim = novo_horario_fim
            print("\nHorário final alterado com sucesso!")


        elif opcao_horario == "3":
            novo_horario_inicio = input("Digite o novo horário inicial (HH:MM): ").strip()
            novo_horario_fim = input("Digite o novo horário final (HH:MM): ").strip()
            try:
                horario_inicio = datetime.strptime(novo_horario_inicio, "%H:%M")
                horario_fim = datetime.strptime(novo_horario_fim, "%H:%M")
            except ValueError:
                print("Erro: formato de horário inválido. Use HH:MM.")
                return
            
            if horario_inicio >= horario_fim:
                print("Erro: O horário inicial deve ser anterior ao horário final.")
                return

            disponibilidade_encontrada.hora_inicio = novo_horario_inicio    
            disponibilidade_encontrada.hora_fim = novo_horario_fim
            print("\nHorários alterados com sucesso!")

        elif opcao_horario == "0":
            print("\nEdição cancelada.")
            return
        else:
            print("Erro: opção inválida, digite 1, 2, 3 ou 0.")
            return

        print(
        f"\nDisponibilidade {disponibilidade_encontrada.id_disponibilidade} "
        f"de {voluntario_encontrado.nome} editada para:" )
        print(disponibilidade_encontrada)