import tkinter as tk
from tkinter import ttk, messagebox
from clase_producto import Producto

class ProductoUI:
    def __init__(self):
        self.producto = Producto()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Productos")

        # Campos
        tk.Label(self.ventana, text="Nombre", font=("Arial", 14)).grid(row=0, column=0)
        self.nombre = tk.Entry(self.ventana)
        self.nombre.grid(row=0, column=1)

        tk.Label(self.ventana, text="Precio",font=("Arial", 14)).grid(row=1, column=0)
        self.precio = tk.Entry(self.ventana)
        self.precio.grid(row=1, column=1)

        tk.Label(self.ventana, text="Stock",font=("Arial", 14)).grid(row=2, column=0)
        self.stock = tk.Entry(self.ventana)
        self.stock.grid(row=2, column=1)

        tk.Label(self.ventana, text="Categoría",font=("Arial", 14)).grid(row=3, column=0)
        self.categoria = tk.Entry(self.ventana)
        self.categoria.grid(row=3, column=1)

        # Botones
        tk.Button(self.ventana, text="Agregar", command=self.agregar,  font=("Arial", 12)).grid(row=4, column=0)
        tk.Button(self.ventana, text="Actualizar", command=self.actualizar,  font=("Arial", 12)).grid(row=4, column=1)
        tk.Button(self.ventana, text="Eliminar", command=self.eliminar, font=("Arial", 12)).grid(row=4, column=2)
        
        # Tabla
        self.tabla = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Precio", "Stock", "Categoría"), show='headings')
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
        self.tabla.grid(row=5, column=0, columnspan=4)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_producto)

        self.producto_seleccionado = None
        self.mostrar_productos()
        self.ventana.mainloop()

    def mostrar_productos(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for fila in self.producto.listar():
            self.tabla.insert("", "end", values=fila)

    def seleccionar_producto(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            datos = self.tabla.item(seleccion)['values']
            self.producto_seleccionado = datos[0]
            self.nombre.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.stock.delete(0, tk.END)
            self.categoria.delete(0, tk.END)
            self.nombre.insert(0, datos[1])
            self.precio.insert(0, datos[2])
            self.stock.insert(0, datos[3])
            self.categoria.insert(0, datos[4])

    def agregar(self):
        self.producto.agregar(
            self.nombre.get(),
            int(self.precio.get()),
            int(self.stock.get()),
            self.categoria.get()
        )
        self.mostrar_productos()
        messagebox.showinfo("Éxito", "Producto agregado correctamente")

    def actualizar(self):
        if self.producto_seleccionado:
            self.producto.actualizar(
                self.producto_seleccionado,
                self.nombre.get(),
                int(self.precio.get()),
                int(self.stock.get()),
                self.categoria.get()
            )
            self.mostrar_productos()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente")

    def eliminar(self):
        if self.producto_seleccionado:
            self.producto.eliminar(self.producto_seleccionado)
            self.mostrar_productos()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
