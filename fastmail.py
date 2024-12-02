import smtplib
import signal
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("FastMail - By S3RGI09")
print("v1.0 estable")
print("FastHost Project")
servidor = None

def manejar_interrupcion(signal, frame):
    print("\nInterrupción recibida. Cerrando el servidor...")
    if servidor:
        servidor.quit()
        print("Conexión al servidor SMTP cerrada.")
    sys.exit(0)

signal.signal(signal.SIGINT, manejar_interrupcion)

def enviar_correo():
    global servidor
    destinatario = input("Ingrese la dirección de correo del destinatario: ")
    asunto = input("Ingrese el asunto del correo: ")
    cuerpo = input("Ingrese el cuerpo del correo: ")

    smtp_servidor = 'smtp.example.com'
    smtp_puerto = 587
    usuario = 'tu_correo@example.com'
    contrasena = 'tu_contrasena'

    mensaje = MIMEMultipart()
    mensaje['From'] = usuario
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        servidor = smtplib.SMTP(smtp_servidor, smtp_puerto)
        servidor.starttls()
        servidor.login(usuario, contrasena)
        servidor.send_message(mensaje)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        if servidor:
            servidor.quit()

if __name__ == "__main__":
    enviar_correo()
