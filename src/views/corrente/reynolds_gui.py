## BIBLIOTECAS ##
import tkinter as tk
from libs.currents_lib import solver_reynolds
from PIL import Image, ImageTk

def reynolds_gui(win):    
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
        text = 'NÚMERO DE REYNOLDS',
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
    # nu
    lbl_nu = tk.Label(app, text = 'ν (m²/s)')
    lbl_nu.grid(row=2, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_nu = tk.Entry(app, width=20)
    ety_nu.grid(row=2, column=1, padx=10, pady=5, sticky=tk.N)

    # rho 3
    lbl_Uo = tk.Label(app, text = 'Uo (m/s)')
    lbl_Uo.grid(row=3, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_Uo = tk.Entry(app, width=20)
    ety_Uo.grid(row=3, column=1, padx=10, pady=5, sticky=tk.N)

    # D 4
    lbl_D = tk.Label(app, text = 'D (m)')
    lbl_D.grid(row=4, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_D = tk.Entry(app, width=20)
    ety_D.grid(row=4, column=1, padx=10, pady=5, sticky=tk.N)

    # Hb 5
    #lbl_hb = tk.Label(app, text = 'Hb (m)')
    #lbl_hb.grid(row=5, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    #ety_hb = tk.Entry(app, width=20)
    #ety_hb.grid(row=5, column=1, padx=10, pady=5, sticky=tk.N)

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

    lbl_resultado = tk.Label(
        frm_drawning, 
        text = 'Re = ',
        font = ('Times New Roman', 20, 'bold')
        )
    lbl_resultado.pack(side = tk.TOP)

    image = Image.open("img/equacao_reynolds.png")
    image = image.resize((520,240), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    #img = tk.PhotoImage(file="")      
    canva_equacao.create_image(350,125, anchor=tk.CENTER, image=pic)      
 
    def draw_results():
        nu = float(ety_nu.get())
        D = float(ety_D.get())
        Uo = float(ety_Uo.get())
        Re = solver_reynolds(Uo=Uo, D=D, viscosidade_cinematica=nu)
        lbl_resultado.configure(text='Re = ' + str(round(Re, 2)))

    ###############################################################################
    # BOTAO PARA CALCULAR
    btn_calculate = tk.Button(app, text = 'CALCULAR', command=draw_results)
    btn_calculate.grid(row=6, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    app.mainloop()