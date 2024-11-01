class categoria:
    def __init__(self, nome, desconto):
        self.nome = nome
        self.desconto = desconto
    
    def aplicar_desconto(self, preco):
        preco = preco - (preco * (self.desconto/100))
        return preco


class produto(categoria):
    def __init__(self, nome, preco, estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria
    
    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade
        return self.estoque
    
    def remover_estoque(self, quantidade):
        if self.estoque < quantidade:
            print(f'Estoque insuficiente! possui apenas {self.estoque} peças')
            return
        else:
            self.estoque -= quantidade
            return self.estoque
    def preco_desconto(self):
        return self.aplicar_desconto

class pedido:
    def __init__(self):
        self.produto = []
        self.quantidade = {}
    
    def adicionar_produto(self, produto, quantidade):
        if produto not in self.produto:
            self.produto.append(produto)
        if produto in self.quantidade:
            self.quantidade[produto] += quantidade
        else:
            self.quantidade[produto] = quantidade

    def excluir_produto(self, produto, quantidade):
            #terminar
            a = 1




    def exibir(self):
        print("ITENS:")
        for produto, quantidade in self.quantidade.items():
            print(f'{produto}, {quantidade} Unidade(s)')
    

pedido = pedido()
pedido.adicionar_produto('Produto A', 3)
pedido.adicionar_produto('Produto B', 4)
pedido.exibir()
