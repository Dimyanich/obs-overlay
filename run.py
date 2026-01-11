import os
import http.server
import socketserver
import webbrowser
import threading

# Папка скрипта как рабочая директория
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# Авто-открытие панели и оверлея
def open_pages():
    webbrowser.open(f"http://localhost:{PORT}/control.html")
    webbrowser.open(f"http://localhost:{PORT}/overlay.html")

threading.Timer(1.0, open_pages).start()

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    print("Нажмите Enter для выхода...")
    threading.Thread(target=lambda: input()).start()
    httpd.serve_forever()
