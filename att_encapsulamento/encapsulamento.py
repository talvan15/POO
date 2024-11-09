from datetime import datetime
class livro:
    def __init__(self, titulo, autor, ano_publicacao, isbn, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.__isbn = isbn
        self.__disponivel = disponivel

    def get_isbn(self):
      print(self.__isbn)
      return self.__isbn
    
    def set_isbn(self, new_isbn):
        
        new_isbn = str(new_isbn)

        if len(new_isbn) == 13:
            self.__isbn = new_isbn
            print(f'ISBN alterado para {self.__isbn}')
            return self.__isbn
        else:
            print(F'O numero digitado não tem 13 dígitos! ')
            return
    
    def emprestar(self):
        self.__disponivel = False
        print(f'O livro não está disponível para empréstimo! ')
        return False

    def devolver(self):
        self.__disponivel = True
        print(f'O livro foi devolvido e está disponivel!')
        return True
    
    def exibir_informacoes(self):
        print(f'INFORMAÇÕES DO LIVRO ')
        print(f'Titulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano_publicacao}\nDisponibilidade: {self.__disponivel}\n')


class autor:
    def __init__(self, nome, nascimento, nacionalidade):
        self.nome = nome
        self.__nascimento = nascimento
        self.nacionalidade = nacionalidade 

    def get_data_nascimento(self):
        print(f'Data de nascimento: {self.__nascimento}')
        return self.__nascimento

    def set_data_nascimento(self, new_data):
        try:
            format_data = datetime.strptime(new_data, "%d,%m,%y")
            self.__nascimento = format_data
            return self.__nascimento

        except ValueError:
            print('Formato incompatível, informe a data no formato: (DD,MM,YY)')
    def exibir_informacoes(self):
        print("INFORMAÇÕS DO AUTOR")
        print(f'Nome: {self.nome}\nNascimento: {self.__nascimento}\nNacionalidade: {self.nacionalidade}')


#class usuarios:
 #   def __init__(self ):










