import tkinter as tk
from tkinter import ttk, messagebox
from clase_cliente import Cliente

class ClienteUI:
    def __init__(self):
        self.cliente = Cliente()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Clientes")

        # Entradas
        tk.Label(self.ventana, text="Nombre", font=("Arial", 14)).grid(row=0, column=0)
        self.nombre = tk.Entry(self.ventana)
        self.nombre.grid(row=0, column=1)

        tk.Label(self.ventana, text="Apellidos", font=("Arial", 14)).grid(row=1, column=0)
        self.apellidos = tk.Entry(self.ventana)
        self.apellidos.grid(row=1, column=1)

        tk.Label(self.ventana, text="Email", font=("Arial", 14)).grid(row=2, column=0)
        self.email = tk.Entry(self.ventana)
        self.email.grid(row=2, column=1)

        # Botones
        tk.Button(self.ventana, text="Agregar", command=self.agregar, font=("Arial", 12)).grid(row=3, column=0)
        tk.Button(self.ventana, text="Actualizar", command=self.actualizar, font=("Arial", 12)).grid(row=3, column=1)
        tk.Button(self.ventana, text="Eliminar", command=self.eliminar, font=("Arial", 12)).grid(row=3, column=2)
    
        # Tabla
        self.tabla = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Apellidos", "Email"), show='headings')
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
        self.tabla.grid(row=4, column=0, columnspan=4)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_cliente)

        self.cliente_seleccionado = None
        self.mostrar_clientes()
        self.ventana.mainloop()

    def mostrar_clientes(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for fila in self.cliente.listar():
            self.tabla.insert("", "end", values=fila)

    def seleccionar_cliente(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            datos = self.tabla.item(seleccion)['values']
            self.cliente_seleccionado = datos[0]
            self.nombre.delete(0, tk.END)
            self.apellidos.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.nombre.insert(0, datos[1])
            self.apellidos.insert(0, datos[2])
            self.email.insert(0, datos[3])

    def agregar(self):
        self.cliente.agregar(
            self.nombre.get(),
            self.apellidos.get(),
            self.email.get()
        )
        self.mostrar_clientes()
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")

    def actualizar(self):
        if self.cliente_seleccionado:
            self.cliente.actualizar(
                self.cliente_seleccionado,
                self.nombre.get(),
                self.apellidos.get(),
                self.email.get()
            )
            self.mostrar_clientes()
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente")

    def eliminar(self):
        if self.cliente_seleccionado:
            self.cliente.eliminar(self.cliente_seleccionado)
            self.mostrar_clientes()
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
