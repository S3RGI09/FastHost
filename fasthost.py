import socket
import os

print("FastHost - by S3RGI09")
print("v1.0 stable")
def get_html_code():
    print("Select an option to provide the HTML content:")
    print("1. Enter the HTML code directly")
    print("2. Load the HTML code from a file")

    option = input("Enter 1 or 2: ")

    if option == '1':
        print("\nEnter the HTML code (press Enter twice to finish):")
        html = ""
        while True:
            line = input()
            if line == "":
                break
            html += line + "\n"
        return html

    elif option == '2':
        directory = input("Enter the path to the directory where the HTML file is located: ")
        if not os.path.isdir(directory):
            print("Error: The directory does not exist.")
            return None

        file_name = input("Enter the name of the HTML file (with .html extension): ")
        file_path = os.path.join(directory, file_name)

        if not os.path.isfile(file_path):
            print("Error: The file does not exist.")
            return None

        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        return html

    else:
        print("Invalid option.")
        return None

def start_server():
    host = 'localhost'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started at http://{host}:{port}")

    html_content = get_html_code()
    if html_content is None:
        print("Could not start the server. Invalid HTML content.")
        return

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection received from {client_address}")

            request = client_socket.recv(1024).decode('utf-8')
            print(f"REQUEST:\n{request}")

            response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

{html_content}
"""

            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
