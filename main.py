import ctypes
import sys
import os
from utils import *
from biblioteca import *

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def iniciar():
    os.system('chcp 65001 > nul')

    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    while True:
        limpar_tela()
        menu1()

        try:
            op = int(input("\nEscolha: "))

            if op == 1:
                menu_pastas()
                sub = int(input("Opção: "))
                if sub == 1: limpar_temp()
                elif sub == 2: limpar_prefetch()
                elif sub == 3: limpar_logs()
                elif sub == 4:
                    limpar_temp()
                    limpar_prefetch()
                    limpar_logs()

            elif op == 2:
                menu_rede()
                sub = int(input("Opção: "))
                if sub == 1: limpar_dns()
                elif sub == 2: resetar_winsock()
                elif sub == 3:
                    limpar_dns()
                    resetar_winsock()

            elif op == 3:
                menu_personalizacao()
                sub = int(input("Opção: "))
                if sub == 1: ajustar_efeitos_visuais(True)
                elif sub == 2: ajustar_efeitos_visuais(False)
                elif sub == 3: reiniciar_explorer()

            elif op == 4:
                reparar_arquivos_sistema()

            elif op == 5:
                ativar_alto_desempenho()

            elif op == 6:
                otimizar_rede()

            elif op == 7:
                exec_all()

            elif op == 8:
                esvaziar_lixeira()

            elif op == 9:
                print("Saindo...")
                break

            elif op == 0:
                exibir_creditos()

            else:
                print("Opção inválida")

        except:
            print("Erro: digite número válido")

        input("\nPressione Enter...")

if __name__ == "__main__":
    iniciar()