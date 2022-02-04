import maquina_bolas
from maquina_bolas import BOLA

maquina = maquina_bolas.Maquina()
SEGUIR = True

while SEGUIR:
    moneda = input('Introduce una moneda válida (Euro_1)')
    if maquina.aceptar_moneda(moneda):
        try:
            giro = int(input('Girar la manivela unos grados (360 = OK)'))
        except ValueError:
            print('Sólo se admiten números enteros.')
            giro = 0 
            
        if maquina.girar_manivela(giro):
            print(maquina.soltar_bola())
            print(f'Quedan {maquina.deposito} bolas')
            print(f'Hay {maquina.monedero} Euros')
        else:
            print('Debes girar 360º si quieres una bola. Operacion cancelada.')
            continue
    else:
        print('Debes introductir 1€  si quieres una bola. Operacion cancelada')
        continue
    resp = input('¿Quieres más bolas s/n?').upper()
    if resp == 'N':
        SEGUIR = False