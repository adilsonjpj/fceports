## BIBLIOTECAS ##
import tkinter as tk
from efeito_onda_estaca_gui import estaca_gui
from efeito_onda_parede_gui import parede_gui

app = tk.Tk()
# ICONE
icn = tk.PhotoImage(file='fceports.png')
app.iconphoto(True, icn)
# Título da Janela
app.title("FCEPORTS")
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
    text = 'FERRAMENTA PARA O CÁLCULO DE ESTRUTURAS PORTUÁRIAS - FCEPORTS',
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
# PARAMETROS A SEREM INFORMADOS
lbl_paramentros_local = tk.Label(
    app, 
    text = 'PARÂMETROS DA ESTACA E DO LOCAL',
    font = ('Times New Roman', 11, 'bold')
    )
lbl_paramentros_local.grid(row=1, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
###############################################################################
###############################################################################
# STATUS BAR
statusbar = tk.Label(app, text="Criado por Adilson José Pereira Junior <adilsonjpj@protonmail.com>", bd=1, relief=tk.SUNKEN)
statusbar.grid(row=10, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
###############################################################################
# BOTAO PARA ONDAS
btn_ondas = tk.Button(app, text = 'ONDAS')
btn_ondas.grid(row=1, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA ESTACAS
btn_estacas = tk.Button(app, text = 'ESTACAS', command=lambda:estaca_gui(app))
btn_estacas.grid(row=2, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA OBSTACULOS
btn_obstaculos = tk.Button(app, text = 'OBSTACULOS', command=lambda:parede_gui(app))
btn_obstaculos.grid(row=3, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA ATRACAÇÃO
btn_calculate = tk.Button(app, text = 'ATRACAÇÃO')
btn_calculate.grid(row=4, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)


app.mainloop()