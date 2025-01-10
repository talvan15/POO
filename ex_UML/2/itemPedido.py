from produto import Produto
class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_total(self) -> float:
        return self.produto.valor * self.quantidade
