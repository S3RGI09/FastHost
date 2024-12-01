# FastHost & FastMail
## FastHost
FastHost es un servidor web simple y ligero desarrollado en Python. Este proyecto te permite ejecutar un servidor web local que puede servir contenido HTML ingresado directamente o cargado desde un archivo en un directorio específico.

### Características

- Servidor web simple que escucha en `localhost` y un puerto configurable (por defecto `8080`).
- Permite ingresar el código HTML manualmente o cargarlo desde un archivo HTML.
- Responde a solicitudes HTTP con el contenido HTML proporcionado.
- Fácil de usar y configurar.

### Requisitos

- Python 3.x
- HTML, CSS y JavaScript en el mismo archivo

### Instalación

1. Clona o descarga el repositorio:
```
   git clone https://github.com/tu-usuario/FastHost.git
   cd FastHost
```
2. Ejecuta el script:
```
   python servidor_web.py
```
### Uso

Cuando ejecutas el script, se te pedirá que elijas cómo proporcionar el contenido HTML:

1. **Ingresar el código HTML directamente**: Puedes escribir el código HTML línea por línea y presionar Enter dos veces para terminar.
2. **Cargar el código HTML desde un archivo**: Ingresa la ruta del directorio y el nombre del archivo HTML para leer su contenido.

El servidor escuchará en `http://localhost:8080` y servirá el contenido proporcionado. Para detener el servidor, puedes presionar `Ctrl + C` en tu terminal.

### Ejemplo de ejecución
```
Seleccione una opción para proporcionar el contenido HTML:
1. Ingresar el código HTML directamente
2. Cargar el código HTML desde un archivo
Ingrese 1 o 2: 1
```
```
Ingrese el código HTML (presione Enter dos veces para terminar):
```
```html
<html>
<head>
    <title>Mi Servidor Web</title>
</head>
<body>
    <h1>¡Hola, mundo!</h1>
    <p>Este es un servidor web simple creado con Python.</p>
</body>
</html>
```
### Detalles técnicos

- Utiliza la biblioteca estándar de Python (`socket`) para crear un servidor web básico.
- Soporta solicitudes HTTP simples y responde con el contenido HTML proporcionado.
- No es adecuado para producción, pero es una excelente herramienta educativa y de prueba.

## FastMail
FastMail es un servidor de correo simple y ligero desarrollado en Python. Este proyecto permite enviar correos electrónicos desde la consola de manera sencilla.

### Características

- Envía correos electrónicos a través de un servidor SMTP configurado.
- Solicita la dirección del destinatario, el asunto y el cuerpo del mensaje.
- Imprime la respuesta del servidor de correo al enviar el mensaje.
- Ideal para pruebas y uso educativo.

### Requisitos

- Python 3.x

### Instalación

1. Clona o descarga el repositorio:
```
   git clone https://github.com/S3RGI09/FastHost
   cd FastHost
```

3. Ejecuta el script:
   `python FastHost`

### Uso

Cuando ejecutas el script, se te pedirá que ingreses la dirección de correo del destinatario, el asunto y el cuerpo del mensaje. Luego, se enviará el correo a través del servidor SMTP configurado y se imprimirá la respuesta del servidor.

### Ejemplo de ejecución
```
Ingrese la dirección de correo del destinatario: example@example.com
Ingrese el asunto del correo: Prueba de envío
Ingrese el cuerpo del correo: Este es un correo de prueba enviado desde FastMail.

Correo enviado exitosamente.
Respuesta del servidor: <respuesta del servidor SMTP>
```
### Detalles técnicos

- Utiliza la biblioteca `smtplib` de Python para enviar correos electrónicos a través de SMTP.
- Maneja la señal de interrupción `Ctrl + C` para cerrar la conexión correctamente.
- No es adecuado para producción, pero es útil para pruebas y demostraciones.

## Contribuciones

Si deseas contribuir a FastHost o FastMail, ¡siéntete libre de hacer un fork del repositorio y enviar un pull request!

## Licencia

Este proyecto está licenciado bajo la [Apache License 2.0](LICENSE).
