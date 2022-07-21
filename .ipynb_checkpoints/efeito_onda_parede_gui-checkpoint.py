## BIBLIOTECAS ##
from operator import mod
import tkinter as tk
from efeito_onda_parede import *
    
app = tk.Tk()
# Título da Janela
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
lbl_comprimento_onda = tk.Label(app, text = 'Comprimento da onda (m)')
lbl_comprimento_onda.grid(row=8, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
ety_comprimento_onda = tk.Entry(app, width=20)
ety_comprimento_onda.grid(row=8, column=1, padx=10, pady=5, sticky=tk.N)

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
canva_estaca = tk.Canvas(
    frm_drawning,
    width=canva_largura, 
    height=canva_altura,
    bg = 'white'
    )
canva_estaca.pack()

def draw_results():
    canva_estaca.delete("all")
    solo, agua, parede, carregamento, plano_medio = coordenadas_canva(
        largura_canva = canva_largura,
        altura_canva = canva_altura,
        comprimento_onda = float(ety_comprimento_onda.get()),
        profundidade = float(ety_profundidade.get()),
        rho = float(ety_rho.get()),
        altura_onda = float(ety_altura_onda.get())
        )
    canva_estaca.create_rectangle(
        solo,
        fill='black'
        )
    canva_estaca.create_line(
        agua,
        fill='blue'
        )
    canva_estaca.create_line(
        plano_medio,
        fill='red',
        dash=(4, 2)
        )
    canva_estaca.create_rectangle(parede)
    canva_estaca.create_line(carregamento)
    #canva_estaca.create_text(
    #    t_agua[0] , 
    #    t_agua[1] , 
    #    text = t_agua[2]
    #) # Agua
    #canva_estaca.create_text(
    #    t_solo[0] , 
    #    t_solo[1] , 
    #    text = t_solo[2]
    #) # Solo
    #canva_estaca.create_text(
    #    t_carga_base[0] , 
    #    t_carga_base[1] , 
    #    text = t_carga_base[2]
    #) # Cmin
    #canva_estaca.create_text(
    #    t_carga_topo[0] , 
    #    t_carga_topo[1] , 
    #    text = t_carga_topo[2]
    #) # Cmax
    #n_loads = len(carga)
    # Primeira meio OK
    #seta = [estaca[0]]
    #seta.append(carga[round((n_loads/2))])
    #seta.append(carga[round((n_loads/2)+1)])
    #seta.append(carga[round((n_loads/2))])
    #canva_estaca.create_line(seta, arrow=tk.FIRST)
    # Segunda meio inferior OK
    #seta = [estaca[0]]
    #seta.append(carga[round((n_loads/4 + n_loads/2))+1]) #y
    #seta.append(carga[round((n_loads/4 + n_loads/2))]) #x
    #seta.append(carga[round((n_loads/4 + n_loads/2))+1]) #y
    #canva_estaca.create_line(seta, arrow=tk.FIRST)
    # Terceira meio superior OK
    #seta = [estaca[0]]
    #seta.append(carga[round((-n_loads/4 + n_loads/2))+1]) #y
    #seta.append(carga[round((-n_loads/4 + n_loads/2))]) #x
    #seta.append(carga[round((-n_loads/4 + n_loads/2))+1]) #y
    #canva_estaca.create_line(seta, arrow=tk.FIRST)

###############################################################################
# BOTAO PARA CALCULAR
btn_calculate = tk.Button(app, text = 'CALCULAR', command=draw_results)
btn_calculate.grid(row=10, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)


app.mainloop()