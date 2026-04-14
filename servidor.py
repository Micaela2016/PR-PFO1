# servidor.py
import socket
import sqlite3
import threading
from datetime import datetime

# ------------- Base de datos -------------
# Inicializacion de Base de datos
def inicializar_base():
    conexion = sqlite3.connect("mensajes.db")
    cursor = conexion.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)
    conexion.commit()
    conexion.close

# Guardado de mensaje en la Base de datos
def guardar_mensaje(texto, ip_cliente):
    conexion = sqlite3.connect("mensajes.db")
    cursor = conexion.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (texto, fecha, ip_cliente))
    conexion.commit()
    conexion.close()
    return fecha

# Manejo de cada conexión entrante
def handle_cliente(conexion, address):
    ip_cliente = address[0]
    print(f"Nueva conexión desde {ip_cliente}")
    while True:
        data = conexion.recv(1024).decode()
        if not data or data.lower() == "listo":
            break
        timestamp = guardar_mensaje(data, ip_cliente)
        if timestamp:
            respuesta = f"Mensaje recibido: {timestamp}"
        else:
            respuesta = "Error guardando el mensaje"
        conexion.send(respuesta.encode())
    conexion.close()
    print(f"Conexión cerrada con {ip_cliente}")

# ------------- Socket -------------
# Configuracion del socket
def inicializar_socket():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("localhost", 5000))
    servidor.listen(5)
    return servidor

# ------------- Punto de entrada -------------
def main():
    inicializar_base()
    servidor = inicializar_socket()
    while True:
        conn, addr = servidor.accept()
        hilo = threading.Thread(target=handle_cliente, args=(conn, addr))
        hilo.start()

if __name__ == "__main__":
    main()