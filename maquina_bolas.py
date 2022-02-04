"""
Maquina expendedora
"""


MONEDA = 'Euro_1'
BOLA = 'Bola entregada'
CAPACIDAD = 100 #Nº de bolas que caben en la máquina

class Maquina():
    """ 
    Clase que representa la máquina 
    """
    def __init__(self) -> None:
        self.deposito = CAPACIDAD
        self.monedero = 0

    def aceptar_moneda(self, moneda_insertada):
        """ 
        Método para aceptar una moneda y
        devuelve T/F dependiendo si es correcta.
        """
        return moneda_insertada == MONEDA

    def girar_manivela(self,giro):
        """
        Simula el giro de la manivela de la máquina,
        Solo funciona con giros de 360º. 
        """
        return giro == 360

    def soltar_bola(self):
        """
        Si se ha insertado una moneda válida y se ha girado la manivela,
        se suelta una bola.
        Se decrementa el número de bolas.
        Se incrementa el número de bolas
        """
        self.deposito -=1
        self.monedero +=1
        return BOLA