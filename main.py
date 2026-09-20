# Importa a classe habilidade
from habilidade import habilidade

# Importa o menu principal
from menu import menu_principal



# DADOS DE HABILIDADES

# Habilidades que já vêm cadastradas no sistema
habilidades_padrao = [
    "Comunicação",
    "Organização",
    "Trabalho em equipe",
    "Informática",
    "Atendimento ao público",
    "Educação",
    "Cuidados com idosos",
    "Cuidados com animais",
    "Cozinha",
    "Gestão"
]


# Lista que armazena as habilidades
habilidades = []


# Cria automaticamente as habilidades padrão
for id_habilidade, nome in enumerate(
    habilidades_padrao,
    start=1
):

    habilidades.append(
        habilidade(id_habilidade, nome)
    )



# DADOS DE VOLUNTÁRIOS

# Lista que vai armazenar os voluntários cadastrados
voluntarios = []



# INÍCIO DO SISTEMA

# Inicia o menu principal e envia as listas do sistema
menu_principal(
    habilidades,
    voluntarios
)