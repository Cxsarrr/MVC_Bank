import tkinter as tk
from tkinter import messagebox, simpledialog

class VistaTkinter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")

        # Pedir el nombre del titular al iniciar
        self.titular = self.pedir_nombre_titular()
        if not self.titular:
            messagebox.showerror("Error", "Debes ingresar un nombre para continuar.")
            self.root.quit()  # Cerrar la aplicación si no se ingresa un nombre

        # Mostrar el nombre del titular en la interfaz
        self.titular_label = tk.Label(root, text=f"Bienvenido, {self.titular}", font=("Arial", 14))
        self.titular_label.pack(pady=10)

        # Botones del menú
        self.btn_consultar_saldo = tk.Button(root, text="Consultar saldo", command=self.mostrar_saldo)
        self.btn_consultar_saldo.pack(pady=5)

        self.btn_depositar = tk.Button(root, text="Hacer un depósito", command=self.pedir_cantidad_deposito)
        self.btn_depositar.pack(pady=5)

        self.btn_retirar = tk.Button(root, text="Hacer un retiro", command=self.pedir_cantidad_retiro)
        self.btn_retirar.pack(pady=5)

        self.btn_salir = tk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.pack(pady=5)

    def pedir_nombre_titular(self):
        # Cuadro de diálogo para pedir el nombre del titular
        nombre = simpledialog.askstring("Nombre del titular", "Ingrese el nombre del titular de la cuenta:")
        return nombre

    def mostrar_saldo(self, saldo):
        messagebox.showinfo("Saldo", f"Tu saldo actual es: {saldo}")

    def pedir_cantidad_deposito(self):
        cantidad = self.pedir_cantidad("Depósito")
        if cantidad is not None:
            return cantidad

    def pedir_cantidad_retiro(self):
        cantidad = self.pedir_cantidad("Retiro")
        if cantidad is not None:
            return cantidad

    def pedir_cantidad(self, operacion):
        cantidad = simpledialog.askfloat(operacion, "Ingresa la cantidad:")
        return cantidad

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)