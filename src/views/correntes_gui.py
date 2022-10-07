## BIBLIOTECAS ##
import tkinter as tk
from corrente.strouhal_gui import strouhal_gui
from corrente.reynolds_gui import reynolds_gui
from corrente.forca_estatica_gui import forca_estatica_gui
from corrente.impulso_lateral_gui import impulso_lateral_gui
from corrente.velocidade_critica_gui import velocidade_critica_gui
from corrente.coeficiente_amortecimento_gui import coeficiente_amortecimento_gui
from corrente.massa_efetiva_gui import massa_efetiva_gui
from corrente.frequencia_natural_gui import frequencia_natural_gui

def correntes_gui(win):    
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
        text = 'ESFORÇOS POR CORRENTES',
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
    btn_reynolds = tk.Button(app, text = 'REYNOLDS', command= lambda: reynolds_gui(app))
    btn_reynolds.grid(row=1, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA STROUHAL
    btn_strouhal = tk.Button(app, text = 'STROUHAL', command= lambda: strouhal_gui(app))
    btn_strouhal.grid(row=2, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA FORÇA ESTÁTICA
    btn_festatica = tk.Button(app, text = 'FORÇA ESTÁTICA', command= lambda: forca_estatica_gui(app))
    btn_festatica.grid(row=3, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO LATERAL
    btn_impulsolateral = tk.Button(app, text = 'IMPULSO LATERAL', command= lambda: impulso_lateral_gui(app))
    btn_impulsolateral.grid(row=4, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO VCRITICA
    btn_vcrit = tk.Button(app, text = 'VELOCIDADE CRITICA', command= lambda: velocidade_critica_gui(app))
    btn_vcrit.grid(row=5, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO LATERAL
    btn_ca = tk.Button(app, text = 'COEFICIENTE DE AMORTECIMENTO', command= lambda: coeficiente_amortecimento_gui(app))
    btn_ca.grid(row=6, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA IMPULSO LATERAL
    btn_mefetiva = tk.Button(app, text = 'MASSA EFETIVA', command= lambda: massa_efetiva_gui(app))
    btn_mefetiva.grid(row=7, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
    # BOTAO PARA FREQUENCIA NATURAL
    btn_fn = tk.Button(app, text = 'FREQUÊNCIA NATURAL', command= lambda: frequencia_natural_gui(app))
    btn_fn.grid(row=8, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)

    app.mainloop()