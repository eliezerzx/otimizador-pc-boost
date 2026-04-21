import time
import os

# CORES
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'
NEGRITO = '\033[1m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading(msg="Processando", tempo=2):
    print(f"\n{msg}", end="")
    for _ in range(tempo * 5):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print()

def barra_progresso(total=20, msg="Carregando"):
    print(f"\n{msg}")
    for i in range(total + 1):
        percent = int((i / total) * 100)
        barra = "█" * i + "-" * (total - i)
        print(f"\r[{barra}] {percent}%", end="")
        time.sleep(0.05)
    print("\n")

def menu1():
    print(f"""{AZUL}
======================================================
                                                  
    ____   ____   ____   _____ _______            
   |  _ \ / __ \ / __ \ / ____|__   __|    /|     
   | |_) | |  | | |  | | (___    | |      / |     
   |  _ <| |  | | |  | |\___ \   | |     /_  |__  
   | |_) | |__| | |__| |____) |  | |       |  _/  
   |____/ \____/ \____/|_____/   |_|       |_/    
              OPTIMIZER ENGINE v1.0               
                                                  
======================================================
{RESET}
[1] Limpeza de Pastas
[2] Otimização de Rede
[3] Aparência e Desempenho
[4] Verificação/Correção de Arquivos Corrompidos
[5] Alto Desempenho
[6] Otimização de Rede Completa
[7] EXECUTAR TUDO
[8] Limpar Lixeira
[9] Sair
[0] Créditos
""")

def menu_pastas():
    print("""
[1] Limpar Temp
[2] Prefetch
[3] Logs
[4] Limpar Tudo
[5] Voltar
""")

def menu_rede():
    print("""
[1] Limpar DNS
[2] Reset Winsock
[3] Ambos
[4] Voltar
""")

def menu_personalizacao():
    print("""
[1] Modo Desempenho
[2] Modo Aparência
[3] Reiniciar Explorer
[4] Voltar
""")

def exibir_creditos():
    print("\n" + "="*30)
    print("   ★ CRÉDITOS ★")
    print("   github.com/eliezerzx")
    print("="*30 + "\n")