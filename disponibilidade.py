# Cria a classe Disponibilidade, que representa
# um período em que o voluntário está disponível
class Disponibilidade:

    # Método construtor
    def __init__(
        self,
        id_disponibilidade,
        dia_semana,
        hora_inicio,
        hora_fim
    ):

        # Guarda o ID da disponibilidade
        self.id_disponibilidade = id_disponibilidade

        # Guarda o dia da semana
        self.dia_semana = dia_semana

        # Guarda o horário inicial
        self.hora_inicio = hora_inicio

        # Guarda o horário final
        self.hora_fim = hora_fim

    # Define como a disponibilidade será exibida
    def __init__(self, id_voluntario, nome, telefone, email):

        self.id_voluntario = id_voluntario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.status = "Ativo"

        # Lista que armazena as habilidades do voluntário
        self.habilidades = []

        # Lista que armazena as disponibilidades do voluntário
        self.disponibilidades = []

    # Adiciona uma disponibilidade ao voluntário
def adicionar_disponibilidade(self, disponibilidade):

    self.disponibilidades.append(disponibilidade)


# Remove uma disponibilidade do voluntário
def remover_disponibilidade(self, disponibilidade):

    self.disponibilidades.remove(disponibilidade)
    