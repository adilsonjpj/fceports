from typing import List
#from waves_lib import OceanWave
from libs.waves_lib import OceanWave
from libs.gui_lib import Point
from libs.wave_pile_effect import *
from libs.wave_wall_effect import *
import mpmath as mp



class Pile:
    wave: OceanWave
    diameter: float # Diameter
    length: float # Length
    CD: float # Coef. de arraste
    CM: float # Coef. de inercia
    kd: float
    km: float
    sd: float
    sm: float
    FD_res: float
    FM_res: float
    MD_res: float
    MM_res: float

    # Constructor
    def __init__(self, diameter: float, length: float, CD: float, CM: float) -> None:
        self.diameter = diameter
        self.length = length
        self.CD = CD
        self.CM = CM
    
    # Recebe uma onda
    def set_wave(self, wave: OceanWave) -> None:
        self.wave = wave
    
    # Create wave
    def create_wave(self, period: float, height: float) -> None:
        self.wave = OceanWave(period=period, height=height)
        self.wave.find_length(depth=self.length)


    def calculate_max_drag_force(self, rho: float, precision: int = 1) -> List[Point]:
        eta = solver_eta(k=self.wave.k, h=self.length)
        kd = solver_forca_arraste_kd_max(eta = eta)
        sd = solver_momento_arraste_sd(eta = eta, k = self.wave.k, h= self.length)
        FD = solver_forca_arraste_res(CD = self.CD, rho = rho, g = 9.81, D = self.diameter, H = self.wave.height, kd = kd)
        MD = solver_momento_arraste_res(FD = FD, h = self.length, sd = sd)
        print('eta = ' + str(eta))
        print('kd = ' + str(kd))
        print('sd = ' + str(sd))
        print('FD = ' + str(FD))
        print('MD = ' + str(MD))
        
        self.kd = kd
        self.sd = sd
        self.FD_res = FD
        self.MD_res = MD

        loads: List[Point] = []
        factor = pow(10,precision)
        h = round(self.length, precision)
        for i in range(int(h*factor) + 1):
            carga_ponto = solver_forca_arraste_max_gui(
                CD = self.CD,
                rho = rho,
                g = 9.81,
                D = self.diameter,
                H = self.wave.height,
                T = self.wave.period,
                L = self.wave.length,
                k = self.wave.k,
                z = float(-i/factor),
                h = self.length
            )
            loads.append( Point(x = i/factor, y = carga_ponto) )
        return(loads)

    def calculate_max_inertia_force(self, rho: float, precision: int = 1) -> List[Point]:
        sm = solver_momento_inercia_sm(k = self.wave.k, h = self.length)
        km = solver_forca_inercia_km_max(k=self.wave.k, h=self.length)
        FM = solver_forca_inercia_res(CM = self.CM, rho = rho, g = 9.81, D = self.diameter, H = self.wave.height, km = km)
        MM = solver_momento_inercia_res(FM = FM, h = self.length, sm = sm)
        
        self.sm = sm
        self.km = km
        self.FM_res = FM
        self.MM_res = MM

        loads: List[Point] = []
        factor = pow(10,precision)
        h = round(self.length, precision)
        for i in range(int(h*factor) + 1):
            carga_ponto = solver_forca_inercia_max_gui(
                CM = self.CM,
                rho = rho,
                g = 9.81,
                D = self.diameter,
                H = self.wave.height,
                L = self.wave.length,
                k = self.wave.k,
                z = float(-i/factor),
                h = self.length
            )
            loads.append( Point(x = i/factor, y = carga_ponto) )
        return(loads)


class Wall:
    wave: OceanWave
    length: float # Length
    
    # Loads
    deltah: float
    deltap: float
    p1: float
    p2: float
    
    # Constructor
    def __init__(self, length: float) -> None:
        self.length = length
    
    # Recebe uma onda
    def set_wave(self, wave: OceanWave) -> None:
        self.wave = wave
    
    # Create wave
    def create_wave(self, period: float, height: float) -> None:
        self.wave = OceanWave(period=period, height=height)
        self.wave.find_length(depth=self.length)
    # Calcula o deltah (plano medio da onda)
    def calculate_deltah(self) -> None:
        deltah = ((mp.pi*self.wave.height**2)/self.wave.length) * mp.coth((2*mp.pi*self.length)/self.wave.length)
        self.deltah = deltah
    # Calcula a variacao de pressao deltap em Pascal (Pa)
    def calculate_deltap(self, rho: float, g: float = 9.81) -> None:
        deltap = (rho*g*self.wave.height) / mp.cosh((2*mp.pi*self.length)/self.wave.length)
        self.deltap = deltap
    # Calcula a pressao no ponto 1
    def calculate_p1(self, rho: float, g: float = 9.81) -> None:
        p1 = (self.deltap + rho*g*self.length) * ((self.wave.height + self.deltah)/(self.wave.height + self.length + self.deltah))
        self.p1 = p1
    # Calcula a pressao no ponto 2
    def calculate_p2(self, rho: float, g: float = 9.81) -> None:
        p2 = rho*g*( self.wave.height - self.deltah )
        self.p2 = p2
