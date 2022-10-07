## BIBLIOTECAS ##
import tkinter as tk
from views.atracacao_gui import atracacao_gui
from views.correntes_gui import correntes_gui
from views.defensas_gui import defensas_gui
from views.estacas_gui import estacas_gui
from views.obstaculos_gui import obstaculos_gui
from views.ondas_gui import ondas_gui




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
btn_estacas = tk.Button(app, text = 'ESTACAS', command=lambda:estacas_gui(app))
btn_estacas.grid(row=2, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA OBSTACULOS
btn_obstaculos = tk.Button(app, text = 'OBSTACULOS', command=lambda:obstaculos_gui(app))
btn_obstaculos.grid(row=3, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA CORRENTES
btn_correntes = tk.Button(app, text = 'CORRENTES', command=lambda:correntes_gui(app))
btn_correntes.grid(row=4, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA ATRACAÇÃO
btn_atracacao = tk.Button(app, text = 'ATRACAÇÃO', command=lambda:atracacao_gui(app))
btn_atracacao.grid(row=5, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
# BOTAO PARA DEFENSAS
btn_atracacao = tk.Button(app, text = 'DEFENSAS', command=lambda:defensas_gui(app))
btn_atracacao.grid(row=6, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)


app.mainloop()