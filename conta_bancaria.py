import datetime

class Conta:

    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        # self.movimentacoes = list()

    def deposito_valido(self, novo_valor):
        if novo_valor > 0:
            self.saldo += novo_valor
            # self.add_movimentacao("Depósito", novo_valor)
            return True
        return False

    def saque_valido(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            # self.add_movimentacao("Saque", valor)
            return True
        return False

    """def add_movimentacao(self, acao, valor):
      data = datetime.datetime.now()
      data = data.strftime("%x")
      movimentacao = f"{acao} no valor de R$ {valor} na data {data}"
      self.movimentacoes.append(movimentacao)"""

    def extrato(self):
        print("---------- Extrato ----------")
        print(f"Conta: {self.numero_conta}\nTitular:{self.titular}")
        for movimentacao in self.movimentacoes:
            print(movimentacao)
        print(f"-------------------- Saldo: {self.saldo}")