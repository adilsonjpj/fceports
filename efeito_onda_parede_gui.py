## BIBLIOTECAS ##
from operator import mod
import tkinter as tk
from efeito_onda_parede import *
    
app = tk.Tk()


app.title("FCEPORTS")
# Tamanho da Janela
app.geometry("800x600")

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
    text = 'FORÇA EXERCIDA POR ONDAS EM PAREDES',
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
    text = 'PARÂMETROS DO LOCAL',
    font = ('Times New Roman', 11, 'bold')
    )
lbl_paramentros_local.grid(row=1, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
#### LOCAL E ESTACA
#### COMECA NA LINHA 2
# Profundidade 2
lbl_profundidade = tk.Label(app, text = 'Profundidade (m)')
lbl_profundidade.grid(row=2, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ety_profundidade = tk.Entry(app, width=20)
ety_profundidade.grid(row=2, column=1, padx=10, pady=5, sticky=tk.N)

# rho 5
lbl_rho = tk.Label(app, text = '𝜌 (kg/m³)')
lbl_rho.grid(row=5, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ety_rho = tk.Entry(app, width=20)
ety_rho.grid(row=5, column=1, padx=10, pady=5, sticky=tk.N)

# PARAMETROS A SEREM INFORMADOS
lbl_paramentros_onda = tk.Label(
    app, 
    text = 'PARÂMETROS DA ONDA',
    font = ('Times New Roman', 11, 'bold')
    )
lbl_paramentros_onda.grid(row=7, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
#### ONDA
#### COMECA NA LINHA 8
# Comprimento da linha 8
lbl_periodo_onda = tk.Label(app, text = 'Periodo da onda (s)')
lbl_periodo_onda.grid(row=8, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ety_periodo_onda = tk.Entry(app, width=20)
ety_periodo_onda.grid(row=8, column=1, padx=10, pady=5, sticky=tk.N)

# Altura da onda 9
lbl_altura_onda = tk.Label(app, text = 'Altura da Onda (m)')
lbl_altura_onda.grid(row=9, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ety_altura_onda = tk.Entry(app, width=20)
ety_altura_onda.grid(row=9, column=1, padx=10, pady=5, sticky=tk.N)


###############################################################################
###############################################################################
# STATUS BAR
statusbar = tk.Label(app, text="Criado por Adilson José Pereira Junior <adilsonjpj@protonmail.com>", bd=1, relief=tk.SUNKEN)
statusbar.grid(row=11, column=0, columnspan=3 , sticky=tk.W+tk.E, padx=5, pady=5)
###############################################################################
# DESENHO DA ESTACA
frm_drawning = tk.Frame(
    app,
    width=450, 
    height=500,
    highlightbackground="black", 
    highlightthickness=1
    )
frm_drawning.grid(row=1, column=2,  rowspan=10, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)

canva_largura = 450
canva_altura = 500
canva_parede = tk.Canvas(
    frm_drawning,
    width=canva_largura, 
    height=canva_altura,
    bg = 'white'
    )
canva_parede.pack()

def draw_results():
    canva_parede.delete("all")
    solo, agua, parede, carregamento, plano_medio, textos, cotas, textos_cotas, linha_58 = coordenadas_canva(
        largura_canva = canva_largura,
        altura_canva = canva_altura,
        periodo_onda = float(ety_periodo_onda.get()),
        profundidade = float(ety_profundidade.get()),
        rho = float(ety_rho.get()),
        altura_onda = float(ety_altura_onda.get())
        )
    canva_parede.create_rectangle(
        solo.coord(),
        fill='black'
        )
    canva_parede.create_line(
        agua.coord(),
        fill='blue'
        )
    canva_parede.create_line(
        plano_medio.coord(),
        fill='red',
        dash=(4, 2)
        )
    canva_parede.create_line(
        linha_58.coord(),
        fill='black',
        dash=(4, 2)
        )
    canva_parede.create_rectangle(parede.coord())
    canva_parede.create_line(carregamento)
    
    # TEXTOS
    for texto in textos:
        canva_parede.create_text(
            texto[0] , 
            texto[1] , 
            text = texto[2]
        )
    # COTAS
    for cota in cotas:
        canva_parede.create_line(cota.coord(), fill='orange')
    
    # TEXTOS COTAS
    for texto_cota in textos_cotas:
        canva_parede.create_text(
            texto_cota[0] , 
            texto_cota[1] , 
            text = texto_cota[2],
            angle = 90
        )
    #########

###############################################################################
# BOTAO PARA CALCULAR
btn_calculate = tk.Button(app, text = 'CALCULAR', command=draw_results)
btn_calculate.grid(row=10, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)


app.mainloop()