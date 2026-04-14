# PR-PFO1

# Alumna: Micaela Orellano Comision C

# Chat Cliente-Servidor con Sockets y SQLite

Este proyecto forma parte de la Propuesta Formativa Obligatoria (PFO-1) y tiene como objetivo implementar un sistema de comunicación básico entre un cliente y un servidor utilizando sockets en Python. Los mensajes enviados por los clientes se almacenan en una base de datos SQLite, y el servidor responde con una confirmación que incluye la marca de tiempo.

---

## Objetivo

- Configurar un servidor de sockets que reciba mensajes de clientes.
- Almacenar cada mensaje en una base de datos SQLite.
- Responder al cliente con una confirmación tipo: `Mensaje recibido: <timestamp>`.
- Aplicar buenas prácticas de modularización, manejo de errores y documentación.

---

## Tecnologías utilizadas

- Python 3
- Sockets TCP/IP (`socket`)
- Base de datos SQLite (`sqlite3`)
- Manejo de fechas (`datetime`)

## Como ejecutar
Iniciar el servidor Abrí una terminal y ejecutá:

python servidor.py

Iniciar el cliente En otra terminal, ejecutá:

python cliente.py

Enviar mensajes 
Escribí cualquier mensaje en el cliente. 
El servidor responderá con: Mensaje recibido: <timestamp> 
Para finalizar la sesión, escribí: listo