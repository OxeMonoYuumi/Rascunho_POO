from tkinter import *
from tkinter import Image, PhotoImage
from tkinter import messagebox
from tkinter import font
# Função para exibir um frame
def show_frame(frame):
    frame.tkraise()
# Funções para os botões da barra de ferramentas do frame 2
def matricula():
    print("Matrícula!")
    messagebox.showinfo("Tela Cadastro", "Clicado no botão de Matrícula")
    show_frame(frame1)

def notas():
    print("Abrir Notas do Aluno!")
    messagebox.showinfo("Tela Cadastro", "Clicado no botão Notas")
    show_frame(frame1)

def chamadas():
    print("Abrir Chamadas!")
    messagebox.showinfo("Tela Cadastro", "Clicado no botão de Chamadas")
    show_frame(frame1)

def boletim():
    print("Abrir Boletim!")
    messagebox.showinfo("Tela Cadastro", "Clicado no botão Boletim")
    show_frame(frame1)

def seleciona_opcao(valor):
    print(f"Opção selecionada: {valor}")
    
    
def trocar_senha():
    print("Abrir troca de senha!")
    messagebox.showinfo("Tela Cadastro", "Clicado no botão Troca de senha")
    show_frame(frame1)
    
def sair():
    print("Abrir sair!")
    messagebox.showinfo("Tela Cadastro", "Clicado no botão para sair")
    show_frame(frame1)


# Criando a janela principal
root = Tk()
root.title("Exemplo de Redirecionamento")
root.geometry("1600x850")

# Criando frames para diferentes "páginas"
frame1 = Frame(root)
frame2 = Frame(root)

for frame in (frame1, frame2):
    frame.place(width=1600,height=850)
    
# Conteúdo do Frame 1
# Carregando as imagens da pasta 
img = PhotoImage(file="imgs/background.png")
img2 = PhotoImage(file="imgs/icon.png")
img3 = PhotoImage(file="imgs/Ellipse 1.png")
# Criando os Labels que irão conter uma imagem
lbl_back = Label(frame1,image=img,background="white")
lbl_icon = Label(lbl_back,image=img2,background="#2990B3")
lbl_elp = Label(lbl_back,image=img3,background="#303A98")
# Criando as Labels que serão exibidas na tela
lbl_text1 = Label(lbl_back,text="Login",background="#2990B3",foreground="white",font="Montserrat 35 bold")
lbl_text2 = Label(lbl_back,text="Insira as informações para acessar o sistema:",background="#2985AF",foreground="white",font="Montserrat 20")
lbl_text3 = Label(lbl_back,text="Usuário:",background="#2A77AB",foreground="white",font="Montserrat 15 bold")
txt_textBox1 = Entry(lbl_back)
lbl_text4 = Label(lbl_back,text="Senha:",background="#2D5EA3",foreground="white",font="Montserrat 15 bold")
txt_textBox2 = Entry(lbl_back)
btn_log = Button(lbl_back,text="Entrar",font="Montserrat 15 bold",foreground="#331C8F",command=lambda: show_frame(frame2))
# Salvando e posicionado os labes dentro do Frame
lbl_back.pack()
lbl_icon.place(x=1160,y=100)
lbl_elp.place(x=1080,y=615)
lbl_text1.place(x=210,y=130)
lbl_text2.place(x=210,y=220)
lbl_text3.place(x=210,y=285)
txt_textBox1.place(x=220,y=335,width=565,height=50)
lbl_text4.place(x=210,y=415)
txt_textBox2.place(x=220,y=470,width=565,height=50)
btn_log.place(x=220,y=600,width=565,height=50)


# Conteúdo do Frame 2
# Carregando imagem da pasta
img4 = PhotoImage(file="imgs/tela_opcoes.png")
label1 = Label(frame2, image=img4, bg="#26A7B9")
label1.place(x=0, y=0)
# Botões

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
btn_matricula = Button(frame2, text="Matrícula", font=custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=10, height=1, command=matricula)
btn_matricula.place(x=230, y=17)

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
btn_notas = Button(frame2, text="Notas", font=custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=8, height=1, command=notas)
btn_notas.place(x=420, y=17)

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
btn_boletim = Button(frame2, text="Boletim", font=custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=6, height=1, command=boletim)
btn_boletim.place(x=510, y=17)

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
btn_trocar_senha = Button(frame2, text="Trocar Senha", font=custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=trocar_senha)
btn_trocar_senha.place(x=760, y=12)

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
btn_sair = Button(frame2, text="Sair", font=custom_font, bg= "white", borderwidth=0, highlightthickness=0, width=12, height=1, command=sair)
btn_sair.place(x=920, y=12)

# Criando uma variável para armazenar o valor selecionado
btn_cadastro = StringVar()
btn_cadastro.set("Cadastro")  # Valor inicial

# Lista de opções para a lista suspensa
opcoes = ["Usuários", "Cursos", "Turmas", "Disciplinas","Horários","Atividades","Dias letivos","Secretarias"]

# Criando o OptionMenu (botão com lista suspensa)
btn_cadastro = OptionMenu(frame2, btn_cadastro, *opcoes, command=seleciona_opcao)
btn_cadastro.place(x=616, y=12)

# Alterando o estilo do botão de lista suspensa
btn_cadastro.config(bg="white", fg="black", borderwidth=0, highlightthickness=0,font=("Arial", 12, "bold"))

# Alterando o estilo das opções do menu suspenso
btn_cadastro["menu"].config(bg="white", fg="black", font=("Arial", 15))

# Mostrar o primeiro frame inicialmente
show_frame(frame1)

# Iniciar o loop da interface gráfica
root.mainloop()
