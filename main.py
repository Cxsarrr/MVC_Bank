from models import CuentaBancaria
from controllers import Controlador
from views import VistaTkinter
import tkinter as tk

def main():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Sistema Bancario")

    # Crear la vista y el controlador (el nombre se pedirá en la interfaz gráfica)
    vista = VistaTkinter(root)
    controlador = Controlador(None, vista)  # Inicialmente, la cuenta es None

    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()