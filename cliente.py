# cliente.py
import socket

# Conecta al servidor
def conectar():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("localhost", 5000))
    return cliente

# Envía mensajes al servidor
def enviar_mensajes(cliente):
    while True:
        mensaje = input("Escribí un mensaje (o 'listo' para salir): ")
        cliente.send(mensaje.encode())
        if mensaje.lower() == "listo":
            break
        respuesta = cliente.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")
    cliente.close()

# Punto de entrada del cliente
def main():
    cliente = conectar()
    enviar_mensajes(cliente)

if __name__ == "__main__":
    main()