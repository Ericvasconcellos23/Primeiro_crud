import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conectar ao banco
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")
conn.commit()

# Função para salvar
def salvar():
    nome = entry_nome.get()
    email = entry_email.get()

    if nome == "" or email == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos")
        return

    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()

    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    listar()

# Função para listar
def listar():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM usuarios")
    for user in cursor.fetchall():
        lista.insert(tk.END, f"{user[0]} - {user[1]} - {user[2]}")

# Interface
janela = tk.Tk()
janela.title("CRUD de Usuários")

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Button(janela, text="Salvar", command=salvar).pack()

lista = tk.Listbox(janela, width=50)
lista.pack()

listar()

janela.mainloop()