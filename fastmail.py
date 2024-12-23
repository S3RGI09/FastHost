import smtplib
import signal
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("FastMail - By S3RGI09")
print("v1.0 stable")
print("FastHost Project")
server = None

def handle_interruption(signal, frame):
    print("\nInterruption received. Closing the server...")
    if server:
        server.quit()
        print("SMTP server connection closed.")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interruption)

def send_email():
    global server
    recipient = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    smtp_server = 'smtp.example.com'
    smtp_port = 587
    user = 'your_email@example.com'
    password = 'your_password'

    message = MIMEMultipart()
    message['From'] = user
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(user, password)
        server.send_message(message)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending the email: {e}")
    finally:
        if server:
            server.quit()

if __name__ == "__main__":
    send_email()
