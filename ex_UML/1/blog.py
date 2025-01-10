from postagem import Postagem

class Blog:
    def __init__(self):
        self.postagem = []
    
    def listarPostagens(self, postagem, usuarioAutenticado):
        if usuarioAutenticado:
            self.postagem.append(postagem)
        else: 
            print(f'Usuário não autenticado! ')

post = Postagem(1, "First post", "esse é meu primeiro post", "12/12/24")