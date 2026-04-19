import sqlite3

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

def criar_usuario(nome, email):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()


def listar_usuarios():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios

def atualizar_usuario(id, nome, email):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (nome, email, id)
    )

    conn.commit()
    conn.close()

def deletar_usuario(id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))

    conn.commit()
    conn.close()

criar_usuario("Eric", "eric@email.com")
criar_usuario("Maria", "maria@email.com")

print(listar_usuarios())

atualizar_usuario(1, "Eric Atualizado", "novo@email.com")

deletar_usuario(2)

print(listar_usuarios())

