class ContaBancaria:
    def __init__(self, titular, saldo, numeroConta):
        self.titular = titular
        self.saldo = saldo
        self.numeroConta = numeroConta

    def depositar(self, valor:float):
        self.saldo += valor

    def sacar(self, valor:float):
        if self.saldo >= valor: 
            self.saldo-= valor
        else: return "Saldo insuficiente"
    
    def exibirSaldo(self):
        print(f"Seu saldo é de: R$ {self.saldo:.2f} ")

#Exemplo de uso 
conta1 = ContaBancaria("Talvan", 1000.00, 12345)
print(f"\nDepósito")
conta1.depositar(200.00)
conta1.exibirSaldo()

print(f"\nSAQUE")
conta1.sacar(1000.00)
conta1.exibirSaldo()

