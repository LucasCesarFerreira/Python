import modelo
import os


resp = 0
while resp != 5:
    print("----------------------------------Menu-----------------------------------")
    print("1-Registrar filme\n2-Registrar série\n3-Dar like\n4-Mostrar lista\n5-sair")
    resp = int(input())
    if resp == 1:
        modelo.registra_programa(1)
    elif resp == 2:
        modelo.registra_programa(2)
    elif resp == 3:
        modelo.like()
    elif resp == 4:
        modelo.mostra_programa()
    os.system('cls')
