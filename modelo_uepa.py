class MembroUEPA:
    """
    Classe base para membros da comunidade UEPA (Universidade do Estado do Pará).
    Representa a abstração com atributos comuns a alunos e professores.
    """
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        """Método genérico para apresentar o membro."""
        return f"Olá, eu sou {self.nome}, um membro da UEPA."

class Aluno(MembroUEPA):
    """
    Classe que representa um Aluno da UEPA.
    Herda de MembroUEPA e adiciona atributos e métodos específicos.
    """
    def __init__(self, nome, matricula, email, curso):
        # Chama o construtor da classe pai usando super()
        super().__init__(nome, matricula, email)
        self.curso = curso
    
    def apresentar(self):
        """Sobrescreve o método apresentar para fornecer uma apresentação específica de Aluno."""
        return f"Olá, sou {self.nome}, aluno(a) do curso de {self.curso} na UEPA."
    
    def verificar_notas(self):
        """Método específico de Aluno para verificar notas."""
        return f"O(A) aluno(a) {self.nome} está verificando suas notas."

class Professor(MembroUEPA):
    """
    Classe que representa um Professor da UEPA.
    Herda de MembroUEPA e adiciona atributos e métodos específicos.
    """
    def __init__(self, nome, matricula, email, departamento):
        # Chama o construtor da classe pai usando super()
        super().__init__(nome, matricula, email)
        self.departamento = departamento
    
    def apresentar(self):
        """Sobrescreve o método apresentar para fornecer uma apresentação específica de Professor."""
        return f"Olá, sou {self.nome}, professor(a) do departamento de {self.departamento} na UEPA."
    
    def lancar_frequencia(self):
        """Método específico de Professor para lançar frequência."""
        return f"O(A) professor(a) {self.nome} está lançando a frequência dos alunos."

# --- Área de Testes ---
if __name__ == "__main__":
    # Instanciando um objeto Aluno
    aluno1 = Aluno(nome="Maria Silva", matricula="2023001", email="maria.s@uepa.br", curso="Engenharia de Software")

    # Instanciando um objeto Professor
    professor1 = Professor(nome="João Souza", matricula="1998010", email="joao.s@uepa.br", departamento="Ciência da Computação")

    # Demonstrando o uso dos métodos
    print("--- Teste do Aluno ---")
    print(aluno1.apresentar())
    print(aluno1.verificar_notas())
    print("-" * 20)

    print("--- Teste do Professor ---")
    print(professor1.apresentar())
    print(professor1.lancar_frequencia())
    print("-" * 20)