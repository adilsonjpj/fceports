from typing import List
import sympy as sym
from waves_lib import OceanWave
from gui_lib import Point, Line
from ..efeito_onda_estaca import solver_forca_arraste_max_gui



class Pile:
    wave: OceanWave
    diameter: float # Diameter
    length: float # Length
    CD: float # Coef. de arraste
    CM: float # Coef. de inercia

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


    def calculate_max_drag_force(self, rho: float, precision: int = 2) -> List[Point]:
        loads: List[Point]
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
                k = self.wave.sigma,
                z = float(-i/factor),
                h = self.length
            )
            loads.append( Point(x = i/factor, y = carga_ponto) )
            #x = (carga_ponto/escala_x) + xS_estaca
            #y = ((i/factor) * escala_y) + y_agua
        return(loads)