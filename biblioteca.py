import os
import shutil
import subprocess
import winreg
from utils import barra_progresso, loading, VERDE, VERMELHO, RESET

def limpar_pasta(nome, caminho):
    caminho = os.path.expandvars(caminho)

    print(f"\n[+] Limpando {nome}")
    barra_progresso(10, "Removendo arquivos")

    if not os.path.exists(caminho):
        print(f"{VERMELHO}[ERRO] Caminho não encontrado{RESET}")
        return

    removidos, erros = 0, 0

    for item in os.listdir(caminho):
        try:
            path = os.path.join(caminho, item)
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            else:
                shutil.rmtree(path)
            removidos += 1
        except:
            erros += 1

    print(f"{VERDE}[✔] Concluído!{RESET} Removidos: {removidos} | Em uso: {erros}")

def limpar_temp():
    limpar_pasta("Temp", r"%temp%")
    limpar_pasta("Windows Temp", r"C:\Windows\Temp")

def limpar_prefetch():
    limpar_pasta("Prefetch", r"C:\Windows\Prefetch")

def limpar_logs():
    limpar_pasta("Logs", r"C:\Windows\Logs")

def limpar_dns():
    print("\n[+] Limpando DNS")
    loading()

    try:
        subprocess.run("ipconfig /flushdns", shell=True)
        print(f"{VERDE}[✔] DNS limpo{RESET}")
    except:
        print(f"{VERMELHO}[ERRO]{RESET}")

def resetar_winsock():
    print("\n[+] Resetando rede")
    loading()

    subprocess.run("netsh winsock reset", shell=True)
    print(f"{VERDE}[✔] Reset concluído{RESET}")

def esvaziar_lixeira():
    print("\n[+] Limpando lixeira")
    loading()

    subprocess.run("powershell Clear-RecycleBin -Force", shell=True)
    print(f"{VERDE}[✔] Lixeira limpa{RESET}")

def reparar_arquivos_sistema():
    print("\n[+] Verificando sistema")
    barra_progresso(15, "Executando SFC")

    subprocess.run("sfc /scannow", shell=True)
    print(f"{VERDE}[✔] Finalizado{RESET}")

def ajustar_efeitos_visuais(melhor=True):
    print("\n[+] Ajustando efeitos")
    loading()

    valor = "0" if melhor else "1"

    chave = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Control Panel\Desktop\WindowMetrics",
        0,
        winreg.KEY_SET_VALUE
    )

    winreg.SetValueEx(chave, "MinAnimate", 0, winreg.REG_SZ, valor)
    winreg.CloseKey(chave)

    print(f"{VERDE}[✔] Ajustado{RESET}")

def reiniciar_explorer():
    print("\n[+] Reiniciando Explorer")
    loading()

    os.system("taskkill /f /im explorer.exe")
    os.system("start explorer.exe")

def ativar_alto_desempenho():
    print("\n[+] Ativando alto desempenho")
    loading()

    subprocess.run("powercfg -setactive SCHEME_MIN", shell=True)
    print(f"{VERDE}[✔] Ativado{RESET}")

def otimizar_rede():
    print("\n[+] Otimizando rede")
    barra_progresso(10)

    comandos = [
        "netsh winsock reset",
        "netsh int ip reset",
        "ipconfig /flushdns"
    ]

    for cmd in comandos:
        subprocess.run(cmd, shell=True)

    print(f"{VERDE}[✔] Rede otimizada{RESET}")

def exec_all():
    print("\n🚀 EXECUTANDO OTIMIZAÇÃO COMPLETA\n")

    limpar_temp()
    limpar_prefetch()
    limpar_dns()
    resetar_winsock()
    limpar_logs()
    esvaziar_lixeira()
    ativar_alto_desempenho()
    otimizar_rede()
    reparar_arquivos_sistema()

    print(f"\n{VERDE}🔥 SISTEMA OTIMIZADO!{RESET}")