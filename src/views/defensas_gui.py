## BIBLIOTECAS ##
import tkinter as tk

def defensas_gui(win):    
    app = tk.Toplevel(win)    
    app.title("FCEPORTS")
    # Não deixo ela ser redimensionada
    app.resizable(
        width=False,
        height=False
    )
    # Tamanho da Janela
    #app.geometry("800x600")
    # Não deixo ela ser redimensionada
    app.resizable(
        width=False,
        height=False
    )
    # TESTE
    options = {'padx': 5, 'pady': 5}
    ###############################################################################
    # TITULO EM CIMA DO SOFTWARE
    lbl_title = tk.Label(
        app, 
        text = 'DIMENSIONAMENTO DE DEFENSAS',
        font = ('Times New Roman', 15, 'bold')
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
    # STATUS BAR
    statusbar = tk.Label(app, text="Criado por Adilson José Pereira Junior <adilsonjpj@protonmail.com>", bd=1, relief=tk.SUNKEN)
    statusbar.grid(row=10, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    ###############################################################################
    # BOTAO PARA REYNOLDS
    btn_reynolds = tk.Button(app, text = 'REYNOLDS')
    btn_reynolds.grid(row=1, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA STROUHAL
    btn_strouhal = tk.Button(app, text = 'STROUHAL')
    btn_strouhal.grid(row=2, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA FORÇA ESTÁTICA
    btn_festatica = tk.Button(app, text = 'FORÇA ESTÁTICA')
    btn_festatica.grid(row=3, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO LATERAL
    btn_impulsolateral = tk.Button(app, text = 'IMPULSO LATERAL')
    btn_impulsolateral.grid(row=4, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO VCRITICA
    btn_vcrit = tk.Button(app, text = 'VELOCIDADE CRITICA')
    btn_vcrit.grid(row=5, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO LATERAL
    btn_ca = tk.Button(app, text = 'COEFICIENTE DE AMORTECIMENTO')
    btn_ca.grid(row=6, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO LATERAL
    btn_mefetiva = tk.Button(app, text = 'MASSA EFETIVA')
    btn_mefetiva.grid(row=7, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA FREQUENCIA NATURAL
    btn_fn = tk.Button(app, text = 'FREQUÊNCIA NATURAL')
    btn_fn.grid(row=8, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)

    app.mainloop()