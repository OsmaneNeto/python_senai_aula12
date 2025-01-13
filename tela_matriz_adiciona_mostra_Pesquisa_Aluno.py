import tkinter as tk
from tkinter import messagebox

# pyinstaller atividade1307.py
# pip install pyinstaller

#Método de adicionar

def adicionar_aluno():
    nome = entry_aluno.get().title()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    media = (num1+num2)/2
    if media >=7:
        situacao="Aprovado"
    else:
        situacao ="Reprovado"
    nota = nome, num1, num2, media, situacao
    alunos.append(nota)
    entry_aluno.delete(0, tk.END)
    messagebox.showinfo("INFORMAÇÃO: ","ADICIONADO COM SUCESSO")

#Método de exibir

def exibir_alunos():

    resultado_text.delete(1.0, tk.END)
    for aluno in alunos:
        resultado_text.insert(tk.END, "|||||||||||||||||||||||||||| \n")
        resultado_text.insert(tk.END, f"Nome: {aluno[0]}\n")
        resultado_text.insert(tk.END, f"Nota1°: {aluno[1]}\n")
        resultado_text.insert(tk.END, f"Nota2°: {aluno[2]}\n")
        resultado_text.insert(tk.END, f"Média: {aluno[3]}\n")
        resultado_text.insert(tk.END, f"Situação: {aluno[4]}\n")
        messagebox.showinfo("INFORMAÇÃO: ","Foi exibido todos os alunos cadastrados")

#Método de busca        pyinstalle

def busca():
    pesquisa = entry_pesquisa.get()
    for aluno in alunos:
        if aluno[0].lower() == pesquisa.lower():
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, f"Nome: {aluno[0]}\n")
            resultado_text.insert(tk.END, f"Nota1°: {aluno[1]}\n")
            resultado_text.insert(tk.END, f"Nota2°: {aluno[2]}\n")
            resultado_text.insert(tk.END, f"Média: {aluno[3]}\n")
            resultado_text.insert(tk.END, f"Situação: {aluno[4]}\n")
            messagebox.showwarning("Atenção:","Você pesquisou por um aluno ")


alunos = []

#Tela

window = tk.Tk()
window.title("Cadastro de Alunos")
window.geometry("300x300")


label_aluno = tk.Label(window, text="Nome do Aluno:")
label_aluno.pack()


entry_aluno = tk.Entry(window)
entry_aluno.pack()

label_num1 = tk.Label(window, text="Entre com a Primeira nota:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Entre com a Segunda nota:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

button_adicionar = tk.Button(window, text="Adicionar", command=adicionar_aluno)
button_adicionar.pack()


button_exibir = tk.Button(window, text="Exibir Alunos", command=exibir_alunos)
button_exibir.pack()

entry_pesquisa = tk.Label(window, text="Pesquisar nome")
entry_pesquisa.pack(pady="1")

button_pesquisa = tk.Button(window, text="Pesquisar", command=busca)
button_pesquisa.pack()

entry_pesquisa= tk.Entry(window)
entry_pesquisa.pack(pady="3")


resultado_text = tk.Text(window, height=30, width=50)
resultado_text.pack()


window.mainloop()