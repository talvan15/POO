from itemPedido import ItemPedido

class Pedido:
    def __init__(self):
        self.itens = []
        self.valor_total = 0.0

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)
        self.valor_total += item.calcular_total()

    def obter_total(self) -> float:
        return self.valor_total
