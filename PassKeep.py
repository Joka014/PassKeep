import random
import string
import sqlite3
from tkinter import *

# criação do banco de dados e tabela
conn = sqlite3.connect('senhas.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Senhas
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 servico TEXT NOT NULL,
                 usuario TEXT NOT NULL,
                 senha TEXT NOT NULL);''')

# função para gerar senhas
def gerar_senha():
    tamanho = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# função para salvar senha no banco de dados
def salvar_senha(servico, usuario, senha):
    cursor.execute('''INSERT INTO Senhas(servico, usuario, senha)
                      VALUES (?, ?, ?)''', (servico, usuario, senha))
    conn.commit()

# função para fazer login
def fazer_login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if usuario == "admin" and senha == "senha123":
        login_window.destroy()
        listar_senhas()
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos")

# função para listar senhas salvas
def listar_senhas():
    listar_window = Tk()
    listar_window.title("Suas senhas salvas")

    scrollbar = Scrollbar(listar_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(listar_window, yscrollcommand=scrollbar.set)
    cursor.execute("SELECT servico, usuario, senha FROM Senhas")
    senhas = cursor.fetchall()
    for senha in senhas:
        listbox.insert(END, f"Serviço: {senha[0]}\nUsuário: {senha[1]}\nSenha: {senha[2]}\n")
    listbox.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=listbox.yview)

# função para gerar e salvar senha
def gerar_e_salvar():
    servico = servico_entry.get()
    usuario = usuario_entry2.get()
    senha = gerar_senha()
    salvar_senha(servico, usuario, senha)
    messagebox.showinfo("Senha gerada", f"A senha gerada para {servico} é: {senha}")

# janela de login
login_window = Tk()
login_window.title("Login")

usuario_label = Label(login_window, text="Usuário:")
usuario_label.grid(row=0, column=0)

usuario_entry = Entry(login_window, show="*")
usuario_entry.grid(row=0, column=1)

senha_label = Label(login_window, text="Senha:")
senha_label.grid(row=1, column=0)

senha_entry = Entry(login_window, show="*")
senha_entry.grid(row=1, column=1)

login_button = Button(login_window, text="Login", command=fazer_login)
login_button.grid(row=2, column=1)

# janela principal
root = Tk()
root.title("Gerador de senhas")

servico_label = Label(root, text="Serviço:")
servico_label.grid(row=0, column=0)

servico_entry = Entry(root)
servico_entry.grid(row=0, column=1)

usuario_label2 = Label(root, text="Usuário:")
usuario_label
