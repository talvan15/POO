class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0.0
    
    def depositar(self, valor):
        if valor < 0:
            print('Valor negativo nao pode ser adicionado! ')
        else:
            self.saldo += valor
            print(f'Deposito realizado! saldo atual: {self.saldo}')
    
    def sacar(self, valor):
        if valor > self.saldo:
            print('SALSO INSUFICIENTE! ')
        else:
            self.saldo -= valor
    def exibir(self):
        print(f'Saldo da conta: {self.saldo}\n')


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, numero_conta):
        super().__init__(titular, numero_conta)
        self.limite = 1000.0

    def sacar(self, valor):
        taxa_saque = valor * 0.02
        total_saque = valor + taxa_saque

        if total_saque <= self.saldo + self.limite:
            if total_saque > self.saldo:
                self.limite -= (total_saque - self.saldo)
                self.saldo = 0
                print(f'Saque de {valor} R$, realizado com taxa de {taxa_saque} R$\nSaldo {self.saldo}\nLimite de crédito: {self.limite}')

            else:
                self.saldo -= total_saque
                print(f'Saque de {valor} R$, realizado com taxa de {taxa_saque} R$\nSaldo {self.saldo}\nLimite de crédito: {self.limite}')


class ContaPoupanca(ContaBancaria):
    
    def AplicarRendimento(self, taxa):
        rendimento = self.saldo * taxa
        self.saldo += rendimento

        print(f'Saldo com rendimento: {self.saldo}')

class ContaSalario(ContaBancaria):
    def __init__(self, titular, numero_conta):
        super().__init__(titular, numero_conta)
        self.saque_mensal = 0
        self.limite_saque = 1

    def saque(self, valor):
        if self.saque_mensal < self.limite_saque:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saque_mensal += 1
                print(f'Saque de R${valor} realizado')
            else:
                print(f'Saldo insuficiente! seu saldo: R${self.saldo}')
        else:
            print(f'Seu limite de saques já foi atingido! ')


def testeContas():

    corrente = ContaCorrente("talvan", 2121)
    poupanca = ContaPoupanca("jose", 2122)
    salario = ContaSalario("alves", 2123)

    print('\nCONTA CORRENTE:')
    corrente.depositar(500)
    corrente.sacar(600)
    corrente.exibir()

    print('\nCONTA POUPANÇA:')
    poupanca.depositar(500)
    poupanca.AplicarRendimento(0.01)
    poupanca.sacar(300)
    poupanca.exibir()

    print('\nCONTA SALÁRIO:')
    salario.depositar(1000)
    salario.saque(1000)
    salario.exibir()

testeContas()