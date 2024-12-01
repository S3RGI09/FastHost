import socket
import os

print("FastHost - by S3RGI09")
print("v1.0 estable")
def obtener_codigo_html():
    print("Seleccione una opción para proporcionar el contenido HTML:")
    print("1. Ingresar el código HTML directamente")
    print("2. Cargar el código HTML desde un archivo")

    opcion = input("Ingrese 1 o 2: ")

    if opcion == '1':
        print("\nIngrese el código HTML (presione Enter dos veces para terminar):")
        html = ""
        while True:
            linea = input()
            if linea == "":
                break
            html += linea + "\n"
        return html

    elif opcion == '2':
        directorio = input("Ingrese la ruta del directorio donde se encuentra el archivo HTML: ")
        if not os.path.isdir(directorio):
            print("Error: El directorio no existe.")
            return None

        archivo = input("Ingrese el nombre del archivo HTML (con extensión .html): ")
        ruta_archivo = os.path.join(directorio, archivo)

        if not os.path.isfile(ruta_archivo):
            print("Error: El archivo no existe.")
            return None

        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            html = f.read()
        return html

    else:
        print("Opción no válida.")
        return None

def iniciar_servidor():
    host = 'localhost'
    puerto = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, puerto))
    server_socket.listen(5)

    print(f"Servidor iniciado en http://{host}:{puerto}")

    html_contenido = obtener_codigo_html()
    if html_contenido is None:
        print("No se pudo iniciar el servidor. El contenido HTML es inválido.")
        return

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Conexión recibida de {client_address}")

            request = client_socket.recv(1024).decode('utf-8')
            print(f"SOLICITUD:\n{request}")

            response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

{html_contenido}
"""

            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    iniciar_servidor()