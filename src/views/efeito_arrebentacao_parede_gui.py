## BIBLIOTECAS ##
from operator import mod
import tkinter as tk
from .efeito_onda_parede import *
from PIL import Image, ImageTk

def arrebentacao_parede_gui(win):    
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
        text = 'FORÇA EXERCIDA POR ONDAS NA ARREBENTAÇÃO EM OBSTACULOS',
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
        text = 'PARÂMETROS DA ESTACA E DO LOCAL',
        font = ('Times New Roman', 11, 'bold')
        )
    lbl_paramentros_local.grid(row=1, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    #### LOCAL E ESTACA
    #### COMECA NA LINHA 2
    # Coeficiente de arrasto Cp
    lbl_cp = tk.Label(app, text = 'Cp')
    lbl_cp.grid(row=2, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_cp = tk.Entry(app, width=20)
    ety_cp.grid(row=2, column=1, padx=10, pady=5, sticky=tk.N)

    # rho 3
    lbl_rho = tk.Label(app, text = '𝜌 (kg/m³)')
    lbl_rho.grid(row=3, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_rho = tk.Entry(app, width=20)
    ety_rho.grid(row=3, column=1, padx=10, pady=5, sticky=tk.N)

    # D 4
    lbl_ds = tk.Label(app, text = 'ds (m)')
    lbl_ds.grid(row=4, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_ds = tk.Entry(app, width=20)
    ety_ds.grid(row=4, column=1, padx=10, pady=5, sticky=tk.N)

    # Hb 5
    lbl_hb = tk.Label(app, text = 'Hb (m)')
    lbl_hb.grid(row=5, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_hb = tk.Entry(app, width=20)
    ety_hb.grid(row=5, column=1, padx=10, pady=5, sticky=tk.N)

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

    lbl_norma = tk.Label(
        frm_drawning, 
        text = 'ASCE 07-2010',
        font = ('Times New Roman', 17, 'bold')
        )
    lbl_norma.pack(side = tk.TOP)

    canva_equacao = tk.Canvas(
        frm_drawning,
        width=canva_largura, 
        height=canva_altura,
        bg = 'white'
        )
    canva_equacao.pack(side = tk.TOP)

    lbl_resultado = tk.Label(
        frm_drawning, 
        text = 'Ft = ',
        font = ('Times New Roman', 20, 'bold')
        )
    lbl_resultado.pack(side = tk.TOP)

    image = Image.open("img/equacao_arrebentacao_obstaculo.png")
    image = image.resize((680,63), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    #img = tk.PhotoImage(file="")      
    canva_equacao.create_image(350,125, anchor=tk.CENTER, image=pic)      
 
    def draw_results():
        cp = float(ety_cp.get())
        rho = float(ety_rho.get())
        ds = float(ety_ds.get())
        #hb = float(ety_hb.get())
        Ft = rho * 9.81 * (ds**2) * (cp*1.1 + 2.4)
        lbl_resultado.configure(text='Ft = ' + str(round(Ft/1000, 2)) + ' kN/m')

    ###############################################################################
    # BOTAO PARA CALCULAR
    btn_calculate = tk.Button(app, text = 'CALCULAR', command=draw_results)
    btn_calculate.grid(row=6, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    app.mainloop()