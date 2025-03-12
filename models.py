class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f'Deposito de {cantidad} realizado con éxito.')
        else:
            print('Cantidad inválida para depósito.')
            
    def retirar(self, cantidad):
        if cantidad <= 0:
            print('Cantidad inválida para retiro.')
        elif cantidad > self.saldo:
            print('No hay suficiente saldo para realizar el retiro.')
        else:
            self.saldo -= cantidad
            print(f'Retiro de {cantidad} realizado con éxito.')
            
    def consultar_saldo(self):
        return self.saldo