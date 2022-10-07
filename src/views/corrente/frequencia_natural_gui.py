## BIBLIOTECAS ##
import tkinter as tk
from libs.currents_lib import solver_frequencia_natural
from PIL import Image, ImageTk

def frequencia_natural_gui(win):    
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
        text = 'FREQUÊNCIA NATURAL',
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
    # fk
    lbl_k = tk.Label(app, text = 'k')
    lbl_k.grid(row=2, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_k = tk.Entry(app, width=20)
    ety_k.grid(row=2, column=1, padx=10, pady=5, sticky=tk.N)

    # rho 3
    lbl_l = tk.Label(app, text = 'l')
    lbl_l.grid(row=3, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_l = tk.Entry(app, width=20)
    ety_l.grid(row=3, column=1, padx=10, pady=5, sticky=tk.N)

    # E 4
    lbl_E = tk.Label(app, text = 'E')
    lbl_E.grid(row=4, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_E = tk.Entry(app, width=20)
    ety_E.grid(row=4, column=1, padx=10, pady=5, sticky=tk.N)

    # I 5
    lbl_I = tk.Label(app, text = 'I (m^4)')
    lbl_I.grid(row=5, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_I = tk.Entry(app, width=20)
    ety_I.grid(row=5, column=1, padx=10, pady=5, sticky=tk.N)

    # m 6
    lbl_m = tk.Label(app, text = 'm')
    lbl_m.grid(row=6, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_m = tk.Entry(app, width=20)
    ety_m.grid(row=6, column=1, padx=10, pady=5, sticky=tk.N)

    # Hb 5
    #lbl_hb = tk.Label(app, text = 'Hb (m)')
    #lbl_hb.grid(row=5, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    #ety_hb = tk.Entry(app, width=20)
    #ety_hb.grid(row=5, column=1, padx=10, pady=5, sticky=tk.N)

    ###############################################################################
    ###############################################################################
    # STATUS BAR
    statusbar = tk.Label(app, text="Criado por Adilson José Pereira Junior <adilsonjpj@protonmail.com>", bd=1, relief=tk.SUNKEN)
    statusbar.grid(row=10, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
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
        text = 'fn = ',
        font = ('Times New Roman', 20, 'bold')
        )
    lbl_resultado.pack(side = tk.TOP)

    image = Image.open("img/equacao_frequencia_natural.png")
    image = image.resize((680,245), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    #img = tk.PhotoImage(file="")      
    canva_equacao.create_image(350,125, anchor=tk.CENTER, image=pic)      
 
    def draw_results():
        k = float(ety_k.get())
        l = float(ety_l.get())
        E = float(ety_E.get())
        I = float(ety_I.get())
        m = float(ety_m.get())
        fn = solver_frequencia_natural(k=k, l=l, E=E, I=I, m=m)
        lbl_resultado.configure(text='fn = ' + str(round(fn, 2)))

    ###############################################################################
    # BOTAO PARA CALCULAR
    btn_calculate = tk.Button(app, text = 'CALCULAR', command=draw_results)
    btn_calculate.grid(row=9, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    app.mainloop()