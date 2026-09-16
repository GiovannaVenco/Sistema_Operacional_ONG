# Cria a classe Habilidade, que servirá como modelo
# para todas as habilidades cadastradas no sistema
class habilidade:
     # Método construtor:
     # é executado automaticamente sempre que uma nova habilidade é criada
    def __init__(self, id_habilidade, nome):
        # Guarda o nome informado dentro da habilidade que está sendo criada
        self.nome = nome
        self.id_habilidade = id_habilidade
        self.status = "Ativa"
        # Toda nova habilidade começa com o status "Ativa"
    def editar_nome (self, novo_nome):
        # Altera o nome da habilidade para o novo nome informado
        self.nome = novo_nome
    def inativar (self):
        # Altera o status da habilidade para "Inativa"
        self.status = "Inativa"
    def reativar (self):
        # Altera o status da habilidade para "Ativa"
        self.status = "Ativa"
    def __str__(self):
        # Retorna uma representação em string da habilidade
        return f"ID: {self.id_habilidade} - Habilidade: {self.nome}, Status: {self.status}"
