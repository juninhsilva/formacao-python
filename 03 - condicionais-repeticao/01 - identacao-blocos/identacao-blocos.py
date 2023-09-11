class conta():

    saldo = 3000.00

    def sacar(self, valor):
        if self.saldo >=valor:
            self.saldo -= valor
            print('Valor sacado: {valor}')
            print('Saldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo+=valor

c1 = conta()

c1.sacar(352.35)

print(c1.saldo)

c1.depositar(240)

print(c1.saldo)