# Fazendo a importação do TKinter e outras funções de dentro do mesmo
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage

def msg_log():
    messagebox.showinfo("Login", "Login Realizado com Sucesso!")
    window.destroy()

# Criando a Janela e definindo suas proporções
window = tk.Tk()
window.title("Tela de Login")
window.geometry("1600x850")
window.configure(bg="white")

img = PhotoImage(file="imgs/background.png")
img2 = PhotoImage(file="imgs/icon.png")
img3 = PhotoImage(file="imgs/Ellipse 1.png")

# Criando os Labels que irão conter uma imagem
lbl_back = tk.Label(window,image=img,background="white")
lbl_icon = tk.Label(lbl_back,image=img2,background="#2990B3")
lbl_elp = tk.Label(lbl_back,image=img3,background="#303A98")

# Criando as Labels que serão exibidas na tela
lbl_text1 = tk.Label(lbl_back,text="Login",background="#2990B3",foreground="white",font="Montserrat 35 bold")
lbl_text2 = tk.Label(lbl_back,text="Insira as informações para acessar o sistema:",background="#2985AF",foreground="white",font="Montserrat 20")
lbl_text3 = tk.Label(lbl_back,text="Usuário:",background="#2A77AB",foreground="white",font="Montserrat 15 bold")
txt_textBox1 = tk.Entry()
lbl_text4 = tk.Label(lbl_back,text="Senha:",background="#2D5EA3",foreground="white",font="Montserrat 15 bold")
txt_textBox2 = tk.Entry()
btn_log = tk.Button(lbl_back,text="Entrar", command=msg_log,font="Montserrat 15 bold",foreground="#331C8F")

# Salvando os Labels para que sejam exibidos quando a Janela abrir e suas posições
lbl_back.pack()
lbl_icon.place(x=1160,y=100)
lbl_elp.place(x=1080,y=615)
lbl_text1.place(x=210,y=130)
lbl_text2.place(x=210,y=220)
lbl_text3.place(x=210,y=285)
txt_textBox1.place(x=225,y=335,width=565,height=50)
lbl_text4.place(x=210,y=415)
txt_textBox2.place(x=225,y=470,width=565,height=50)
btn_log.place(x=210,y=600,width=565,height=50)

# Exibindo a Janela
window.mainloop()