# Cria a classe Voluntario, que servirá como modelo
# para todos os voluntários cadastrados no sistema
class Voluntario:

    # Método construtor
    def __init__(self, id_voluntario, nome, telefone, email):

        self.id_voluntario = id_voluntario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.status = "Ativo"

        # Lista que vai armazenar as habilidades do voluntário
        self.habilidades = []
        # Todo novo voluntário começa ativo
        self.status = "Ativo"

    # Altera os dados do voluntário
    def editar_nome(self, novo_nome):
        self.nome = novo_nome

    def editar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def editar_email(self, novo_email):
        self.email = novo_email

    # Inativa o voluntário
    def inativar(self):
        self.status = "Inativo"

    # Reativa o voluntário
    def reativar(self):
        self.status = "Ativo"

    # Define como o voluntário será exibido
    def __str__(self):

        # Verifica se o voluntário possui habilidades cadastradas
        if self.habilidades:

            # Junta os nomes das habilidades em um único texto
            nomes_habilidades = ", ".join(
                h.nome for h in self.habilidades
            )

        else:

            # Caso o voluntário ainda não tenha nenhuma habilidade
            nomes_habilidades = "Nenhuma"

        # Retorna os dados do voluntário
        return (
            f"ID: {self.id_voluntario} - "
            f"Nome: {self.nome}, "
            f"Telefone: {self.telefone}, "
            f"E-mail: {self.email}, "
            f"Status: {self.status}, "
            f"Habilidades: {nomes_habilidades}"
        )
    
    # Adiciona uma habilidade ao voluntário
    def adicionar_habilidade(self, habilidade):
            self.habilidades.append(habilidade)


        # Remove uma habilidade do voluntário
    def remover_habilidade(self, habilidade):
            self.habilidades.remove(habilidade)

