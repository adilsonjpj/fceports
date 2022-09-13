from libs.gui_lib import *
from libs.structures_lib import *


############################################################################################
## REPASSANDO OS VALORES CALCULADOS PARA A INTERFACE GRÁFICA
############################################################################################

def coordenadas_canva(
    largura_canva, # Largura do canva
    altura_canva, # Altura do Canva
    periodo_onda, # Periodo da onda
    profundidade, # Profundidade da onda
    diametro, # Diametro da Estaca
    CD,
    CM,
    rho,
    altura_onda
    ):
    
    # criando a onda
    onda = OceanWave(period=periodo_onda, height=altura_onda)
    # calculando o comprimento
    onda.find_length(depth=profundidade)

    # criando a estaca
    estaca = Pile(
        diameter=diametro,
        length=profundidade,
        CD=CD,
        CM=CM)
    # passando os parametros da onda criada
    estaca.set_wave(onda)
    # 
    carregamento_inercia = estaca.calculate_max_inertia_force(rho=rho)
    carregamento_arraste = estaca.calculate_max_drag_force(rho=rho)
    ## SETANDO AS VARIAVEIS DA FORMULA
    h = round(profundidade,2) # Profundidade do local

    # VARIAVEIS PARA O DESENHO
    # PORCENTAGENS
    h_estaca = 80/100
    h_agua = 55/100
    h_solo = 5/100
    #h_H = 15/100
    l_maxima = 50/100
    #########################################################################################
    # SISTEMA DE COORDENADAS CANTO SUPERIOR ESQUERDO (0,0) CANTO INFERIOR DIREITO (MAX,MAX)
    # LIMITES DO QUADRO DE DESENHO
    x_lim_min = 0 # Canto esquerdo da tela
    x_lim_max = largura_canva # Canto direito da tela

    # DESENHO FIXO, DEVE SER MODIFICADO AQUI
    
    # DESENHO DO SOLO
    yS_solo = altura_canva - altura_canva*h_solo
    solo = Line(
        p1 = Point(x_lim_min, altura_canva), 
        p2 = Point(x_lim_max, yS_solo)
    )

    # DESENHO DA AGUA
    y_agua = yS_solo - (altura_canva*h_agua)
    agua = Line(
        p1 = Point(x_lim_min, y_agua), 
        p2 = Point(x_lim_max, y_agua)
    )
    
    # DESENHO DA ESTACA
    x_estaca = x_lim_max/2
    d_estaca = Line(
        p1 = Point(x_estaca, yS_solo), 
        p2 = Point(x_estaca, yS_solo - (altura_canva*h_estaca))
    )
    
    # Resultante
    FD = estaca.FD_res/1000
    FM = estaca.FM_res/1000
    # Momentos
    sd = estaca.sd
    sm = estaca.sm

    # COTA INERCIA
    cota_inercia = Line(
        p1 = Point(l_maxima *(x_lim_max/2), yS_solo - ((yS_solo - y_agua)*sm)),
        p2 = Point(l_maxima *(x_lim_max/2), yS_solo)
    )
    t_cota_inercia = [cota_inercia.p1.x - 5, (cota_inercia.p2.y + cota_inercia.p1.y)/2, str(round((sm * estaca.length),2))]
    # COTA ARRASTE
    cota_arraste = Line(
        p1 = Point(l_maxima *(x_lim_max/2), yS_solo- ((yS_solo - y_agua)*sd)),
        p2 = Point(l_maxima *(x_lim_max/2), yS_solo)
    )
    t_cota_arraste = [cota_arraste.p1.x - 5, (cota_arraste.p2.y + cota_arraste.p1.y)/2 , str(round((sd * estaca.length),2))]


    # DESENHO DO CARREGAMENTO
    # DESCOBRE A FORÇA MÁXIMA
    arraste_max = 0
    inercia_max = 0
    for i in carregamento_arraste:
        if (i.y > arraste_max):
            arraste_max = i.y
    for i in carregamento_inercia:
        if (i.y > inercia_max):
            inercia_max = i.y
    
    fator_l_arraste = l_maxima *(x_lim_max/2)/arraste_max
    fator_l_inercia = l_maxima *(x_lim_max/2)/inercia_max
    # MONTA O VETOR COM AS POSICOES PARA O GUI
    cargas_arraste = []
    cargas_inercia = []
    dist = yS_solo - y_agua
    fator = dist/len(carregamento_arraste)

    contador = 0
    for i in carregamento_arraste:
        cargas_arraste.append(x_estaca + i.y*fator_l_arraste) #X
        cargas_arraste.append( y_agua + contador*fator ) #Y
        contador += 1
    contador = 0
    for i in carregamento_inercia:
        cargas_inercia.append(x_estaca + i.y*fator_l_inercia) #X
        cargas_inercia.append( y_agua + contador*fator ) #Y
        contador += 1
        #cargas_inercia.append((i.x) + y_agua) #Y

    # TEXTOS
    t_agua = [x_lim_max - (8*4), y_agua -15, 'Água'] # x,y,text
    t_solo = [x_lim_max - (8*4), yS_solo -15 , 'Solo'] # x,y,text
    t_carga_topo_arraste = [x_estaca + l_maxima *(x_lim_max/2) + 50 , cargas_arraste[1] +30, str(round(carregamento_arraste[0].y/1000, 2)) + ' kN/m'] # x,y,text
    t_carga_base_arraste = [x_estaca + l_maxima *(x_lim_max/2) + 50 , cargas_arraste[-1] -30, str(round(carregamento_arraste[-1].y/1000, 2)) + ' kN/m'] # x,y,text

    t_carga_topo_inercia = [x_estaca + l_maxima *(x_lim_max/2) + 50 , cargas_inercia[1] +30, str(round(carregamento_inercia[0].y/1000, 2)) + ' kN/m'] # x,y,text
    t_carga_base_inercia = [x_estaca + l_maxima *(x_lim_max/2) + 50 , cargas_inercia[-1] -30, str(round(carregamento_inercia[-1].y/1000, 2)) + ' kN/m'] # x,y,text
    
    titulo_arraste = [x_estaca, 30, 'ARRASTE'] # x,y,text
    titulo_inercia = [x_estaca, 30, 'INERCIA']

    textos_arraste = [t_agua, t_solo, t_carga_topo_arraste, t_carga_base_arraste, titulo_arraste]
    textos_inercia = [t_agua, t_solo, t_carga_topo_inercia, t_carga_base_inercia, titulo_inercia]
    textos_cotas = [t_cota_arraste, t_cota_inercia]

    return(solo, agua, d_estaca, cargas_arraste, cargas_inercia, textos_arraste, textos_inercia, cota_arraste, cota_inercia, textos_cotas, FD, FM)

