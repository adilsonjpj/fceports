## BIBLIOTECAS ##
import tkinter as tk
from views.efeito_onda_parede_gui import parede_gui

def obstaculos_gui(win):    
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
        text = 'ESFORÇOS EM OBSTACULOS',
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
    # BOTAO PARA ONDAS
    btn_ondas = tk.Button(app, text = 'ONDAS', command=lambda:parede_gui(app))
    btn_ondas.grid(row=1, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA ARREBENTACAO
    btn_arrebentacao = tk.Button(app, text = 'ZONA DE ARREBENTAÇÃO', command=lambda:parede_gui(app))
    btn_arrebentacao.grid(row=2, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA CORRENTES
    btn_correntes = tk.Button(app, text = 'CORRENTES', command=lambda:parede_gui(app))
    btn_correntes.grid(row=3, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)

    app.mainloop()