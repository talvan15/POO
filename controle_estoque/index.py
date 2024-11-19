#SISTEMA DE CONTROLE DE ESTOQUE PARA UMA  LOJA DE ANIMAIS
class produto:
    def __init__(self, nome, preco, qtd_em_estoque):
        self.nome = nome
        self.preco = preco
        self.qtd_em_estoque = qtd_em_estoque

    def vender(self, quantidade):
        if quantidade <= self.qtd_em_estoque:
            self.qtd_em_estoque -= quantidade
        else: print(f'Operacao não realizada: quantidade disponível: {self.qtd_em_estoque}')

    def ReporEstoque(self, quantidade):
        self.qtd_em_estoque += quantidade

    def exibir_informacoes(self):
        print(f'Produto: {self.nome}\nPreço: R${self.preco}\nQuantidade: {self.qtd_em_estoque}')

class racao(produto):
    def __init__(self, nome, preco, qtd_em_estoque,tipo_animal, peso):
        super().__init__(nome, preco, qtd_em_estoque)
        self.tipo_animal = tipo_animal
        self.peso = peso
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Tipo do animal: {self.tipo_animal}')
        print(f'Peso: {self.peso} Kg')

class brinquedo(produto):
    def __init__(self, nome, preco, qtd_em_estoque, material, faixa_etaria):
        super().__init__(nome, preco, qtd_em_estoque)
        self.material = material
        self.faixa_etaria = faixa_etaria

    def exibir_informacoes(self):
        print(f'Produto: {self.nome}\nPreço: R${self.preco}\nQuantidade em estoque: {self.qtd_em_estoque}\nMaterial: {self.material}\nFaixa etária: {self.faixa_etaria}')

class medicamento(produto):
    def __init__(self, nome, preco, qtd_em_estoque, tipo, dosagem):
        super().__init__(nome, preco, qtd_em_estoque)
        self.tipo = tipo
        self.dosagem = dosagem

class acessorio(produto):
    def __init__(self, nome, preco, qtd_em_estoque, categoria, tamanho):
        super().__init__(nome, preco, qtd_em_estoque)
        self.categoria = categoria
        self.tamanho = tamanho



def menu():
    produtos = []
    while True:
        print("\n--- Menu de Controle de Estoque ---")
        print("1. Cadastrar Ração")
        print("2. Cadastrar Brinquedo")
        print("3. Cadastrar Medicamento")
        print("4. Cadastrar Acessório")
        print("5. Consultar Estoque")
        print("6. Realizar Venda")
        print("7. Repor Estoque")
        print("8. Exibir Alerta de Estoque Baixo")
        print("9. Relatório de Produtos Mais Vendidos")
        print("10. Sair")
        acao = input("Escolha uma opção: ")
        
        match acao:
            case "1":
                # Cadastro de Ração
                nome = input("Nome da ração: ")
                preco = float(input("Preço da ração: "))
                quantidade = int(input("Quantidade em estoque: "))
                tipo_animal = input("Tipo de animal: ")
                peso = float(input("Peso da ração (kg): "))
                produtos.append(racao(nome, preco, quantidade, tipo_animal, peso))
                print("Ração cadastrada com sucesso!")

            case "2":
                # Cadastro de Brinquedo
                nome = input("Nome do brinquedo: ")
                preco = float(input("Preço do brinquedo: "))
                quantidade = int(input("Quantidade em estoque: "))
                material = input("Material do brinquedo: ")
                faixa_etaria = input("Faixa etária: ")
                produtos.append(brinquedo(nome, preco, quantidade, material, faixa_etaria))
                print("Brinquedo cadastrado com sucesso!")

            case "3":
                # Cadastro de Medicamento
                nome = input("Nome do medicamento: ")
                preco = float(input("Preço do medicamento: "))
                quantidade = int(input("Quantidade em estoque: "))
                tipo = input("Tipo do medicamento: ")
                dosagem = input("Dosagem: ")
                produtos.append(medicamento(nome, preco, quantidade, tipo, dosagem))
                print("Medicamento cadastrado com sucesso!")

            case "4":
                # Cadastro de Acessório
                nome = input("Nome do acessório: ")
                preco = float(input("Preço do acessório: "))
                quantidade = int(input("Quantidade em estoque: "))
                categoria = input("Categoria do acessório: ")
                tamanho = input("Tamanho: ")
                produtos.append(acessorio(nome, preco, quantidade, categoria, tamanho))
                print("Acessório cadastrado com sucesso!")

            case "5":
                nome = input("Nome do produto para consulta: ")
                for produto in produtos:
                    if produto.nome.lower() == nome.lower():
                        produto.exibir_informacoes()
                        break
                else:
                    print("Produto não encontrado.")

            case "6":
                nome = input("Nome do produto para venda: ")
                quantidade = int(input("Quantidade a vender: "))
                for produto in produtos:
                    if produto.nome.lower() == nome.lower():
                        produto.vender(quantidade)
                        break
                else:
                    print("Produto não encontrado.")

            case "7":
                nome = input("Nome do produto para repor estoque: ")
                quantidade = int(input("Quantidade a repor: "))
                for produto in produtos:
                    if produto.nome.lower() == nome.lower():
                        produto.repor_estoque(quantidade)
                        break
                else:
                    print("Produto não encontrado.")

            case "8":
                limite = int(input("Informe o limite mínimo para alerta: "))
                for produto in produtos:
                    produto.verificar_estoque_baixo(limite)

            case "9":
                produtos_ordenados = sorted(produtos, key=lambda p: p.vendidos, reverse=True)
                print("\n--- Produtos Mais Vendidos ---")
                for produto in produtos_ordenados:
                    if produto.vendidos > 0:
                        print(f"{produto.nome}: {produto.vendidos} unidades vendidas")
                    else:
                        print(f"{produto.nome}: Nenhuma unidade vendida")

            case "10":
                print("Saindo do programa...")
                break

            case _:
                print("Opção inválida! Tente novamente.")


menu()


