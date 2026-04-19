import tkinter as tk
from tkinter import messagebox
import banco

def iniciar_interface():

    def salvar():
        nome = entry_nome.get()
        email = entry_email.get()

        if nome == "" or email == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos")
            return

        banco.inserir(nome, email)

        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)

        atualizar_lista()

    def atualizar_lista():
        lista.delete(0, tk.END)
        for user in banco.listar():
            lista.insert(tk.END, f"{user[0]} - {user[1]} - {user[2]}")

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

    atualizar_lista()
    janela.mainloop()