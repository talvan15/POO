from datetime import datetime
class livro:
    def __init__(self, titulo, autor, ano_publicacao, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.__isbn = isbn
        self.__disponivel = True


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


class Usuario:
    id_contador = 1 

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.__id_usuario = Usuario.id_contador
        Usuario.id_contador += 1
        self.__livros_emprestados = []

    def get_id_usuario(self):
        return self.__id_usuario

    def emprestar_livro(self, livro):
        if livro not in self.__livros_emprestados and livro.__disponivel:
            livro.emprestar()
            self.__livros_emprestados.append(livro)
        else:
            print("O livro não está disponível ou já foi emprestado.")

    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            livro.devolver()
            self.__livros_emprestados.remove(livro)
        else:
            print("O livro não foi emprestado por este usuário.")

    def exibir_informacoes(self):
        livros = ", ".join([livro.titulo for livro in self.__livros_emprestados]) if self.__livros_emprestados else "Nenhum livro emprestado"
        print(f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Livros Emprestados: {livros}")


class SistemaBiblioteca:
    def __init__(self):
        self.livros = []
        self.autores = []
        self.usuarios = []

    def cadastrar_livro(self, titulo, autor, ano_publicacao, isbn):
        novo_livro = livro(titulo, autor, ano_publicacao, isbn)
        self.livros.append(novo_livro)

    def cadastrar_autor(self, nome, data_nascimento, nacionalidade):
        novo_autor = autor(nome, data_nascimento, nacionalidade)
        self.autores.append(novo_autor)

    def cadastrar_usuario(self, nome, endereco, telefone, id_usuario):
        novo_usuario = Usuario(nome, endereco, telefone, id_usuario)
        self.usuarios.append(novo_usuario)

    def pesquisar_livro(self, criterio, valor):
        for livro in self.livros:
            if (criterio == "titulo" and livro.titulo == valor) or \
               (criterio == "autor" and livro.autor == valor) or \
               (criterio == "isbn" and livro.get_isbn() == valor):
                livro.exibir_informacoes()

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1. Cadastrar Livro")
            print("2. Cadastrar Autor")
            print("3. Cadastrar Usuário")
            print("4. Empréstimo de Livro")
            print("5. Devolução de Livro")
            print("6. Pesquisar Livro")
            print("7. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                titulo = input("Título do Livro: ")
                autor = input("Autor do Livro: ")
                ano_publicacao = int(input("Ano de Publicação: "))
                isbn = input("ISBN do Livro: ")
                self.cadastrar_livro(titulo, autor, ano_publicacao, isbn)
            elif escolha == "2":
                nome = input("Nome do Autor: ")
                data_nascimento = input("Data de Nascimento (DD-MM-AAAA): ")
                nacionalidade = input("Nacionalidade: ")
                self.cadastrar_autor(nome, data_nascimento, nacionalidade)
            elif escolha == "3":
                nome = input("Nome do Usuário: ")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                id_usuario = int(input("ID do Usuário: "))
                self.cadastrar_usuario(nome, endereco, telefone, id_usuario)
            elif escolha == "4":
                id_usuario = int(input("ID do Usuário: "))
                isbn = input("ISBN do Livro: ")
                usuario = next((u for u in self.usuarios if u.get_id_usuario() == id_usuario), None)
                livro = next((l for l in self.livros if l.get_isbn() == isbn), None)
                if usuario and livro:
                    usuario.emprestar_livro(livro)
            elif escolha == "5":
                id_usuario = int(input("ID do Usuário: "))
                isbn = input("ISBN do Livro: ")
                usuario = next((u for u in self.usuarios if u.get_id_usuario() == id_usuario), None)
                livro = next((l for l in self.livros if l.get_isbn() == isbn), None)
                if usuario and livro:
                    usuario.devolver_livro(livro)
            elif escolha == "6":
                criterio = input("Pesquisar por (titulo/autor/isbn): ")
                valor = input("Valor da busca: ")
                self.pesquisar_livro(criterio, valor)
            elif escolha == "7":
                break
            else:
                print("Opção inválida!")

biblioteca = SistemaBiblioteca()
biblioteca.exibir_menu()












