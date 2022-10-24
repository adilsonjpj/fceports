## BIBLIOTECAS ##
from operator import mod
import tkinter as tk
from views.efeito_ondas.efeito_onda_estaca_max import *
from libs.gui_lib import *

def onda_estaca_max_gui(win):    
    app = tk.Toplevel(win)
    # Título da Janela
    app.title("FCEPORTS")
    # Tamanho da Janela
    app.geometry("1200x600")
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
        text = 'FORÇA EXERCIDA POR ONDAS EM ESTACAS CIRCULARES',
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
    # Profundidade 2
    lbl_profundidade = tk.Label(app, text = 'Profundidade (m)')
    lbl_profundidade.grid(row=2, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_profundidade = tk.Entry(app, width=20)
    ety_profundidade.grid(row=2, column=1, padx=10, pady=5, sticky=tk.N)

    # CD 3
    lbl_cd = tk.Label(app, text = 'CD')
    lbl_cd.grid(row=3, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_cd = tk.Entry(app, width=20)
    ety_cd.grid(row=3, column=1, padx=10, pady=5, sticky=tk.N)

    # CM 4
    lbl_cm = tk.Label(app, text = 'CM')
    lbl_cm.grid(row=4, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_cm = tk.Entry(app, width=20)
    ety_cm.grid(row=4, column=1, padx=10, pady=5, sticky=tk.N)

    # rho 5
    lbl_rho = tk.Label(app, text = '𝜌 (kg/m³)')
    lbl_rho.grid(row=5, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_rho = tk.Entry(app, width=20)
    ety_rho.grid(row=5, column=1, padx=10, pady=5, sticky=tk.N)

    # Diâmetro 6
    lbl_diametro = tk.Label(app, text = 'Diâmetro da estaca (m)')
    lbl_diametro.grid(row=6, column=0, ipadx=5, pady=5, sticky=tk.W+tk.N)
    ety_diametro = tk.Entry(app, width=20)
    ety_diametro.grid(row=6, column=1, padx=10, pady=5, sticky=tk.N)

    # PARAMETROS A SEREM INFORMADOS
    lbl_paramentros_onda = tk.Label(
        app, 
        text = 'PARÂMETROS DA ONDA',
        font = ('Times New Roman', 11, 'bold')
        )
    lbl_paramentros_onda.grid(row=7, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)
    #### ONDA
    #### COMECA NA LINHA 8
    # Periodo da onda 8
    lbl_periodo_onda = tk.Label(app, text = 'Período da Onda (s)')
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
        width=700, 
        height=500,
        highlightbackground="black", 
        highlightthickness=1
        )
    frm_drawning.grid(row=1, column=2,  rowspan=10, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)

    canva_largura = 435
    canva_altura = 500

    canva_arraste = tk.Canvas(
        frm_drawning,
        width=canva_largura, 
        height=canva_altura,
        bg = 'white'
        )
    canva_arraste.pack(side = tk.LEFT)

    canva_inercia = tk.Canvas(
        frm_drawning,
        width=canva_largura, 
        height=canva_altura,
        bg = 'white'
        )
    canva_inercia.pack(side = tk.LEFT)

    def draw_results():
        solo, agua, estaca, cargas_arraste, cargas_inercia, textos_arraste, textos_inercia, cota_arraste, cota_inercia, textos_cotas, FD, FM = coordenadas_canva(
            largura_canva = canva_largura,
            altura_canva = canva_altura,
            periodo_onda = float(ety_periodo_onda.get()),
            profundidade = float(ety_profundidade.get()),
            diametro = float(ety_diametro.get()),
            CD = float(ety_cd.get()),
            CM = float(ety_cm.get()),
            rho = float(ety_rho.get()),
            altura_onda = float(ety_altura_onda.get())
            )

        canva_arraste.delete("all")
        canva_inercia.delete("all")

        canva_arraste.create_rectangle(solo.coord(), fill='black')
        canva_inercia.create_rectangle(solo.coord(), fill='black')

        canva_arraste.create_line(agua.coord(), fill='blue')
        canva_inercia.create_line(agua.coord(), fill='blue')

        canva_arraste.create_rectangle(estaca.coord())
        canva_inercia.create_rectangle(estaca.coord())

        canva_arraste.create_line(cargas_arraste)
        canva_inercia.create_line(cargas_inercia)

        canva_arraste.create_line(cota_arraste.coord())
        canva_inercia.create_line(cota_inercia.coord())

        n_loads = len(cargas_arraste)
        # Primeira meio OK
        seta = [estaca.coord()[0]]
        seta.append(cargas_arraste[round((n_loads/2))])
        seta.append(cargas_arraste[round((n_loads/2)+1)])
        seta.append(cargas_arraste[round((n_loads/2))])
        canva_arraste.create_line(seta, arrow=tk.FIRST)
        # Segunda meio inferior OK
        seta = [estaca.coord()[0]]
        seta.append(cargas_arraste[round((n_loads/4 + n_loads/2))+1]) #y
        seta.append(cargas_arraste[round((n_loads/4 + n_loads/2))]) #x
        seta.append(cargas_arraste[round((n_loads/4 + n_loads/2))+1]) #y
        canva_arraste.create_line(seta, arrow=tk.FIRST)
        # Terceira meio superior OK
        seta = [estaca.coord()[0]]
        seta.append(cargas_arraste[round((-n_loads/4 + n_loads/2))+1]) #y
        seta.append(cargas_arraste[round((-n_loads/4 + n_loads/2))]) #x
        seta.append(cargas_arraste[round((-n_loads/4 + n_loads/2))+1]) #y
        canva_arraste.create_line(seta, arrow=tk.FIRST)

        # Primeira meio OK
        seta = [estaca.coord()[0]]
        seta.append(cargas_inercia[round((n_loads/2))])
        seta.append(cargas_inercia[round((n_loads/2)+1)])
        seta.append(cargas_inercia[round((n_loads/2))])
        canva_inercia.create_line(seta, arrow=tk.FIRST)
        # Segunda meio inferior OK
        seta = [estaca.coord()[0]]
        seta.append(cargas_inercia[round((n_loads/4 + n_loads/2))+1]) #y
        seta.append(cargas_inercia[round((n_loads/4 + n_loads/2))]) #x
        seta.append(cargas_inercia[round((n_loads/4 + n_loads/2))+1]) #y
        canva_inercia.create_line(seta, arrow=tk.FIRST)
        # Terceira meio superior OK
        seta = [estaca.coord()[0]]
        seta.append(cargas_inercia[round((-n_loads/4 + n_loads/2))+1]) #y
        seta.append(cargas_inercia[round((-n_loads/4 + n_loads/2))]) #x
        seta.append(cargas_inercia[round((-n_loads/4 + n_loads/2))+1]) #y
        canva_inercia.create_line(seta, arrow=tk.FIRST)
        # TEXTOS
        for texto in textos_arraste:
            canva_arraste.create_text(
                texto[0] , 
                texto[1] , 
                text = texto[2]
            )
        for texto in textos_inercia:
            canva_inercia.create_text(
                texto[0] , 
                texto[1] , 
                text = texto[2]
            )
        # TEXTOS COTAS
        canva_arraste.create_text(
            textos_cotas[0][0],
            textos_cotas[0][1],
            text = textos_cotas[0][2],
            angle=90
        )
        canva_inercia.create_text(
            textos_cotas[1][0],
            textos_cotas[1][1],
            text = textos_cotas[1][2],
            angle=90
        )
        # FORCAS RESULTANTES
        seta_FD = [cota_arraste.coord()[0] - 20, cota_arraste.coord()[1], estaca.coord()[0], cota_arraste.coord()[1]]
        canva_arraste.create_line(
            seta_FD, 
            arrow=tk.FIRST,
            fill='red',
            width=3
        )
        canva_arraste.create_text(
            cota_arraste.coord()[0] - 20,
            cota_arraste.coord()[1] - 20,
            text = str(round(FD, 2)) + ' kN',
            fill='red'
        )
        
        seta_FM = [cota_inercia.coord()[0] - 20, cota_inercia.coord()[1], estaca.coord()[0], cota_inercia.coord()[1]]
        canva_inercia.create_line(
            seta_FM, 
            arrow=tk.FIRST,
            fill='red',
            width = 3
        )
        canva_inercia.create_text(
            cota_inercia.coord()[0] - 20,
            cota_inercia.coord()[1] - 20,
            text = str(round(FM, 2)) + ' kN',
            fill='red'
        )
    ###############################################################################
    # BOTAO PARA CALCULAR
    btn_calculate = tk.Button(app, text = 'CALCULAR', command=draw_results)
    btn_calculate.grid(row=10, column=0, columnspan=2 , sticky=tk.W+tk.E, padx=5, pady=5)


    app.mainloop()
