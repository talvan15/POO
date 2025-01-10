from produto import Produto
from itemPedido import ItemPedido
from pedido import Pedido

produto1 = Produto(1, 10.0, "Caderno")
produto2 = Produto(2, 5.0, "Caneta")

item1 = ItemPedido(produto1, 2) 
item2 = ItemPedido(produto2, 3) 

pedido = Pedido()
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)


print(f"Total do pedido: R${pedido.obter_total():.2f}")
