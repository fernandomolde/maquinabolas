"""

Pruebas de la clase Maquina_bola
"""

import unittest
from maquina_bolas import Maquina,MONEDA,BOLA
import maquina_bolas

class TestMaquina(unittest.TestCase):
    """ Pruebas """
    def test_creacion_maquina(self):
        """ Prueba de existencia"""
        maquina = Maquina()
        self.assertIsNotNone(maquina)
        
    def test_moneda_1E_es_valida(self):
        """ Prueba de monda de un E"""
        maquina = Maquina()
        resp = maquina.aceptar_moneda(MONEDA)
        self.assertEqual(resp, True) 

    def test_moneda_50cent_es_valida(self):
        """ Prueba de moneda de 50cts es incorrecta"""
        maquina = Maquina()
        resp = maquina.aceptar_moneda('Cent_50')
        self.assertEqual(resp, False)

    def test_giro_manivela_correcto(self):
        """Si gira correctamente True """
        maquina = Maquina()
        giro = 360
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp,True) 

    def test_giro_manivela_incorrecto(self):
        """Si gira menos de 360º es incorrecto"""
        maquina = Maquina()
        giro = 30
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp,False) 

    def test_moneda_y_giro_correctos_suelta_bola(self):
        """ Si las condiciones son correctas suelta una bola """
        maquina = Maquina()
        dep = maquina.deposito
        mon = maquina.monedero
        resp = maquina.soltar_bola()
        self.assertEqual(resp,BOLA)
        self.assertEqual(maquina.deposito, dep-1)
        self.assertEqual(maquina.monedero, mon+1)

    def test_escribir():



    def test_leer_archivo():    