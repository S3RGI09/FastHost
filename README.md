![Versión](https://img.shields.io/badge/versión-2.8-blue)
![Licencia](https://img.shields.io/badge/licencia-Apache-green)
# ![FastHost Project](https://github.com/user-attachments/assets/71b1e13e-b816-428c-982a-fc06e0273b78)

## FastHost
FastHost is a simple and lightweight web server developed in Python. This project allows you to run a local web server that can serve HTML content entered directly or loaded from a file in a specified directory.

### Features

- Simple web server that listens on `localhost` and a configurable port (default `8080`).
- Allows entering HTML code manually or loading it from an HTML file.
- Responds to HTTP requests with the provided HTML content.
- Easy to use and configure.

 ### Requirements

- Python 3.x
- HTML, CSS, and JavaScript in the same file

### Installation

1. Clone or download the repository:
```
git clone https://github.com/S3RGI09/FastHost.git
cd FastHost
```
2. Run the script:
```
python fasthost.py
```
### Usage

When you run the script, you will be asked to choose how to provide the HTML content:

1. **Enter HTML code directly**: You can type the HTML code line by line and press Enter twice to finish.
2. **Load HTML code from a file**: Enter the directory path and name of the HTML file to read its content.

The server will listen on `http://localhost:8080` and serve the provided content. To stop the server, you can press `Ctrl + C` in your terminal.

 ### Example of execution
```
Select an option to provide the HTML content:
1. Enter the HTML code directly
2. Load the HTML code from a file
Enter 1 or 2: 1
```
```
Enter the HTML code (press Enter twice to finish):
```
```html
<html>
<head>
<title>My Web Server</title>
</head>
<body>
<h1>Hello, world!</h1>
<p>This is a simple web server built with Python.</p>
</body>
</html>
```
### Technical details

- Uses the Python standard library (`socket`) to create a basic web server.
- Supports simple HTTP requests and responds with the provided HTML content.
- Not suitable for production, but is an excellent educational and testing tool.

 >[!warning]
>While static content such as HTML, CSS and JavaScript is not dangerous, the server can be compromised by a third party. You are responsible for the security of your server.
>The server is designed for low traffic and use on a local network, although it is possible to redirect the ports of your router to point to the port of your private IP through your public IP, it is not recommended.

>[!note]
>The server is designed to work with low load, if your website is going to receive high traffic, it is recommended to use other alternatives such as **Nginx** or **Apache**

## FastMail
FastMail is a simple and lightweight mail server developed in Python. This project allows you to send emails from the console in a simple way.

### Features

- Sends emails through a configured SMTP server.
- Requests the recipient's address, subject and body of the message.
- Prints the mail server's response when sending the message.
- Ideal for testing and educational use.

 ### Requirements

- Python 3.x

### Installation

1. Clone or download the repository:
```
git clone https://github.com/S3RGI09/FastHost
cd FastHost
```

3. Run the script:
`python FastHost`

### Usage

When you run the script, you will be asked to enter the recipient's email address, subject, and body of the message. The email will then be sent through the configured SMTP server and the server's response will be printed.

### Example of execution
```
Enter the recipient's email address: example@example.com
Enter the email subject: Test Sending
Enter the email body: This is a test email sent from FastMail.

Email sent successfully.
 Server response: <SMTP server response>
```
### Technical details

- Uses Python's `smtplib` library to send emails via SMTP.
- Handles the `Ctrl+C` kill signal to close the connection gracefully.
- Not suitable for production, but useful for testing and demos.

>[!warning]
>Try not to send an email to addresses from well-known providers such as Gmail, Yahoo!, Outlook, Hotmail, ProtonMail, TutaMail and many others. These companies can intercept your email as **spam** and block the IP from which it comes. Even if the content of the email is harmless, the server can enter the address and IP into a blacklist for not having a domain.

>[!note]
>We recommend using a domain you own to send emails. Although the program can work without it, it is more convenient and easier to use a domain.

 ## Contributions

If you would like to contribute to FastHost or FastMail, feel free to fork the repository and submit a pull request!

## License

This project is licensed under the [Apache License 2.0](LICENSE).
