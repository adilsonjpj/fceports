## BIBLIOTECAS ##
import tkinter as tk
from libs.currents_lib import solver_massa_efetiva
from views.corrente.massa_efetiva.caso1_gui import caso1_gui
from views.corrente.massa_efetiva.caso2_gui import caso2_gui
from views.corrente.massa_efetiva.caso3_gui import caso3_gui
from PIL import Image, ImageTk

def massa_efetiva_gui(win):    
    app = tk.Toplevel(win)    

    app.title("FCEPORTS")
    # Tamanho da Janela
    #app.geometry("800x600")

    # Não deixo ela ser redimensionada

    app.resizable(
        width=False,
        height=False
    )

    # CONFIGURANDO O GRID
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=3)

    # TESTE
    options = {'padx': 5, 'pady': 5}

    # DEFINICOES
    # NUMERO DE COLUNAS 3
    # NUMERO DE LINHAS 10
    ###############################################################################
    # TITULO EM CIMA DO SOFTWARE
    lbl_title = tk.Label(
        app, 
        text = 'MASSA EFETIVA',
        font = ('Times New Roman', 17, 'bold')
        )
    lbl_title.grid(
        row=0, 
        column=0,
        columnspan=3, 
        ipadx=5, 
        pady=5, 
        sticky=tk.W+tk.E)
    ###############################################################################
    ###############################################################################
    # PARAMETROS A SEREM INFORMADOS
    lbl_paramentros_local = tk.Label(
        app, 
        text = 'PARÂMETROS',
        font = ('Times New Roman', 11, 'bold')
        )
    lbl_paramentros_local.grid(row=1, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    #### LOCAL E ESTACA
    #### COMECA NA LINHA 2
    
    # BOTAO PARA ENGASTADA-ENGASTADA
    btn_caso1 = tk.Button(app, text = 'CASO I', command= lambda: caso1_gui(app))
    btn_caso1.grid(row=1, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA ENGASTADA-APOIADA
    btn_caso2 = tk.Button(app, text = 'CASO II', command= lambda: caso2_gui(app))
    btn_caso2.grid(row=2, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA ENGASTADA-LIVRE
    btn_caso3 = tk.Button(app, text = 'CASO III', command= lambda: caso3_gui(app))
    btn_caso3.grid(row=3, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    
        ###############################################################################
    ###############################################################################
    # STATUS BAR
    statusbar = tk.Label(app, text="Criado por Adilson José Pereira Junior <adilsonjpj@protonmail.com>", bd=1, relief=tk.SUNKEN)
    statusbar.grid(row=7, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    ###############################################################################
    # DESENHO DA ESTACA
    frm_drawning = tk.Frame(
        app,
        width=700, 
        height=500,
        highlightbackground="black", 
        highlightthickness=1
        )
    frm_drawning.grid(row=1, column=2,  rowspan=6, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)

    canva_largura = 700
    canva_altura = 250

    #lbl_norma = tk.Label(
    #    frm_drawning, 
    #    text = 'ASCE 07-2010',
    #    font = ('Times New Roman', 17, 'bold')
    #    )
    #lbl_norma.pack(side = tk.TOP)

    canva_equacao = tk.Canvas(
        frm_drawning,
        width=canva_largura, 
        height=canva_altura,
        bg = 'white'
        )
    canva_equacao.pack(side = tk.TOP)

    image = Image.open("img/casos-frequencia-natural.jpg")
    image = image.resize((510,265), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    #img = tk.PhotoImage(file="")      
    canva_equacao.create_image(350,125, anchor=tk.CENTER, image=pic)      
 

    app.mainloop()