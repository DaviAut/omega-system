"""
╔══════════════════════════════════════════════╗
║   SISTEMA ÔMEGA — RAIDER.CORP.U              ║
║   Launcher v4.1                              ║
║   Execute este arquivo para iniciar o app    ║
╚══════════════════════════════════════════════╝

Requisito: Python 3.6+
Não é necessário instalar nada além do Python padrão.
"""

import os
import sys
import subprocess
import webbrowser
import threading
import time

# Caminho do arquivo HTML (relativo ao script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE  = os.path.join(SCRIPT_DIR, "omega_system.html")

def check_html():
    if not os.path.exists(HTML_FILE):
        print("[ERRO] Arquivo omega_system.html não encontrado!")
        print(f"       Esperado em: {HTML_FILE}")
        input("\nPressione ENTER para sair...")
        sys.exit(1)

def launch_browser():
    """Abre o sistema no navegador padrão."""
    url = "file:///" + HTML_FILE.replace("\\", "/")
    print(f"\n[ÔMEGA] Iniciando sistema...")
    print(f"[ÔMEGA] URL: {url}")
    time.sleep(0.5)
    webbrowser.open(url)

def try_launch_app():
    """
    Tenta abrir como janela dedicada usando pywebview (se instalado).
    Caso contrário, usa o navegador padrão.
    """
    try:
        import webview
        print("[ÔMEGA] pywebview detectado — abrindo em janela dedicada...")
        window = webview.create_window(
            title        = "SISTEMA ÔMEGA — RAIDER.CORP.U",
            url          = HTML_FILE,
            width        = 1280,
            height       = 800,
            resizable    = True,
            min_size     = (900, 600),
            background_color = "#000000",
            frameless    = False,
        )
        webview.start(debug=False)
    except ImportError:
        print("[ÔMEGA] pywebview não instalado — usando navegador padrão.")
        print("[DICA ] Para janela nativa, instale com:  pip install pywebview")
        launch_browser()

def print_banner():
    RED   = "\033[91m"
    DIM   = "\033[2m\033[91m"
    RESET = "\033[0m"
    banner = f"""
{RED}
  ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗
 ██╔═══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗
 ██║   ██║██╔████╔██║█████╗  ██║  ███╗███████║
 ██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║
 ╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║
  ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
{RESET}{DIM}  RAIDER.CORP.U — SISTEMA SEGURO v4.1{RESET}
"""
    print(banner)

if __name__ == "__main__":
    print_banner()
    check_html()
    try_launch_app()
