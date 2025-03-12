from models import CuentaBancaria

class Controlador:
    def __init__(self, cuenta, vista):
        self.vista = vista
        self.cuenta = None  # Inicialmente, la cuenta es None

        # Crear la cuenta bancaria después de obtener el nombre del titular
        if self.vista.titular:
            self.cuenta = CuentaBancaria(self.vista.titular)

        # Asignar eventos a los botones
        self.vista.btn_consultar_saldo.config(command=self.consultar_saldo)
        self.vista.btn_depositar.config(command=self.depositar)
        self.vista.btn_retirar.config(command=self.retirar)

    def consultar_saldo(self):
        if self.cuenta:
            saldo = self.cuenta.consultar_saldo()
            self.vista.mostrar_saldo(saldo)
        else:
            self.vista.mostrar_error("No se ha creado una cuenta bancaria.")

    def depositar(self):
        if self.cuenta:
            cantidad = self.vista.pedir_cantidad_deposito()
            if cantidad is not None:
                self.cuenta.depositar(cantidad)
        else:
            self.vista.mostrar_error("No se ha creado una cuenta bancaria.")

    def retirar(self):
        if self.cuenta:
            cantidad = self.vista.pedir_cantidad_retiro()
            if cantidad is not None:
                self.cuenta.retirar(cantidad)
        else:
            self.vista.mostrar_error("No se ha creado una cuenta bancaria.")